from odoo import models, fields, api, _  # type:ignore
from odoo.exceptions import ValidationError, UserError  # type:ignore


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ma_dh = fields.Char(
        string='Mã ĐH',
        compute='_compute_ma_dh'
    )
    name = fields.Char(
        string="Tên ĐH",
        required=True,
        default=""
    )
    create_order_date = fields.Date(
        string="Đặt hàng",
        default=lambda self: fields.Date.today()
    )
    vnd_rate = fields.Float(
        string="Tỷ giá",
        readonly="True",
        default=lambda self: (
            self.env["res.currency"].search([("name", "=", "VND")]).rate_ids[0].company_rate
        ) if self.env["res.currency"].search([("name", "=", "VND")]).rate_ids else 0.0
    )
    vnd_total = fields.Integer(
        string="Trị giá(VND)",
        compute='_compute_vnd_total'
    )
    currency_id_1 = fields.Many2one(
        'res.currency',
        default=lambda self: (
            self.env.ref('base.VND').id
        )
    )

    def action_confirm(self):
        """ Confirm the given quotation(s) and set their confirmation date.

        If the corresponding setting is enabled, also locks the Sale Order.

        :return: True
        :rtype: bool
        :raise: UserError if trying to confirm locked or cancelled SO's
        """
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                "It is not allowed to confirm an order in the following states: %s",
                ", ".join(self._get_forbidden_state_confirm()),
            ))

        self.order_line._validate_analytic_distribution()

        for order in self:
            order.validate_taxes_on_sales_order()
            if order.partner_id in order.message_partner_ids:
                continue
            order.message_subscribe([order.partner_id.id])

        self.write(self._prepare_confirmation_values())

        # Context key 'default_name' is sometimes propagated up to here.
        # We don't need it and it creates issues in the creation of linked records.
        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()
        # if self.env.user.has_group('sale.group_auto_done_setting'):
        #     self.action_done()

        return True

    @api.depends('vnd_rate')
    def _compute_vnd_total(self):
        for rc in self:
            rc.vnd_total = rc.vnd_rate * rc.amount_total

    def _compute_ma_dh(self):
        for rc in self:
            if rc.id:
                rc.ma_dh = "{:05d}".format(rc.id)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        # Clear the values of dependent fields
        self.order_line = False
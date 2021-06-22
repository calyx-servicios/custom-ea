# flake8: noqa
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _
from odoo.tools.misc import format_date
from datetime import datetime, timedelta


class ReportAccountAgedPartner(models.AbstractModel):
    _inherit = "account.aged.partner"

    def get_columns_name(self, options):
        columns = [{}]
        columns += [
            {
                "name": v,
                "class": "number",
                "style": "white-space:nowrap;",
            }
            for v in [
                _("F.&nbsp;Em.").replace("&nbsp;", " "),
                _("F.&nbsp;Vec.").replace("&nbsp;", " "),
                _("Dias&nbsp;vencida").replace("&nbsp;", " "),
                _("Socio"),
                _("Not&nbsp;due&nbsp;on %s").replace("&nbsp;", " ")
                % format_date(self.env, options["date"]["date"]),
                _("1&nbsp;-&nbsp;30").replace("&nbsp;", " "),
                _("31&nbsp;-&nbsp;60").replace("&nbsp;", " "),
                _("61&nbsp;-&nbsp;90").replace("&nbsp;", " "),
                _("91&nbsp;-&nbsp;120").replace("&nbsp;", " "),
                _("Older"),
                _("Total"),
            ]
        ]
        return columns

    def _verify_number(self, number):
        check_number = isinstance(number, float)
        if check_number:
            return True
        else:
            return False

    def _check_date_number(self, d):
        days = 0
        end = datetime.today()
        while d.date() < end.date():
            days += 1
            d += timedelta(days=1)
        return days

    @api.model
    def get_lines(self, options, line_id=None):
        sign = -1.0 if self.env.context.get("aged_balance") else 1.0
        lines = []
        account_types = [self.env.context.get("account_type")]
        results, total, amls = (
            self.env["report.account.report_agedpartnerbalance"]
            .with_context(include_nullified_amount=True)
            ._get_partner_move_lines(
                account_types, self._context["date_to"], "posted", 30
            )
        )
        for values in results:
            if (
                line_id
                and "partner_%s" % (values["partner_id"],) != line_id
            ):
                continue
            vals = {
                "id": "partner_%s" % (values["partner_id"],),
                "name": values["name"],
                "level": 2,
                "columns": [
                    {
                        "name": self.format_value(sign * v)
                        if self._verify_number(v)
                        else v
                    }
                    for v in [
                        "",
                        "",
                        "",
                        "",
                        values["direction"],
                        values["4"],
                        values["3"],
                        values["2"],
                        values["1"],
                        values["0"],
                        values["total"],
                    ]
                ],
                "trust": values["trust"],
                "unfoldable": True,
                "unfolded": "partner_%s" % (values["partner_id"],)
                in options.get("unfolded_lines"),
            }
            lines.append(vals)
            if "partner_%s" % (values["partner_id"],) in options.get(
                "unfolded_lines"
            ):
                for line in amls[values["partner_id"]]:
                    aml = line["line"]
                    caret_type = "account.move"
                    if aml.invoice_id:
                        date_due_invoice = datetime.strptime(
                            aml.invoice_id.date_due, "%Y-%m-%d"
                        )
                        days_due = self._check_date_number(
                            date_due_invoice
                        )
                        caret_type = (
                            "account.invoice.in"
                            if aml.invoice_id.type
                            in ("in_refund", "in_invoice")
                            else "account.invoice.out"
                        )
                    elif aml.payment_id:
                        caret_type = "account.payment"
                        days_due = ""

                    nv = []
                    nv.append(
                        format_date(
                            self.env, aml.invoice_id.date_invoice
                        )
                        or ""
                    )
                    nv.append(
                        format_date(self.env, aml.invoice_id.date_due)
                        or ""
                    )
                    nv.append(days_due)
                    nv.append(aml.invoice_id.associate_id.name)

                    for i in range(7):
                        val = (
                            line["period"] == 6 - i
                            and self.format_value(sign * line["amount"])
                            or ""
                        )
                        nv.append(val)

                    vals = {
                        "id": aml.id,
                        # INICIO CAMBIO ADDOC
                        "name": aml.move_id.display_name,
                        # 'name': aml.move_id.name if aml.move_id.name else '/'
                        # FIN CAMBIO ADDOC
                        "caret_options": caret_type,
                        "level": 4,
                        "parent_id": "partner_%s"
                        % (values["partner_id"],),
                        "columns": [
                            {
                                "name": v,
                            }
                            for v in [
                                x
                                for x in nv
                            ]
                        ],
                        "action_context": aml.get_action_context(),
                    }
                    lines.append(vals)
                vals = {
                    "id": values["partner_id"],
                    "class": "o_account_reports_domain_total",
                    "name": _("Total "),
                    "parent_id": "partner_%s" % (values["partner_id"],),
                    "columns": [
                        {
                            "name": self.format_value(sign * v)
                            if self._verify_number(v)
                            else v
                        }
                        for v in [
                            "",
                            "",
                            "",
                            "",
                            values["direction"],
                            values["4"],
                            values["3"],
                            values["2"],
                            values["1"],
                            values["0"],
                            values["total"],
                        ]
                    ],
                }
                lines.append(vals)
        if total and not line_id:
            total_line = {
                "id": 0,
                "name": _("Total"),
                "class": "total",
                "level": "None",
                "columns": [
                    {
                        "name": self.format_value(sign * v)
                        if self._verify_number(v)
                        else v
                    }
                    for v in [
                        "",
                        "",
                        "",
                        "",
                        total[6],
                        total[4],
                        total[3],
                        total[2],
                        total[1],
                        total[0],
                        total[5],
                    ]
                ],
            }
            lines.append(total_line)
        return lines

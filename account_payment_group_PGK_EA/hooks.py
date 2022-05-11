# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging
from openerp import api, SUPERUSER_ID
_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    """
    calculate matched_move_line_ids_qty after install
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    payments = env['account.payment.group'].search([('partner_type','=','customer')])#('currency_id','in',(20,3))])
    for rec in payments:
        try:
            rec._compute_matched_move_line_ids()
        except Exception:
            pass


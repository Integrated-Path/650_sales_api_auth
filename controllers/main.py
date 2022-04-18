from odoo.addons.base_rest.controllers import main


class SessionRestController(main.RestController):
    _root_path = "/session/"
    _collection_name = "wolfgym.session.rest.services"

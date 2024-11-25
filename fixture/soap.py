from suds.client import Client
from suds import WebFault


class SoapHepler:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_login(username, password)
        except WebFault:
            return False

    def get_project_list_soap(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return None

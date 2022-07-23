import logging
from typing import Dict
from requests import Session, Response
from tab_vizportal.server.endpoints import Endpoint
from urllib.parse import urlparse


class Sites(Endpoint):

    def __init__(self, session : Session , base_url : str, base_headers : Dict):
        self.session = session
        self.base_headers = base_headers
        self.base_url = base_url
        domain = urlparse(base_url).netloc
        super().__init__(host=domain)

    def switch_site(self, new_params : Dict) -> Response:
        api_url = "vizportal/api/web/v1/switchSite"
        response = super().vizportal_api(api_url, new_params)
        return response
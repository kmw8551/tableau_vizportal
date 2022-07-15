
import logging
import requests
from typing import Dict, List, Union
from requests import Session
from tab_vizportal.server.endpoints import Endpoint
from tab_vizportal.server.api.data_alert_api import DataAlert
from tab_vizportal.server.api.view_api import View
from urllib.parse import urlparse


class APIFactory:

    @staticmethod
    def create_api_request(name,  session : Session , base_url : str, base_headers : Dict):

        if name  == "DataAlerts":
            base_headers.setdefault("X-Requested-With","XMLHttpRequest")
            return DataAlert(session, base_url, base_headers)

        elif name == "View":
            return View(session, base_url, base_headers)

        else:
            raise Exception("Method Not Found")





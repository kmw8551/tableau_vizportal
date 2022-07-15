import logging
import os
from server.api.auth_api import Auth
from server.api.data_alert_api import DataAlert
from server.api.view_api import View
from server.api.api_factory import APIFactory

logging.basicConfig(level=logging.INFO)

tab_id = os.environ['TABLEAU_ID']
tab_passwd = os.environ['TABLEAU_PWD']
tab_server = os.environ['TABLEAU_SERVER']

# First, Login VizPortal
auth = Auth(tab_id, tab_passwd, tab_server)
resp_session, cookies, xsrf_token = auth.auth_login()

# Basic Info - You can find the headers option in the Network tab in Developer's console in Chrome
base_url = auth.base_url
base_headers = {"Content-Type": "application/json;charset=UTF-8",
                             "Accept": "application/json, text/plain, */*",
                             "Connection": "keep-alive"}

# using APIFactory
data_alert = APIFactory.create_api_request('DataAlerts', resp_session , base_url, base_headers)
view = APIFactory.create_api_request('View', resp_session , base_url, base_headers)

# Example 1. Get DataAlert Data

operator_params1 = {
                    "page":{"startIndex":0},
                    "order":[{"field":"title", "ascending":"true"}],
                  }
# 
response_data_alert = data_alert.get_data_alerts(operator_params1)

if status_code_da:= response_data_alert.status_code == 200:
    print("DataAlerts Method working!!!")


# Example 2. Get View 

operator_params2 = {
                    "page":{"startIndex":0},
                    "order":[{"field":"title", "ascending":"true"}],
                  }
response_view = view.get_views(operator_params2)
if status_code_view:= response_view.status_code == 200:
    print("View Method working!!!")

# Close Session
auth.auth_logout()
import logging
import os
from server.api.auth_api import Auth
from server.api.data_alert_api import DataAlert
from server.api.view_api import View

logging.basicConfig(level=logging.INFO)

tab_id = os.environ['TABLEAU_ID']
tab_passwd = os.environ['TABLEAU_PWD']
tab_server = os.environ['TABLEAU_SERVER']

# First, Login VizPortal
auth = Auth(tab_id, tab_passwd, tab_server)
resp_session, cookies, xsrf_token = auth.auth_login()
base_url = auth.base_url

# Example 1. Get DataAlert Data
data_alert = DataAlert(resp_session , base_url)
operator_params = {
                    "page":{"startIndex":0},
                    "order":[{"field":"title", "ascending":"true"}],
                  }
status_code, resp_headers, content =  data_alert.get_data_alerts(operator_params)


# Example 2. Get View By Path
view = View(resp_session , base_url)

# assign view_id and sheet number
view_id = 111111
sheet_no = 1

operator_params = {"path" : f"{view_id}/sheet{sheet_no}"}
status_code, resp_headers, content = view.get_view_by_path(operator_params)

auth.auth_logout()
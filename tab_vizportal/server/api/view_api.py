import logging
from requests import Session
from tab_vizportal.server.endpoints import Endpoint
from urllib.parse import urlparse


class View(Endpoint):

    def __init__(self, session: Session, base_url: str):
        self.session = session
        self.base_headers = {"Content-Type": "application/json;charset=UTF-8",
                             "Accept": "application/json, text/plain, */*",
                             "Connection": "keep-alive"}
        self.base_url = base_url
        domain = urlparse(base_url).netloc
        super().__init__(host=domain)

    def get_views(self):
        pass

    def get_view_by_path(self, new_params):
        self.base_headers["Host"] = self.host
        self.base_headers["Origin"] = self.base_url
        self.base_headers["X-XSRF-TOKEN"] = self.session.cookies['XSRF-TOKEN']

        resp_session = self.api_request(base_url=self.base_url,
                                        http_method='POST',
                                        api_url="vizportal/api/web/v1/getViewByPath",
                                        headers=self.base_headers,
                                        params=new_params,
                                        cookies=self.session.cookies)

        return (resp_session.status_code, resp_session.headers, resp_session.content.decode('utf-8'))

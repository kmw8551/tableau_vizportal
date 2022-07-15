import logging
import sys
import requests
import json

# Python3 only
if sys.version_info.major > 3 or sys.version_info.minor == 9:
    from collections.abc import Callable
    from typing import Any, Dict, Optional, TYPE_CHECKING
else:
    from typing import Any, Callable, Dict, Optional, TYPE_CHECKING

XML_CONTENT_TYPE = "text/xml"
JSON_CONTENT_TYPE = "application/json"
HTML_CONTENT_TYPE = "text/html"

class Endpoint(object):
    """
    Endpoint Class

    Attributes
    host : Tableau Host
    headers : Request headers
    """
    def __init__(self, host):
        self.host = host
        self._headers = None
        self._method = None
        self._params = None
        self._cookies = None

    @property
    def headers(self):
        return self._headers
    
    @headers.setter
    def headers(self, headers):
        if not isinstance(headers, Dict):
            raise ValueError("Headers must be of Dict type")
        self._headers = headers

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method_val):
        if not isinstance(method_val, str):
            raise ValueError("Method_Val must be of String type")
        self._method = method_val

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        if not isinstance(params, Dict):
            raise ValueError("Params must be of Dict type")
        self._params = params

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        if not isinstance(cookies, Dict):
            raise ValueError("Cookies must be of Dict type")
        self._cookies = cookies


    def api_request(self,
                    base_url,
                    http_method,
                    api_url,
                    headers=None,
                    method=None,
                    params=None,
                    cookies=None):


        request_url = base_url + '/' + api_url
        api_method = api_url.split('/')[-1]
        payload= json.dumps({"method": api_method, "params" : params}) if method is None else json.dumps({"method": method, "params" : params})

        return requests.request(method=http_method, url=request_url, headers=headers, data=payload, cookies=cookies)
        # return requests.request(method=http_method, url=request_url, headers=headers, data=payload)
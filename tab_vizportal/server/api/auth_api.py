import logging
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from requests import RequestException ,  HTTPError
from tab_vizportal.server.endpoints import Endpoint
from tab_vizportal.server.api.site_api import Sites
from urllib.parse import urlparse

logger = logging.getLogger("tableau.vizportal.login")

class Auth(Endpoint):

    def __init__(self, tableau_id, tableau_passwd, base_url, site_name) :

        self._tableau_id = tableau_id
        self._tableau_passwd = tableau_passwd
        self.base_url = base_url
        self.site_name = site_name

        domain = urlparse(base_url).netloc
        super().__init__(host=domain)

        self.session = None

    def get_public_key(self, base_url):
        resp = self.api_request(base_url, 'POST', 'vizportal/api/web/v1/generatePublicKey')
        if resp.status_code == 200:
            resp_json = resp.json()
            pub_kid, pub_key = resp_json["result"]["keyId"], resp_json["result"]["key"]
            self.key_id, self.key = pub_kid, pub_key
            logging.debug("VizPortal Public Key Info:\n  Key ID : {}\n  Key : {}".format(pub_kid, pub_key))
            return (pub_kid, pub_key)
        else:
            logging.error("Request failed status code : {}".format(resp.status_code))
            raise RequestException("Request failed status code : {}".format(resp.status_code))

    def encrypt_passwd(self, passwd, n, e):
        logging.info("Encrypting Password")
        rsa_public_key = RSA.construct((int(n, 16), int(e, 16)))
        cipher = PKCS1_v1_5.new(rsa_public_key)
        byte_passwd = passwd.encode()
        rsa_encrypt_val = cipher.encrypt(byte_passwd)
        return binascii.b2a_hex(rsa_encrypt_val)

    def auth_login(self):
        pub_kid, pub_key = self.get_public_key(self.base_url)

        encrypt_pw = self.encrypt_passwd(self._tableau_passwd, pub_key['n'], pub_key['e'])
        decrypt_pw = encrypt_pw.decode()

        params= {"username": self._tableau_id, "encryptedPassword": decrypt_pw, "keyId": pub_kid}
        print("passing params : {}".format(params))
        headers = {
            'content-type': "application/json;charset=UTF-8",
            'accept': "application/json, text/plain, */*",
            'cache-control': "no-cache"
        }

        resp_session = self.api_request(base_url= self.base_url,
                                        http_method= 'POST',
                                        api_url= "vizportal/api/web/v1/login",
                                        headers=headers,
                                        params=params)

        # print(resp_session.json())

        self.session = resp_session

        print("status code = %s" % resp_session.status_code)
        if int(resp_session.status_code) not in [200, 201, 204, 206]:
            logging.error("Http Error")
            raise HTTPError

        logging.info("Login Success")
        logging.info("Content : %s" % resp_session.content)

        cookies = resp_session.cookies
        xsrf_token = resp_session.cookies["XSRF-TOKEN"]
        logging.info("Session Cookies : {}".format(self._cookies))

        new_header= headers
        new_header['X-XSRF-TOKEN'] = xsrf_token
        operator_params = {
            "urlName": f"{self.site_name}"

        }

        resp_session_after_switch_site = self.api_request(base_url=self.base_url,
                                         http_method='POST',
                                         api_url="vizportal/api/web/v1/switchSite",
                                         headers=new_header,
                                         params=operator_params,
                                         cookies=cookies)


        return resp_session_after_switch_site

    def auth_logout(self):
        self.session.close()






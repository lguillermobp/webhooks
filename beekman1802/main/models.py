from django.db import models
import asyncio
import json
from requests_oauthlib import OAuth1Session

class Class_NetSuite():
   
    def __init__(self, payload):
        
       # CLIENT_KEY: str = "adb62c969e3de81813105bcbdf1371f9741671ccfc7909ab162e24f1588ad4ad"
       # CLIENT_SECRET: str = "d537386d481f643eed5aea50b509a7af94977e610b5028143613d9bad58726e4"
       # ACCESS_KEY: str = "8b3f30d99c0fd7775a1532adbf9cbe1cbd9110b0902134091402817e6f1a274b"
       # ACCESS_SECRET: str = "abee94967d0834e36f560cf636badf9beb0df0b082b8e2e3275cb41134731746"

        CLIENT_KEY: str = "fd6cd72933c498b60ff340d8d2af2bdc5c16f0382359252b5d026fadf309f635"
        CLIENT_SECRET: str = "7e7299cffe5bc0fb2b2d5951b099d2e20c0a4cbd35a38efc33fea6de61f06d66"
        ACCESS_KEY: str = "acb8e0cd9f6f1b96c2195c110aafa21dc043ead933f721443420ca1ae72e5f76"
        ACCESS_SECRET: str = "356a683de3d97e5b701e83be7caae269eef406492644a36db2a00144e7df24bb"


        SIGNATURE_METHOD: str = "HMAC-SHA256"
        REALM_ID: str = "3374911"
        SCRIPT_ID: int = 2446
        DEPLOY_ID: int = 1
        URL: str = f"https://{REALM_ID}.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script={SCRIPT_ID}&deploy={DEPLOY_ID}"

        oauth = OAuth1Session(
            client_key=CLIENT_KEY,
            client_secret=CLIENT_SECRET,
            resource_owner_key=ACCESS_KEY,
            resource_owner_secret=ACCESS_SECRET,
            realm=REALM_ID,
            signature_method=SIGNATURE_METHOD
            )
        if not payload:
            data = {            "error": "POST is comming in blank"             }
        else:
            data = payload

        headers = {
            "Content-Type": "application/json"
        }

        self.res = oauth.post(URL, data=json.dumps(data), headers=headers)
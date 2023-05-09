import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredentials:
    consumer_key = 'Tw6L7vGoF3w98hFscF32iAeMikyYXYUG'
    consumer_secret = ' UPqljDDKCMPcFot2'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

class MpesaAccessToken:
    r = requests.get(MpesaC2bCredentials.api_URL,
                   auth=HTTPBasicAuth(MpesaC2bCredentials.consumer_key,
                                       MpesaC2bCredentials.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
   

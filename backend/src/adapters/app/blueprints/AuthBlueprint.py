from flask import Blueprint, jsonify, url_for, redirect, request

import json
from oauthlib.oauth2 import WebApplicationClient
import requests

from flask import current_app as app

auth = Blueprint('auth', __name__,)


#Disable SSL Verification
import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


@auth.route('/', methods = ['GET'])
def Auth():
    try:


        GOOGLE_CLIENT_ID = '890513067732-pag2evg2g4pa0aqhs2cj2sn5739hatme.apps.googleusercontent.com'
        GOOGLE_CLIENT_SECRET = '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'
        GOOGLE_DISCOVERY_URL = (
            "https://accounts.google.com/.well-known/openid-configuration"
        )

        client = WebApplicationClient(GOOGLE_CLIENT_ID)

        google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()

        authorization_endpoint = google_provider_cfg["authorization_endpoint"]


        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri="http://localhost:8000/auth/callback",
            scope=["openid", "email", "profile"],
        )

        return redirect(request_uri)

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500


@auth.route("/callback", methods= ['GET'])
def callback():

    # Get authorization code Google sent back to you
    code = request.args.get("code")
    
    GOOGLE_CLIENT_ID = '890513067732-pag2evg2g4pa0aqhs2cj2sn5739hatme.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    client = WebApplicationClient(GOOGLE_CLIENT_ID)
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Get Access Token
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Get user information
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    print(userinfo_response.json())
    

    return 'ok'
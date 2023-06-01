import os
from django.contrib.sessions.backends.db import SessionStore
import logging
import requests

def getRole(request):
    login_data = request.COOKIES.get('session')

    if login_data:
        response = requests.get(getUserDataUrl(), cookies=request.COOKIES)

        logging.warning(response.json()['userinfo'].keys())

        user_data = response.json()['userinfo']
        request.session['user'] = user_data

        logging.warning(os.environ.get('AUTH0_DOMAIN') + '/role')

        role = user_data[os.environ.get('AUTH0_DOMAIN') + '/role']

        return role
    else:
        return ''

def getLoginUrl():
    auth_host = os.environ.get('AUTH_SERVICE_HOST')
    https = "https" if os.environ.get("HTTPS") == "True" else "http"
    return f'{https}://{auth_host}/login'

def getUserDataUrl():
    auth_host = os.environ.get('AUTH_SERVICE_HOST')
    https = "https" if os.environ.get("HTTPS") == "True" else "http"
    return f'{https}://{auth_host}/api/user'
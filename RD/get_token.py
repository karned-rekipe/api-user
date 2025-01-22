import logging
from keycloak_params import *

logging.basicConfig(level=logging.INFO)

def get_token():
    token_url = f"https://{KEYCLOAK_HOST}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
    data = {
        "client_id": KEYCLOAK_CLIENT_ID,
        "client_secret": KEYCLOAK_CLIENT_SECRET,
        "grant_type": "password",
        "username": KEYCLOAK_ADMIN_USER,
        "password": KEYCLOAK_ADMIN_PASSWORD
    }

    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    logging.info(f"Access token: {access_token}")
    return access_token

def record_token():
    access_token = get_token()
    with open("access_token.txt", "w") as f:
        f.write(access_token)

record_token()
import json
import logging

import requests

with open("access_token.txt") as f:
    KEYCLOAK_ACCESS_TOKEN = f.read().strip()
KEYCLOAK_HOST = 'iam.karned.bzh'
KEYCLOAK_REALM  ='Karned'

username = 'tutu'

users_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users"
headers = {
    "Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"
}

data = {
    "username": username,
    "firstName": "toto",
    "lastName": "labourde",
    "email": f"{username}@example.com",
    "emailVerified": True,
    "enabled": True,
    "credentials": [
        {
            "type": "password",
            "value": f"{username}password",
            "temporary": False
        }
    ]
}

response = requests.post(users_url, headers=headers, json=data)
logging.info(f"Status: {response.status_code}")



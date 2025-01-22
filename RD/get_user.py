import json
import requests

with open("access_token.txt") as f:
    KEYCLOAK_ACCESS_TOKEN = f.read().strip()
KEYCLOAK_HOST = 'iam.karned.bzh'
KEYCLOAK_REALM  ='Karned'

username = 'killian'

users_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users"
headers = {
    "Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"
}

data = {
    "username": username
}

response = requests.get(users_url, headers=headers, params=data)
users = response.json()
print(f"Users: {users}")

for user in users:
    print(f"User: {user['id']} {user['username']}")

with open("users.json", "w") as f:
    json.dump(users, f)

import requests
import logging

with open("access_token.txt") as f:
    KEYCLOAK_ACCESS_TOKEN = f.read().strip()
KEYCLOAK_HOST = 'iam.karned.bzh'
KEYCLOAK_REALM  ='Karned'

#user_id = "9bad8cb9-fdb6-4da9-9454-862a87f92dba" # titi
user_id = "c66f3671-7e64-4017-b0e1-e848fcef5ddb" # tutu
new_password = "newpassword123"

headers = {
    "Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"
}
password_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users/{user_id}/reset-password"
data = {
    "type": "password",
    "value": new_password,
    "temporary": False
}

password_response = requests.put(password_url, headers=headers, json=data)
if password_response.status_code == 204:
    logging.info(f"Mot de passe mis à jour avec succès pour l'utilisateur '{user_id}'.")
else:
    logging.error(f"Erreur lors de la mise à jour du mot de passe : {password_response.status_code}, {password_response.text}")

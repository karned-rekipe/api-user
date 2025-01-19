import requests
import logging

with open("access_token.txt") as f:
    KEYCLOAK_ACCESS_TOKEN = f.read().strip()
KEYCLOAK_HOST = 'iam.karned.bzh'
KEYCLOAK_REALM  ='Karned'

# Étape 1 : Récupérer l'ID de l'utilisateur
def get_user_id(username):
    users_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users"
    headers = {"Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"}
    response = requests.get(users_url, headers=headers, params={"username": username})
    if response.status_code == 200 and response.json():
        return response.json()[0]["id"]
    else:
        logging.error(f"Erreur lors de la récupération de l'utilisateur : {response.status_code}, {response.text}")
        return None

# Étape 2 : Récupérer l'ID du groupe
def get_group_id(group_name):
    groups_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/groups"
    headers = {"Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"}
    response = requests.get(groups_url, headers=headers)
    if response.status_code == 200:
        for group in response.json():
            if group["name"] == group_name:
                return group["id"]
    logging.error(f"Groupe '{group_name}' non trouvé ou erreur API : {response.status_code}, {response.text}")
    return None

# Étape 3 : Ajouter l'utilisateur au groupe
def add_user_to_group(user_id, group_id):
    add_url =  f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users/{user_id}/groups/{group_id}"
    headers = {"Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"}
    response = requests.put(add_url, headers=headers)
    if response.status_code == 204:
        logging.info(f"Utilisateur ajouté au groupe avec succès.")
    else:
        logging.error(f"Erreur lors de l'ajout de l'utilisateur au groupe : {response.status_code}, {response.text}")

def remove_user_from_group(user_id, group_id):
    remove_url = f"https://{KEYCLOAK_HOST}/admin/realms/{KEYCLOAK_REALM}/users/{user_id}/groups/{group_id}"
    headers = {"Authorization": f"Bearer {KEYCLOAK_ACCESS_TOKEN}"}
    response = requests.delete(remove_url, headers=headers)
    if response.status_code == 204:
        logging.info(f"Utilisateur retiré du groupe avec succès.")
    else:
        logging.error(f"Erreur lors du retrait de l'utilisateur du groupe : {response.status_code}, {response.text}")


# Exemple d'utilisation
username = "toto"
group_name = "Karned-user"

user_id = get_user_id(username)
group_id = get_group_id(group_name)

if user_id and group_id:
    #add_user_to_group(user_id, group_id)
    remove_user_from_group(user_id, group_id)
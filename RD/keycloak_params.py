import os
import requests

KEYCLOAK_HOST = os.environ['KEYCLOAK_HOST']
KEYCLOAK_REALM = os.environ['KEYCLOAK_REALM']
KEYCLOAK_CLIENT_ID = os.environ['KEYCLOAK_CLIENT_ID']
KEYCLOAK_CLIENT_SECRET =os.environ['KEYCLOAK_CLIENT_SECRET']
KEYCLOAK_ADMIN_USER = os.environ['KEYCLOAK_ADMIN_USER']
KEYCLOAK_ADMIN_PASSWORD = os.environ['KEYCLOAK_ADMIN_PASSWORD']

print(f"Keycloak host: {KEYCLOAK_HOST}")
print(f"Keycloak realm: {KEYCLOAK_REALM}")
print(f"Keycloak client ID: {KEYCLOAK_CLIENT_ID}")
print(f"Keycloak client secret: {KEYCLOAK_CLIENT_SECRET}")
print(f"Keycloak admin user: {KEYCLOAK_ADMIN_USER}")
print(f"Keycloak admin password: {KEYCLOAK_ADMIN_PASSWORD}")
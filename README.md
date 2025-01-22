# user

les users seront des adresses emails et seront gérés par keycloak
la création se fait sur keycloak et l'uuid est utilisé dans mongodb pour compléter les informations
Les informations nécessaires à toutes les apps / apis seront dupliquées dans keycloak dans le but de les intégrer au token
les autres informations seront stockées dans mongodb
la base de données utilisateurs sera uniquement sur la base de données de Koden
la base de données personnes sera propre à chaque client

filtre des utilisateurs au niveau de mongodb car il n'est pas possible de le faire avec keycloak

le token valide la possibilité d'utiliser l'API mais la base de données est automatiquement désigné comme celle de Koden

il n'est pas possible de modifier un _id sur mongodb, il faut créer le user sur keycloak en premier

### user
- uuid (from keycloak)
- entities : array
- firstname
- lastname
- email

## person
- uuid
- firstname
- lastname
- email
- phone
- user_uuid

## routes
POST /
recherche sur keycloak d'un user avec l'identifiant 
si existant : utilisation par affectation de l'entity sur laquelle on se trouve
sinon : creation d'un user et affectation automatique de l'entity sur laquelle on se trouve
la création se fait sur keycloak, on lit ensuite le uuid afin de le créer sur mongodb

DELETE /
suppression de l'entity sur laquelle on se trouve
si pas d'autre entity alors suppression de keycloack
suppression de mongodb

POST /{uuid}/reset-password
modification du password sur keycloack limité à l'entity en cours) via un email
pb de sécurité ici : si plusieurs entité alors modifié le pass sur une entité revient à donner un accès 
sur les autres entités à la personne qui a fait la modification !!!
il faut que le reset passe par un mail envoyé sur la bal du user et ne pas proposer d'autre alternative

GET /{uuid}
retourne les informations de l'utilisateur (en limitant aux users de l'entity en cours)

GET /
retourne la liste des users en limitant à l'entity en cours
il s'agit d'une recherche qui sera faite sur mongodb, tous les champs sont "cherchables"


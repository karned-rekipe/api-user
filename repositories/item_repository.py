from typing import List
from uuid import uuid4

from pymongo import MongoClient

from interfaces.item_interface import ItemRepository
from models.item_model import Item
from schemas.item_schema import list_item_serial, item_serial


class ItemRepositoryMongo(ItemRepository):

    def __init__( self, url: str, name: str, collection: str ):
        self.url = url
        self.name = name
        self.collection = collection
        self.client = None
        self.db = None

    def __enter__( self ):
        self.client = MongoClient(self.url)
        self.db = self.client[self.name]
        return self

    def __exit__( self, exc_type, exc_val, exc_tb ):
        self.client.close()

    #Todo
    # gerer l'erreur si insert_one ne fonctionne pas
    # du coup inserted_id n'existe pa
    def create_item(self, item_create: Item) -> str:
        item_data = item_create.model_dump()
        item_data["_id"] = str(uuid4())
        new_item_id = self.db[self.collection].insert_one(item_data)
        return new_item_id.inserted_id

    def get_item(self, item_id: int) -> dict:
        result = self.db[self.collection].find_one({"_id": item_id})
        item = item_serial(result)
        return item

    def list_items(self) -> List[dict]:
        result = self.db[self.collection].find()
        items = list_item_serial(result)
        return items

    def update_item(self, item_id: str, item_update: Item) -> None:
        update_data = {"$set": item_update.model_dump()}
        self.db[self.collection].find_one_and_update({"_id": item_id}, update_data)

    def delete_item(self, item_id: str) -> None:
        self.db[self.collection].delete_one({"id": item_id})

    def close(self):
        self.client.close()
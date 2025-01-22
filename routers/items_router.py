from fastapi import APIRouter, HTTPException, status, Depends, Request
from config.config import API_TAG_NAME
from decorators.check_permission import check_permissions
from models.item_model import Item
from services.items_service import create_item, get_items, get_item, update_item, delete_item


router = APIRouter(
    tags=[API_TAG_NAME]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
@check_permissions(['create'])
async def create_new_item(request: Request, item: Item) -> dict:
    return {"return": 'TODO'}


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[Item])
@check_permissions(['read', 'read_own'])
async def read_items(request: Request):

    return {"return": 'TODO'}


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=Item)
@check_permissions(['list', 'list_own'])
async def read_item(request: Request, item_id: str):


    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions(['delete', 'delete_own'])
async def delete_existing_item(request: Request, item_id: str):
    repo = request.state.repo
    delete_item(item_id, repo)

@router.post("/{uuid}/reset-password", status_code=status.HTTP_201_CREATED)
@check_permissions(['update'])
async def reset_password(request: Request, item: Item) -> dict:
    return {"return": 'TODO'}
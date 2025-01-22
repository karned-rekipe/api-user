from typing import Optional
from pydantic.v1 import validator
from pydantic import BaseModel, Field

class Item(BaseModel):
    uuid: str = Field(None, description="User : UUID")
    username: str = Field(None, description="User : username")
    firstname: Optional[str] = Field(None, description="User : firstname")
    lastname: Optional[str] = Field(None, description="User : lastname")
    email: str = Field(None, description="User : email")
    created_by: Optional[str] = Field(None, description="User who created this step")

class UserFilter(BaseModel):
    uuid: Optional[str] = Field(None, description="User : UUID")
    username: Optional[str] = Field(None, description="User : username")
    firstname: Optional[str] = Field(None, description="User : firstname")
    lastname: Optional[str] = Field(None, description="User : lastname")
    created_by: Optional[str] = Field(None, description="User who created this step")

    class Config:
        extra = "forbid"

    """
    TODO : chercher une solution pour cette partie. L'idée est de récupérer dans le state l'uuid de l'entity
    @validator("entity", pre=True)
    def set_entity_from_token(self):
        if request.state.token_info:
            return token["desired_value"]
        else:
            return None
    """



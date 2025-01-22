from typing import Optional
from pydantic.v1 import validator
from pydantic import BaseModel, Field


class Item(BaseModel):
    uuid: str = Field(None, description="User : UUID")
    username: str = Field(None, description="User : username")
    firstname: Optional[str] = Field(None, description="User : firstname")
    lastname: Optional[str] = Field(None, description="User : lastname")
    email: str = Field(None, description="User : email")

class UserFilter(BaseModel):
    uuid: Optional[str] = Field(None, description="User : UUID")
    username: Optional[str] = Field(None, description="User : username")
    firstname: Optional[str] = Field(None, description="User : firstname")
    lastname: Optional[str] = Field(None, description="User : lastname")
    created_by: Optional[str] = Field(None, description="User who created this step")

    class Config:
        extra = "forbid"

    @validator("entity", pre=True)
    def set_entity_from_token(self):
        if "desired_value" in token:
            return token["desired_value"]
        else:
            return None



from pydantic import BaseModel
from pydantic import field_serializer
from pydantic import Field
from typing import Union
from uuid import UUID

class Pokemon(BaseModel):
    id: UUID
    name: str
    attack: int = Field(..., gt=0 , le=100, description="This Attack must be in between 1 and 100")
    defense: int = Field(..., gt=0 , le=100, description="This Defense must be in between 1 and 100")
    speed: int = Field(..., gt=0 , le=100, description="This Speed must be in between 1 and 100")
    hp: int = Field(..., gt=0 , le=100, description="This Life must be in between 1 and 100")
    image: str
    element: str

    @field_serializer('id')
    def serialize_id(self, id: UUID):
        return str(id)
from pydantic import BaseModel
from pydantic import PositiveInt
from pydantic import field_serializer
from typing import Union
from uuid import UUID

class Pokemon(BaseModel):
    id: Union[UUID, None] = None
    name: str
    attack: PositiveInt
    defense: PositiveInt
    speed: PositiveInt
    life: PositiveInt
    image: str

    @field_serializer('id')
    def serialize_id(self, id: UUID):
        return str(id)
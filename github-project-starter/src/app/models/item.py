from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    title: str = Field(..., example="Sample Item")
    description: Optional[str] = Field(None, example="Detailed description of the item")
    price: float = Field(..., gt=0, example=29.99)

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int = Field(..., example=1)

    class Config:
        from_attributes = True

from fastapi import APIRouter, HTTPException, status
from typing import List
from src.app.models.item import Item, ItemCreate

router = APIRouter()

# In-memory mock database
db_items = [
    {"id": 1, "title": "Developer Laptop", "description": "High performance workstation", "price": 1999.99},
    {"id": 2, "title": "Mechanical Keyboard", "description": "RGB Tactile switch keyboard", "price": 129.50},
]

@router.get("", response_model=List[Item])
def get_items():
    return db_items

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    new_id = len(db_items) + 1
    new_item = {"id": new_id, **item.model_dump()}
    db_items.append(new_item)
    return new_item

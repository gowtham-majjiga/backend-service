from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import ItemCreate, ItemRead
from .services import ItemService

router = APIRouter(prefix="/api/v1/items", tags=["items"])
service = ItemService()

@router.get("", response_model=list[ItemRead])
def list_items(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), q: str | None = None, db: Session = Depends(get_db)):
    return service.list_items(db, offset, limit, q)

@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    return service.create_item(db, payload)

@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return service.get_item(db, item_id)

@router.patch("/{item_id}", response_model=ItemRead)
def update_item(item_id: int, payload: ItemCreate, db: Session = Depends(get_db)):
    return service.update_item(db, item_id, payload)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    service.delete_item(db, item_id)

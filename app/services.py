from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .repositories import ItemRepository
from .schemas import ItemCreate

class ItemService:
    def __init__(self, repo: ItemRepository | None = None):
        self.repo = repo or ItemRepository()

    def list_items(self, db: Session, offset: int, limit: int, q: str | None):
        return self.repo.list(db, offset=offset, limit=limit, q=q)

    def get_item(self, db: Session, item_id: int):
        item = self.repo.get(db, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return item

    def create_item(self, db: Session, payload: ItemCreate):
        return self.repo.create(db, payload)

    def update_item(self, db: Session, item_id: int, payload: ItemCreate):
        item = self.get_item(db, item_id)
        return self.repo.update(db, item, payload)

    def delete_item(self, db: Session, item_id: int):
        item = self.get_item(db, item_id)
        self.repo.delete(db, item)

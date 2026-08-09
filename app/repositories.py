from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Item
from .schemas import ItemCreate

class ItemRepository:
    def list(self, db: Session, *, offset: int = 0, limit: int = 20, q: str | None = None):
        stmt = select(Item).offset(offset).limit(limit)
        if q:
            stmt = select(Item).where(Item.name.ilike(f"%{q}%")).offset(offset).limit(limit)
        return list(db.scalars(stmt).all())

    def get(self, db: Session, item_id: int):
        return db.get(Item, item_id)

    def create(self, db: Session, payload: ItemCreate):
        item = Item(**payload.model_dump())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def update(self, db: Session, item: Item, payload: ItemCreate):
        item.name = payload.name
        item.description = payload.description
        db.commit()
        db.refresh(item)
        return item

    def delete(self, db: Session, item: Item):
        db.delete(item)
        db.commit()

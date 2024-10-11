import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select, SQLModel
from db import get_session
from models.wrestlers import Wrestler
from models.championships import Championship
from models.merchandise_sales import Merchandise_Sales

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WWE Wrestlers"}


def create_generic(model):
    def create(item: model, session: Session = Depends(get_session)):
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return create

def read_generic(model):
    def read(item_id: int, session: Session = Depends(get_session)):
        return session.get(model, item_id)
    return read

def update_generic(model):
    def update(item_id: int, item: model, session: Session = Depends(get_session)):
        db_item = session.get(model, item_id)
        if db_item:
            item_data = item.model_dump(exclude_unset=True)
            for key, value in item_data.items():
                setattr(db_item, key, value)
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item
        return {"error": f"{model.__name__} with id {item_id} not found"}
    return update

def delete_generic(model):
    def delete(item_id: int, session: Session = Depends(get_session)):
        item = session.get(model, item_id)
        if item:
            session.delete(item)
            session.commit()
        return {"ok": True}
    return delete

# CRUD operations for Wrestler
create_wrestler = create_generic(Wrestler)
read_wrestler = read_generic(Wrestler)
update_wrestler = update_generic(Wrestler)
delete_wrestler = delete_generic(Wrestler)

# CRUD operations for Championship
create_championship = create_generic(Championship)
read_championship = read_generic(Championship)
update_championship = update_generic(Championship)
delete_championship = delete_generic(Championship)

# CRUD operations for Merchandise_Sales
create_merchandise_sale = create_generic(Merchandise_Sales)
read_merchandise_sale = read_generic(Merchandise_Sales)
update_merchandise_sale = update_generic(Merchandise_Sales)
delete_merchandise_sale = delete_generic(Merchandise_Sales)
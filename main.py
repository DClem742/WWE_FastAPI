import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, SQLModel
from db import get_session
from models.wrestlers import Wrestler
from models.championships import Championship
from models.merchandise_sales import Merchandise_Sale

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
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
app.post("/wrestlers/")(create_generic(Wrestler))
# app.get("/wrestlers/{item_id}")(read_generic(Wrestler))
app.put("/wrestlers/{item_id}")(update_generic(Wrestler))
app.delete("/wrestlers/{item_id}")(delete_generic(Wrestler))

# CRUD operations for Championship
app.post("/championships/")(create_generic(Championship))
app.get("/championships/{item_id}")(read_generic(Championship))
app.put("/championships/{item_id}")(update_generic(Championship))
app.delete("/championships/{item_id}")(delete_generic(Championship))

# CRUD operations for Merchandise_Sales
app.post("/merchandise_sales/")(create_generic(Merchandise_Sale))
app.get("/merchandise_sales/{item_id}")(read_generic(Merchandise_Sale))
app.put("/merchandise_sales/{item_id}")(update_generic(Merchandise_Sale))
app.delete("/merchandise_sales/{item_id}")(delete_generic(Merchandise_Sale))

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


@app.get("/wrestlers/name/{wrestler_name}")
def get_wrestler_by_name(wrestler_name: str, session: Session = Depends(get_session)):
    wrestler = session.exec(select(Wrestler).where(Wrestler.name == wrestler_name)).first()
    if wrestler:
        championships = session.exec(select(Championship).where(
            (Championship.current_champion_id1 == wrestler.id) | 
            (Championship.current_champion_id2 == wrestler.id)
        )).all()
        
        return {
            "wrestler": wrestler,
            "championships": [champ.title_name for champ in championships]
        }
    return {"error": f"Wrestler with name {wrestler_name} not found"}

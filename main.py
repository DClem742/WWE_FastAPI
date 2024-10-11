import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, SQLModel, select
from models.wrestlers import Wrestler
from models.championships import Championship
from models.merchandise_sales import Merchandise_Sale
from db import get_session

app = FastAPI()

# Dependency
def get_db():
    return next(get_session())

# Wrestlers CRUD
@app.post("/wrestlers/")
def create_wrestler(wrestler: Wrestler, db: Session = Depends(get_db)):
    db.add(wrestler)
    db.commit()
    db.refresh(wrestler)
    return wrestler

@app.get("/wrestlers/{wrestler_id}")
def read_wrestler(wrestler_id: int, db: Session = Depends(get_db)):
    statement = select(Wrestler).where(Wrestler.id == wrestler_id)
    result = db.exec(statement).first()
    if not result:
        raise HTTPException(status_code=404, detail="Wrestler not found")
    return result
@app.put("/wrestlers/{wrestler_id}")
def update_wrestler(wrestler_id: int, updated_wrestler: Wrestler, db: Session = Depends(get_db)):
    statement = select(Wrestler).where(Wrestler.id == wrestler_id)
    result = db.exec(statement).first()
    if not result:
        raise HTTPException(status_code=404, detail="Wrestler not found")
    return result
    wrestler_data = updated_wrestler.dict(exclude_unset=True)
    for key, value in wrestler_data.items():
        setattr(wrestler, key, value)
    db.add(wrestler)
    db.commit()
    db.refresh(wrestler)
    return wrestler

@app.delete("/wrestlers/{wrestler_id}")
def delete_wrestler(wrestler_id: int, db: Session = Depends(get_db)):
    statement = select(Wrestler).where(Wrestler.id == wrestler_id)
    wrestler = db.exec(statement).first()
    if not wrestler:
        raise HTTPException(status_code=404, detail="Wrestler not found")
    db.delete(wrestler)
    db.commit()
    return {"message": "Wrestler deleted successfully"}
    db.commit()
    return {"message": "Wrestler deleted successfully"}

# Championships CRUD
@app.post("/championships/")
def create_championship(championship: Championship, db: Session = Depends(get_db)):
    db.add(championship)
    db.commit()
    db.refresh(championship)
    return championship

@app.get("/championships/{championship_id}")
def read_championship(championship_id: int, db: Session = Depends(get_db)):
    championship = db.get(Championship, championship_id)
    if not championship:
        raise HTTPException(status_code=404, detail="Championship not found")
    return championship

@app.put("/championships/{championship_id}")
def update_championship(championship_id: int, updated_championship: Championship, db: Session = Depends(get_db)):
    championship = db.get(Championship, championship_id)
    if not championship:
        raise HTTPException(status_code=404, detail="Championship not found")
    championship_data = updated_championship.dict(exclude_unset=True)
    for key, value in championship_data.items():
        setattr(championship, key, value)
    db.add(championship)
    db.commit()
    db.refresh(championship)
    return championship

@app.delete("/championships/{championship_id}")
def delete_championship(championship_id: int, db: Session = Depends(get_db)):
    championship = db.get(Championship, championship_id)
    if not championship:
        raise HTTPException(status_code=404, detail="Championship not found")
    db.delete(championship)
    db.commit()
    return {"message": "Championship deleted successfully"}

# Merchandise Sales CRUD
@app.post("/merchandise-sales/")
def create_merchandise_sale(merchandise_sale: Merchandise_Sale, db: Session = Depends(get_db)):
    db.add(merchandise_sale)
    db.commit()
    db.refresh(merchandise_sale)
    return merchandise_sale

@app.get("/merchandise-sales/{sale_id}")
def read_merchandise_sale(sale_id: int, db: Session = Depends(get_db)):
    merchandise_sale = db.get(Merchandise_Sale, sale_id)
    if not merchandise_sale:
        raise HTTPException(status_code=404, detail="Merchandise sale not found")
    return merchandise_sale

@app.put("/merchandise-sales/{sale_id}")
def update_merchandise_sale(sale_id: int, updated_sale: Merchandise_Sale, db: Session = Depends(get_db)):
    merchandise_sale = db.get(Merchandise_Sale, sale_id)
    if not merchandise_sale:
        raise HTTPException(status_code=404, detail="Merchandise sale not found")
    sale_data = updated_sale.dict(exclude_unset=True)
    for key, value in sale_data.items():
        setattr(merchandise_sale, key, value)
    db.add(merchandise_sale)
    db.commit()
    db.refresh(merchandise_sale)
    return merchandise_sale

@app.delete("/merchandise-sales/{sale_id}")
def delete_merchandise_sale(sale_id: int, db: Session = Depends(get_db)):
    merchandise_sale = db.get(Merchandise_Sale, sale_id)
    if not merchandise_sale:
        raise HTTPException(status_code=404, detail="Merchandise sale not found")
    db.delete(merchandise_sale)
    db.commit()
    return {"message": "Merchandise sale deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
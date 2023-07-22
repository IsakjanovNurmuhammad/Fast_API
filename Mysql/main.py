from fastapi import FastAPI, Depends

from schemas import MsgSchema
from models import MsgModel
from db import session_local
from sqlalchemy.orm import Session


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/hello")
async def hello(name: str):
    return name


@app.post("/create/msg")
async def create_msg(schema: MsgSchema,
                     db: Session = Depends(get_db)):
    model = MsgModel()
    model.id = schema.id
    model.msg = schema.msg

    db.add(model)
    db.commit()

    return model


@app.get("/get")
async def get_db(db: Session = Depends(get_db)):
    query = db.query(MsgModel).all()

    return query


@app.put("/update/msg")
async def create_msg(id: int
                     , schema: MsgSchema,
                     db: Session = Depends(get_db)):
    print("-----------------------------------------------------",db)

    model = db.query(MsgModel).filter(MsgModel.id == id).first()

    if model is None:
        return "Is none"

    model.id = schema.id
    model.msg = schema.msg

    db.add(model)
    db.commit()

    return model

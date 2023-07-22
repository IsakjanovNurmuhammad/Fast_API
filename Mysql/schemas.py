from pydantic import BaseModel


class MsgSchema(BaseModel):
    id: int
    msg: str

from pydantic import BaseModel

class Checkbox(BaseModel):
    id: int
    checked: bool = False

    class Config:
        orm_mode = True


from pydantic import BaseModel, Field , EmailStr
from typing import Optional

class Usercreate(BaseModel):
    name : str
    age : int = Field(ge=18)
    email : EmailStr
    password : str = Field(min_length=8)

    class config():
        orm_mode = True


class Userresponse(BaseModel):
    name : str
    age  : int
    email: str
    id   : int

    class config():
        orm_mode = True

class Userupdate(BaseModel):
    name : Optional[str] | None
    age  : Optional[int] | None
    password : Optional[str] | None

    class config():
        orm_mode = True


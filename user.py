
from multiprocessing import synchronize

from fastapi import APIRouter , status , Depends , HTTPException
from schema import Usercreate , Userresponse , Userupdate
from database import sessionlocal
from sqlalchemy.orm import session
from model import User

user_route = APIRouter()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
    
@user_route.post("/user_login",response_model=Userresponse , status_code=status.HTTP_201_CREATED)
def user_post(user : Usercreate, db : session = Depends(get_db)):
    existing = db.query(User).filter(user.email == User.email).first()
    if existing:
        raise HTTPException(status_code=400 , detail=f"user on {user.email} already exist")
    new_entry = User(name = user.name , email = user.email , age = user.age ,password = user.password)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@user_route.get("/user-info/{id}",response_model=Userresponse ,status_code=status.HTTP_200_OK)
def user_info(id : int , db :session =Depends(get_db)):
    existing = db.query(User).filter(User.id == id).first()
    if not existing:
        raise HTTPException(status_code=400 , detail="no user exist for this id")
    return existing
@user_route.delete("/user-delete/{id}")
def user_delete(id : int , db :session = Depends(get_db)):
    existing = db.query(User).filter(User.id == id)
    if not existing:
        raise HTTPException(status_code=400 , detail="no user present to delete")
    existing.delete(synchronize_session = False)
    db.commit()
    return {"message":"user is deleted from database"}
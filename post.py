from multiprocessing import synchronize
from fastapi import APIRouter , status , Depends , HTTPException
from schema import Usercreate , Userresponse , Userupdate
from database import sessionlocal
from sqlalchemy.orm import session
from model import User

post_route = APIRouter()


from fastapi import FastAPI
from database import engine , Base
from route.user import user_route

app = FastAPI()
app.include_router(user_route)

Base.metadata.create_all(engine)

@app.get("/")
def start():
    return {"message":"this is the main route"}
# FASTAPI
# https://towardsdatascience.com/you-should-start-using-fastapi-now-7efb280fec02
# pip install fastapi

from fastapi import FastAPI
from pydantic import BaseModel  # data validation

class User(BaseModel):
    email: str
    password: str

app = FastAPI()

@app.post("/login")
def login(user: User):
    # ...
    # do some magic
    # ...
    return {"msg": "login successful"}

print('Listening...')

# To run, serve with uvicorn: uvicorn main:app
# https://www.uvicorn.org/
# curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"

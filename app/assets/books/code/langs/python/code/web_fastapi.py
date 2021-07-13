# FAST API 

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
# curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"







# >pip3 install fastapi
# pip3 install uvicorn
# pip3 install pydantic

app = FastAPI(
    title = "Logging API",
    description = "An API for all your logging needs.",
    version = "2.0",
)

@app.get("/loggingapi/v2/logs/{appId}")
async def Logs(appId: str):
    results = storage.GetLogs(appId)
    return results    

GET request — /loggingapi/v1/logs
 
POST request — /loggingapi/v1/log    
{
     "appId": "7542a72b-b6eb-4b9d-a672-a8d82ad0dadf",
     "message": "This is my log message."
} 


# ML API: https://www.youtube.com/watch?v=La1HAYI1j30&t=1s

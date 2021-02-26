## fastapi

FastAPI framework for all my Python APIs
Asynchronous tasks are integrated by default. Flask does have support for asynchronous tasks, but the “celery” module needs to be imported. Same thing when it comes to sending responses in Flask (“json” module is needed). FastAPI by default sends responses as JSON objects. Finally, the swagger documentation is amazing! 

>pip3 install fastapi
pip3 install uvicorn
pip3 install pydantic

```python
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
     "appId": 7542a72b-b6eb-4b9d-a672-a8d82ad0dadf
     "message": "This is my log message."
}    
```
    

### More
- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062
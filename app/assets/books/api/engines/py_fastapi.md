## FASTAPI

Fast (high-performance) web framework to build APIs on Python >= 3.6+ based on standard Python type hints.
Every developer in my network has shifted to FastApi from Django and Flask. 
It is a lot easier to learn and quick to implement. The performance is as par with Golang and Node. 

Asynchronous tasks are integrated by default. Flask does have support for asynchronous tasks, but the “celery” module needs 
to be imported. Same thing when it comes to sending responses in Flask (“json” module is needed). FastAPI by 
default sends responses as JSON objects. Finally, the swagger documentation is amazing! 

To gathering web-based data, especially from APIs.   
Requests makes it easy to interact with APIs and other HTML sources in simple, one-line solutions.

Similar to the Flask app structure. You need to create endpoints where our client service can make requests and obtain the required data.

>pip install fastapi

```py
import uvicorn   # Uvicorn is used for implementing the server and handling all the calls in Python
from fastapi import FastAPI

app = FastAPI()  # FastAPI app instance is created

@app.get('/')
def index():
    return {'message': "This is the home page of this API. Go to /apiv1/ or /apiv2/?name="}

# To Add routes/endpoints: route decorator + function
# Decorator registers the function for the route defined so that when that particular route is requested
# The function is called and its result is returned to the client. Generally, we return a JSON object so that it can be parsed in any language.
# To get the inputs from the client, you can use Path parameters, Query parameters, Request bodies. 
# you can define these routes directly for HTTP methods. In Flask, you need to manually add them to a list of methods
@app.get('/apiv1/{name}')    
def api1(name: str):
    return {'message': f'Hello! @{name}'}


@app.get('/apiv2/')   #  query-based, parameters passed by xxxxx?name=joe&age=20&...
def api2(name: str):
    return {'message': f'Hello! @{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)
```

### Request Body Approach
Pass the data from the client to our API
FastAPI simplify things with Pydantic models to define the data structure for the receiving data. The Pydantic does all the type checking for the parameters and returns explainable errors if the wrong type of parameter is received.

```py
# After other imports
from pydantic import BaseModel
class Details(BaseModel):  # model is inherited from the Pydantic base model and offers data validation
    f_name: str
    l_name: str
    phone_number: int
app = FastAPI()
...
# After old routes. create a route for the request body
@app.post('/apiv3/')
def api3(data: Details):      # route function declares a parameter "data" of the type "Details"
    return {'message': data}
```

download.code(assets/books/code/langs/python/code/web_fastapi.py)

### More
- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062
- https://github.com/tiangolo/fastapi
- https://towardsdatascience.com/you-should-start-using-fastapi-now-7efb280fec02
- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062
- https://www.analyticsvidhya.com/blog/2021/06/deploying-ml-models-as-api-using-fastapi-and-heroku
- https://realpython.com/python-requests/


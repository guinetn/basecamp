## ASGI

https://asgi.readthedocs.io/en/latest/

Asynchronous Server Gateway Interface
WSGI++ (WSGI provided a standard for synchronous Python apps)
Standard interface between async-capable Python web servers, frameworks, and applications.

ASGI is structured as a single, asynchronous callable. It takes 
- a scope
a dict containing details about the specific connection
- send
an asynchronous callable, that lets the application send event messages to the client
- receive
an asynchronous callable which lets the application receive event messages from the client.

This allows 
- multiple incoming events and outgoing events for each application
- background coroutine so the application can do other things (such as listening for events on an external trigger, like a Redis queue).

In its simplest form, an application can be written as an asynchronous function, like this:

```py
async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...})
```

Every event that you send or receive is a Python dict, with a predefined format. It’s these event formats that form the basis of the standard, and allow applications to be swappable between servers.
These events each have a defined type key, which can be used to infer the event’s structure. 

example event that you might receive from receive with the body from a HTTP request:
{
    "type": "http.request",
    "body": b"Hello World",
    "more_body": False,
}

example of an event you might pass to send to send an outgoing WebSocket message:
{
    "type": "websocket.send",
    "text": "Hello world!",
}

## Servers Implementations

* Uvicorn
https://www.uvicorn.org/

A fast ASGI server based on uvloop and httptools. Supports HTTP/1 and WebSockets.

* Hypercorn
https://pgjones.gitlab.io/hypercorn/index.html
An ASGI server based on the sans-io hyper, h11, h2, and wsproto libraries. Supports HTTP/1, HTTP/2, and WebSockets.

## applications Implementations

* Django/Channels
http://channels.readthedocs.io
Channels is the Django project to add asynchronous support to Django and is the original driving force behind the ASGI project. Supports HTTP and WebSockets with Django integration, and any protocol with ASGI-native code.

* FastAPI
https://github.com/tiangolo/fastapi
FastAPI is an ASGI web framework (made with Starlette) for building web APIs based on standard Python type annotations and standards like OpenAPI, JSON Schema, and OAuth2. Supports HTTP and WebSockets.

* Quart
https://github.com/pgjones/quart
Quart is a Python ASGI web microframework. It is intended to provide the easiest way to use asyncio functionality in a web context, especially with existing Flask apps. Supports HTTP.

* Starlette
https://github.com/encode/starlette
Starlette is a minimalist ASGI library for writing against basic but powerful Request and Response classes. Supports HTTP.

* rpc.py
https://github.com/abersheeran/rpc.py
An easy-to-use and powerful RPC framework. RPC server base on WSGI & ASGI, client base on httpx. Supports synchronous functions, asynchronous functions, synchronous generator functions, and asynchronous generator functions. Optional use of Type hint for type conversion. Optional OpenAPI document generation.
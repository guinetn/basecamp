# REST - REpresentational State Transfer

Underlying protocol: REST uses HTTP/HTTPS
Stateless
Response can be cached (GET requests)
No limits and contracts, light weight comparing to SOAP.
REST is easier than SOAP

## RESTful APi

Provide Web resources in a textual representation and allow them to be read and modified with a stateless protocol and a predefined set of operations:

HTTP is the Common protocol for these requests and responses. It provides operations (HTTP methods) GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE


Web service APIs that adhere to the REST architectural constraints are called RESTful APIs. HTTP-based RESTful APIs are defined with the following aspects:
- a base URI, such as http://api.example.com/;
- standard HTTP methods (e.g., GET, POST, PUT, and DELETE);
- a media type that defines state transition data elements (e.g., Atom, microformats, application/vnd.collection+json). 

A Web service that follows this standard is called 'RESTful'
Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON...

Using a stateless protocol and standard operations, RESTful systems aim for fast performance, reliability, and the ability to grow by reusing components that can be managed and updated without affecting the system as a whole, even while it is running.

## Http verbs

|HTTP VERBS||
|---|---|
| GET    | ​/api​/v2​/articles |
| GET    | ​/api​/v2​/articles​/{id} |
| GET    | ​/api​/v2​/articles​/launch​/{id}|
| POST   | ​/api​/v2​/articles |
| PUT    | ​/api​/v2​/articles​/{id} |
| PATCH  | ​/api​/v2​/articles​/{id} |
| DELETE | ​/api​/v2​/articles​/{id} |
| OPTIONS|  |

## HTTP STATUS CODES
<div>
<div>100 <br\> <span>In progress</span></div> 		
<div>200 <br\> <span>OK</span></div> 		
<div>300 <br\> <span>Redirect</span></div> 		
<div>400 <br\> <span>Client Error</span></div> 		
<div>500 <br\> <span>Server Error</span></div> 		
</div>
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

Singular routes     /profile
Plural routes       /posts   /posts/1
Filter
- /posts?id=1&id=2
- /comments?author.name=typicode
Paginate
    GET /posts?_page=7
    GET /posts?_page=7&_limit=20

Sort + _sort, _order
GET /posts?_sort=views&_order=asc
GET /posts/1/comments?_sort=votes&_order=asc
GET /posts?_sort=user,views&_order=desc,asc

Slice + _start and _end, _limit
GET /posts?_start=20&_end=30
GET /posts/1/comments?_start=20&_end=30
GET /posts/1/comments?_start=20&_limit=10


Operators
Add _gte or _lte for getting a range

GET /posts?views_gte=10&views_lte=20
Add _ne to exclude a value

GET /posts?id_ne=1
Add _like to filter (RegExp supported)

GET /posts?title_like=server
Full-text search
Add q

GET /posts?q=internet
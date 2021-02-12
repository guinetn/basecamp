# API

/api/v1
X-MyGreatApi-Token : apiKey
Rate Limits: 30... API calls/second. Else Status Code 429


- https://github.com/public-apis/public-apis
- https://public-apis.io/

- https://developer.spotify.com/
- https://developers.google.com/youtube/v3
- https://developer.twitter.com/en/docs/twitter-api
- https://www.twilio.com/docs/sms/send-messages
- https://cloud.google.com/maps-platform
- https://www.edamam.com/ (nutrition, food, recipes)
- https://stripe.com/docs/api

- https://finnhub.io/ retrieve data from the stock market
- https://www.exchangerate-api.com/
- https://www.coindesk.com/coindesk-api
- https://github.com/1Forge/javascript-forex-quotes

- https://hoppscotch.io/
- https://pokeapi.co/
- https://api.nasa.gov/
- https://spaceflightnewsapi.net/

* Fake api
- https://jsonplaceholder.typicode.com/
```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
  
async function fetchData() {
 const result = await fetch('http://reqres.in/api/users/2')
 const jsonResult = await result.json()
 console.log(jsonResult.first_name) // Lucille
}
```

* SEND GET REQUEST
Any properties that may have spaces or special characters in them should be passed into the encodeURIComponent() to encode it.

```html
<form id="post">
	<label for="title">Title</label>
	<input type="text" name="title" id="title" value="Go to the beach">  
```

```js
// Get the form data
let form = document.querySelector('form');
let data = new FormData(form);

// Submit the form data
fetch('https://jsonplaceholder.typicode.com/posts', {
	method: 'POST',
	body: new URLSearchParams(data).toString(),
	headers: {
		'Content-type': 'application/x-www-form-urlencoded'
	}
}).then(function (response) {
	if (response.ok) {
		return response.json();
	}
	throw response;
}).then(function (data) {
	console.log(data);
}).catch(function (error) {
	console.warn(error);
});
```

* SEND POST REQUEST
```js

function serialize (data) {
  // Serialize form data into an object
	let obj = {};
	for (let [key, value] of data) {
		if (obj[key] !== undefined) {
			if (!Array.isArray(obj[key])) {
				obj[key] = [obj[key]];
			}
			obj[key].push(value);
		} else {
			obj[key] = value;
		}
	}
	return obj;
}

// Get the form data
let form = document.querySelector('form');
let data = new FormData(form);

// Submit to the API
fetch('https://jsonplaceholder.typicode.com/posts', {
	method: 'POST',
	body: JSON.stringify(serialize(data)),
	headers: {
		'Content-type': 'application/json; charset=UTF-8'
	}
}).then(function (response) {
	if (response.ok) {
		return response.json();
	}
	throw response;
}).then(function (data) {
	console.log(data);
}).catch(function (error) {
	console.warn(error);
});
```

::::
## Request Pipeline

Add middlewares
hello.js
module.exports = (req, res, next) => {
  res.header('X-Hello', 'World')
  next()
}

::::
download.page(api/architecture/_architecture.md)
::::
download.page(api/rest.md)
  
download.page(api/soap.md)
::::   
download.page(api/graphql.md)
::::   
download.page(api/json.md)
::::
download.page(api/jsonp.md)
::::
download.page(api/grpc.md)
::::
download.page(api/performances.md)
::::
download.page(api/cors.md)
::::   
download.page(api/engines/_engines.md)
::::
download.page(api/open_api.md)
::::
download.page(api/health_check.md)
::::
download.page(api/testing/_testing.md)
::::
download.page(api/webhooks.md)
::::

[ways of Communication](https://michaelscodingspot.com/rest-vs-grpc-for-asp-net/)

[gRPC](https://grpc.io/)(gRPC Remote Procedure Call) is an open-source remote procedure call system developed by Google. It’s a bit like REST in the way that it provides a way to send requests from a client to a server. But it’s different in many ways

[GraphQL](https://graphql.org/) is a query language for APIs developed by Facebook. It allows the client to ask for exactly the data it needs from the server. This way, you can create just one endpoint on the server that will be extremely flexible and return only the data the client needs. GraphQL is becoming very popular in recent years.

[SignalR](https://github.com/SignalR/SignalR) is a technology that allows for real-time bi-directional communication between server and client. Instead of the client always sending requests to server, SignalR also allows the server to send push notifications to the client. This allows to see real-time updates in web applications. SignalR is extremely popular in ASP.NET.

[TcpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.tcpclient?view=netframework-4.8) and TcpListener (in System.Net.Sockets) provide a low-level connection over TCP. Basically, you’re going to establish a connection and transfer byte arrays. It’s not ideal for a big application where you can use ASP.NET’s controllers and actions to make order in a big API.

[UdpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.udpclient?view=netframework-4.8) provides a way to communicate over UDP protocol. TCP establishes a connection and then sends data, whereas UDP just sends data. TCP makes sure there are no errors in the data, whereas UDP doesn’t. UDP is more effective to transfer data quickly that you don’t care enough for it to be reliable and error-free. Some examples are: Video streaming, Live broadcasts, and Voice over IP (VoIP).

[WCF](https://docs.microsoft.com/en-us/dotnet/framework/wcf/whats-wcf) is an older technology that mostly uses SOAP-based communication between processes. It’s a huge framework that I’m not going to get into except to say that it lost its popularity to REST and JSON payloads.

## More

URL shortening service like bit.ly or goo.gl
- https://github.com/abhinavdhasmana/tinyUrl
- https://medium.com/@adhasmana/system-design-create-a-url-shortening-service-part-1-overview-26aae5597914
- https://github.com/abhinavdhasmana/ratelimiter
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://auth0.com/blog/how-to-build-and-secure-web-apis-with-aspnet-core-3/
- https://www.tutorialsteacher.com/webapi/consuming-web-api-in-dotnet-using-httpclient
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5


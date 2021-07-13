# Hapi

http://hapijs.com

Router And Templating Engine For Node
A rich framework for building applications and services
hapi enables developers to focus on writing reusable application logic instead of spending time building infrastructure.

Framework for building web services in Node.js. Hapi.js extracts input validation out of controllers into the intermediate layer between router and route handlers. Hapi is very modular and its schema validation component is a separate library called Joi.
https://medium.com/warsawjs/an-elegant-solution-for-handling-errors-in-express-27332f768c6

# Authentication
# Caching
# Cookies
# Getting Started
# Logging
# Plugins
# Routing
# Server Methods
# Serving Static Content
# Validation
# Views

# Node.js has 2 REST frameworks
*http://expressjs.com
*http://hapijs.com


npm init						Generate package.json
npm install hapi --save			Install hapi and save it to your package.json dependencies:

# Create aserver.js file with the following contents:

'use strict';
const Hapi = require('hapi');

// Create a server with a host and port
const server = new Hapi.Server();
server.connection({ 
    host: 'localhost', 
    port: 8000 
});

// Add the route
server.route({
    method: 'GET',
    path:'/hello', 
    handler: function (request, reply) {

        return reply('hello world');
    }
});

npm start 
open localhost:8000/hello


most basic server looks like the following:
# When adding the server connection, we can also provide a hostname, IP address, or even a 
# Unix socket file, or Windows named pipe to bind the server to. For more details, see the API reference.http://hapijs.com/api/#serverconnectionoptions

'use strict';
const Hapi = require('hapi');
const server = new Hapi.Server();
server.connection({ port: 3000 });

server.start((err) => {

    if (err) {
        throw err;
    }
    console.log('Server running at:', server.info.uri);
});



# Adding routes

server.route({
    method: 'GET',
    path: '/',
    handler: function (request, reply) {
        reply('Hello, world!');
    }
});

server.route({
    method: 'GET',
    path: '/{name}',
    handler: function (request, reply) {
        reply('Hello, ' + encodeURIComponent(request.params.name) + '!');
    }
});

http://localhost:3000/stimpy 		→ 	Hello, stimpy!
URI encode the name parameter, this is to prevent content injection attacks. 
Remember, it's never a good idea to render user provided data without output encoding it first!




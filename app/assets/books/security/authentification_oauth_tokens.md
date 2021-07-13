## OAuth

For all web apps that expose APIs to other web apps


- Delegated AUTHORIZATION framework for REST/APIs: approve one app interacting with another on your behalf without giving away your password. 
    - Identity Providers Supported by Auth0
        - Social Identity Providers
        - Enterprise Identity Providers
        - Legal Identity Providers
    - Database and Custom Connections    
        create your own user store, instead of using external identity providers like Google or Facebook, you can use a Database Connection. This way you can authenticate users with an email or username and a password. The credentials can be securely stored either in the Auth0 user store or in your own database.
    - Passwordless
        Passwordless connections allow users to log in without the need to remember a password. Instead, users enter their mobile phone number or email address and receive a one-time code or link, which they can then use to log in.    
- HTTP-based protocol 
- Enables an application or service to obtain limited access to a protected HTTP resource. Decouples authentication from authorization
- Doesn't share password data 
- Uses authorization tokens to prove an identity between consumers and service providers

- OAuth isn't authentication: access tokens are not intended for the client application. When an authorization server issues an access token, the intended audience is the protected resource. ... It's down to the protected resource to understand and validate the token.


http://auth0.com/
plate-forme d'authentification et d'autorisation
free with up to 7,000 active users and unlimited logins. No credit card required.
https://auth0.com/docs/quickstarts/  ★ ★ ★ 
https://auth0.com/docs/quickstart/spa/vanillajs  ★ ★ ★ 



https://oauth.net/
https://oauth.net/2
industry-standard protocol for authorization

https://medium.com/pragmatic-programmers/understanding-security-basics-1c2b1d5371d8

OAuth is a set of standards focused on authorization. OpenID is a set of standards focused on authentication. OpenID Connect is the identity layer built on top of the OAuth access control specification
 
OAuth (authentication and authorization) is a common API security solution because it offers quite a number of authentication workflows (called grant types) to fit various levels of security and interaction needs. An important feature of OAuth is that it supports what’s called three-legged authentication. This means the actual authentication event happens at the provider service, which provides an authentication token that’s then used by the client (application or API) to present to the actual service.


![](assets/books/security/assets/token_01.png)

1. The client application makes a request to an OAuth provider service to get a valid token. This is where the username and password are supplied by the client application. For machine-to-machine APIs, we’ll supply the client ID and the client secret.
2. The OAuth provider validates the login identity and returns a special encoded token. This token is what the client application will use when making requests to the API service.
3. The client application sends a request to the API service (for example, GET http://api.example.org/company/132435). The client application includes the token it got from the OAuth provider in the Authorization HTTP header.
4. The API service accepts the request and the token from the client application and sends the token to the OAuth provider to ask if that token is valid.
5. The OAuth provider validates the token and returns it to the API service.
6. The API service, having determined this is a valid token for this request, returns the requested resource response that the client application asked for in Step 3.


- https://aqueduct.io/docs/auth/what_is_oauth/
- https://github.com/christiannwamba/egghead-oauth-demo



https://auth0.com/docs/quickstart/spa/vanillajs#setting-up-the-application

- Configure Auth0
signed up for Auth0
set application(s) settings
Callback URLs: URL in your application where Auth0 redirects 
the user after they have authenticated
Logout URLs

- Integrate Auth0 in your Application

- Users start your appp

- Users Login 
using a third party (Google, Facebook..) via OAuth
When a user logs in, Auth0 returns three items:
. access_token: to learn more, see the Access Token documentation
. id_token: to learn more, see the ID Token documentation
. expires_in: the number of seconds before the Access Token expires

- Calling an api 
with the token received

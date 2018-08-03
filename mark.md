

after walking me through the whole week, he DM me the important points as well , lol


Mark [6:51 PM]
Just a last reinforcing thought I had.  You can think of the token as the api version of the session.

The session is created when you successfully login.  The session identifies the current logged in user and allows him to see the protected web pages.

The token is created when you do the POST request to:
```curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"PASSWORD"}' http://127.0.0.1:8000/api-token-auth/```
You can think of this as “logging in” to your protected apis.

So now you have token which is like a session for your api.  So you use this token to make requests to your protected api endpoints and also the server uses the token to identify who you are.

A big difference between a web session and an api token is the api token has no concept of “logging out”.  The equivalent would be deleting the reference to the token in the admin page or the token expiring
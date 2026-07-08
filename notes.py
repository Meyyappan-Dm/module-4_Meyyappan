"""
====================================================
Task 1 - Django Request Response Cycle
====================================================

1. Journey of a GET /api/courses/ request

Browser
   |
   | HTTP GET Request
   v
URL Router (urls.py)
   |
   | Matches the requested URL
   v
View (views.py)
   |
   | Processes request
   | If data is required...
   v
Model (models.py)
   |
   | Executes database query
   v
Database
   |
   | Returns data
   v
Model
   |
   v
View
   |
   | Creates HttpResponse/JsonResponse
   v
Response returned to Browser


----------------------------------------------------
2. Middleware
----------------------------------------------------

Middleware sits between the incoming request and the view,
and also processes the outgoing response before it reaches
the browser.

Example Built-in Middleware:

1. SecurityMiddleware
   - Adds various security protections.
   - Enables HTTPS redirects and security headers.

2. AuthenticationMiddleware
   - Associates authenticated users with each request.
   - Makes request.user available inside views.


----------------------------------------------------
3. WSGI vs ASGI
----------------------------------------------------

WSGI (Web Server Gateway Interface)
- Supports synchronous applications.
- One request is processed at a time.
- Good for traditional Django applications.

ASGI (Asynchronous Server Gateway Interface)
- Supports asynchronous programming.
- Can handle WebSockets, long-lived connections,
  async views, and real-time applications.
- Better performance for concurrent requests.

By default, Django supports WSGI.

Switch to ASGI when:
- Using async views
- Building chat applications
- Using WebSockets
- Handling many simultaneous connections


----------------------------------------------------
4. MVC vs Django's MVT
----------------------------------------------------

MVC

Model      -> Database Logic
View       -> User Interface
Controller -> Business Logic

Django uses MVT

Model    -> Same as MVC Model
View     -> Acts like MVC Controller
Template -> Acts like MVC View

Mapping

MVC Model      -> Django Model
MVC View       -> Django Template
MVC Controller -> Django View
"""
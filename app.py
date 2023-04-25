from starlette.applications import Starlette
from controllers import Blog_Router


from Auth.Basic_Authentication import BasicAuthBackend
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(debug = True,
                routes=Blog_Router.user_router,
                middleware=middleware)

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from controllers import posts_controller


app = Starlette(debug = True, routes=posts_controller.user_router)

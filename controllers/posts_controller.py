from starlette.routing import Route
from views.posts_view import get_user_posts

# Define the routes
user_router = [
    Route('/', endpoint=get_user_posts, methods=['GET']),
]

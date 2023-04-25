from starlette.routing import Route
from controllers.Blog_Post_Controller import get_user_posts

# Define the routes
user_router = [
    Route('/', endpoint=get_user_posts, methods=['GET'])
]

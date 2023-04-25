import json
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.authentication import requires
from typing import List
from data.blog_post_data import BlogPostDataProvider


@requires("authenticated")
async def get_user_posts(request: Request):
    """This method is responsible to return user blog post data with/without user_id

    Args:
        request (Request): This is starlette request object of http request type.

    Returns:
        _type_: This return jsonresponse for blog post data given user id or response for all users if user id not passed
    """
    user_id = request.query_params.get('user_id')
    serialized_posts =BlogPostDataProvider.seed_blog_posts()
    if user_id:
        blogResults =  [post for post in serialized_posts if post["user_id"] == int(user_id)]
    else:
        blogResults = serialized_posts
    return JSONResponse(content=blogResults)
import json
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.authentication import requires
from typing import List
from data.blog_post_data import BlogPostDataProvider

serialized_posts =BlogPostDataProvider.seed_blog_posts()

@requires("authenticated")
async def get_user_posts(request: Request):
    user_id = request.query_params.get('user_id')
    if user_id:
        blogResults =  [post for post in serialized_posts if post["user_id"] == int(user_id)]
        #result  = json.dumps(blogResults)
    else:
        #result = json.dumps(serialized_posts)
        blogResults = serialized_posts
    return JSONResponse(content=blogResults)
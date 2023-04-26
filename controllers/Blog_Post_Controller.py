from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.authentication import requires
from starlette.exceptions import HTTPException
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
    try:
        user_id = request.query_params.get('user_id')
        serialized_posts =BlogPostDataProvider.seed_blog_posts()
        if user_id:
            blogResults =  [post for post in serialized_posts if post["user_id"] == int(user_id)]
            if blogResults == []:
                blogResults = "Record not found"

        else:
            blogResults = "Record not found"
        return JSONResponse(content=blogResults)
    except HTTPException as e:
        # Handle HTTP errors such as 4xx or 5xx status codes
        return JSONResponse({"error": str(e.detail)}, status_code=e.status_code)
    except Exception as e:
        # Handle other types of exceptions
        return JSONResponse({"error": str(e)}, status_code=500)

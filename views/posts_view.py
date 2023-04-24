from starlette.responses import JSONResponse
from starlette.requests import Request


#DataBase
posts = [
    {
        'post_id' : 1, 'category_id': 100, 'post_name' : "post_name", 'post_title': "post_title",
        'post_description': "post_description",
        'user_id': 1
    },
    {
        'post_id' : 2, 'category_id': 101, 'post_name': "post_name_1", 'post_title': "post_title_1",
        'post_description': "post_description_2",
        'user_id':2
    },
    {
        'post_id' : 3, 'category_id': 103, 'post_name': "post_name_2", 'post_title': "post_title_2",
        'post_description': "post_description_3",
        'user_id':1
    },

]

 
# Views
async def user_posts(request: Request):
    user_id = request.query_params.get('user_id')
    if user_id:
        result  = [post for post in posts if post['user_id'] == int(user_id)]
    else:
        result = posts
    return JSONResponse(content={"data": result})
from models.blog_post_model import BlogPost
from typing import List

class BlogPostDataProvider:
    def seed_blog_posts():
        blog_posts: List[BlogPost] = [
        BlogPost(id=1, title="First post", content="This is my first blog post", user_id=1),
        BlogPost(id=2, title="Second post", content="This is my second blog post", user_id=2),
        BlogPost(id=3, title="Third post", content="This is my third blog post", user_id=1),
        ]

        serialized_posts = [post.dict() for post in blog_posts]

        return serialized_posts


# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Initialize Base object
Base = declarative_base()

# Define Post model
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String)
    body = Column(String)

    # Method to return all posts of user_id = 1
    @staticmethod
    async def get_posts_by_user_id(session: Session):
        posts = session.query(Post).filter(Post.user_id == 1).all()
        return posts

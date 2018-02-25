from handlers.base import BaseHandler
from models.models import Post
from datetime import datetime, timedelta


class DeletePostCron(BaseHandler):
    def get(self):
        current_time = datetime.now()
        time_deleted_limit = current_time - timedelta(days=30)
        posts = Post.query(Post.deleted == True, Post.time_updated < time_deleted_limit).fetch()

        for post in posts:
            post.key.delete()

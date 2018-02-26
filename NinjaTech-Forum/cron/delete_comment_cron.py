from handlers.base import BaseHandler
from models.models import Comment
from datetime import datetime, timedelta


class DeleteCommentCron(BaseHandler):
    def get(self):
        current_time = datetime.now()
        time_deleted_limit = current_time - timedelta(minutes=2)
        comments = Comment.query(Comment.deleted == True, Comment.time_updated < time_deleted_limit).fetch()

        for comment in comments:
            comment.key.delete()
from handlers.base import BaseHandler
from models.models import Comment, Post
from google.appengine.api import users


class DeleteCommentHandler(BaseHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        user = users.get_current_user()
        email = ''

        if user:
            email = user.email()
        comments = Comment.query(Comment.user_email == email, Comment.postID == post.key.id()).fetch()
        params = {
            'post': post,
            'comments': comments
        }
        return self.render_template('delete_comment.html', params=params)

    def post(self, post_id):
        post = Post.get_by_id(int(post_id))

        user = users.get_current_user()
        email = ''

        if user:
            email = user.email()

        comments = Comment.query(Comment.user_email == email, Comment.postID == post.key.id()).fetch()

        for comment in comments:
            if comment.user_email == email:
                comment.deleted = True
                comment.put()

        return self.redirect_to('main-page')

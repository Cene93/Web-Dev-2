import uuid

from handlers.base import BaseHandler
from models.models import Comment, Post
from google.appengine.api import users
import cgi


class CommentHandler(BaseHandler):
    def get(self):
        params = {
        'csrf_token': str(uuid.uuid4())
        }

        memcache.add(params['csrf_token'], True, 60 * 10)
        return self.render_template('add_post.html', params)

    def post(self, post_id):
        post = Post.get_by_id(int(post_id))
        comment = cgi.escape(self.request.get('comment'))
        user = users.get_current_user()
        email = user.email()
        new_comment = Comment(content=comment,
                              postID=post.key.id(),
                              user_email=email)
        new_comment.put()
        return self.redirect_to('post', post_id=post.key.id())

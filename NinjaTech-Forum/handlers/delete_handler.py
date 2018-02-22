from handlers.base import BaseHandler
from models.models import Post
from google.appengine.api import users


class DeleteHandler(BaseHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        params = {
            'post': post
        }
        return self.render_template('delete.html', params=params)

    def post(self, post_id):

        post = Post.get_by_id(int(post_id))
        post.deleted = True
        post.put()
        return self.redirect_to('main-page')
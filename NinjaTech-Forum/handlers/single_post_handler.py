from handlers.base import BaseHandler
from models.models import Post


class PostHandler(BaseHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        params = {
            'post': post
        }
        return self.render_template('post.html', params=params)

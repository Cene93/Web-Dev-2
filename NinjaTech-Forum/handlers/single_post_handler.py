from handlers.base import BaseHandler
from models.models import Post, Comment


class PostHandler(BaseHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        comments = Comment.query(Comment.postID == post.key.id()).order(-Comment.time_posted).fetch()
        params = {
            'post': post,
            'comments': comments
        }
        return self.render_template('post.html', params=params)




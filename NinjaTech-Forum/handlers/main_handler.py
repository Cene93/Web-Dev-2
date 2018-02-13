from handlers.base import BaseHandler
from models.models import Post


class MainHandler(BaseHandler):
    def get(self):
        posts = Post.query(Post.deleted == False).fetch()
        params = {
            'posts': posts
        }
        return self.render_template("home.html", params=params)

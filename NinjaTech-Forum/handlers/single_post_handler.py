from handlers.base import BaseHandler
from models.models import Post, Comment
from google.appengine.api import users


class PostHandler(BaseHandler):
    def get(self, post_id,):
        post = Post.get_by_id(int(post_id))
        comments = Comment.query(Comment.postID == post.key.id()).order(-Comment.time_posted).fetch()
        admin = users.is_current_user_admin()
        author = post.user_email
        user = users.get_current_user()
        email = ''

        if user:
            email = user.email()
            if email == author:
                admin = True


        params = {
            'post': post,
            'comments': comments,
            'admin': admin,
            'author': author,
            'email': email
        }
        return self.render_template('post.html', params=params)




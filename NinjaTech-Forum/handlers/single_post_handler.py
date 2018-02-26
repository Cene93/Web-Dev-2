from handlers.base import BaseHandler
from models.models import Post, Comment
from google.appengine.api import users, memcache
import cgi



class PostHandler(BaseHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        comments = Comment.query(Comment.postID == post.key.id(), Comment.deleted == False).order(-Comment.time_posted).fetch()
        admin = users.is_current_user_admin()
        author = post.user_email
        user = users.get_current_user()
        email = ''

        if user:
            email = user.email()

        params = {
            'post': post,
            'comments': comments,
            'admin': admin,
            'author': author,
            'email': email,
        }
        return self.render_template('post.html', params=params)

    def post(self, post_id):
        value_csrf = self.request.get('csrf-token')

        if not memcache.get(value_csrf):
            return self.write('CSRF Attack Detected!')

        post = Post.get_by_id(int(post_id))
        content = cgi.escape(self.request.get('comment'))
        Comment.save_comment(post_id, content)

        return self.redirect_to('post', post_id=post.key.id())



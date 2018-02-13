from handlers.base import BaseHandler
from models.models import Post
from google.appengine.api import users

class AddPostHandler(BaseHandler):
    def get(self):
        return self.render_template('add_post.html')

    def post(self):
        title = self.request.get('title')
        content = self.request.get('text')
        user = users.get_current_user()
        email = user.email()
        new_post = Post(title=title,
                        content=content,
                        user_email=email)

        new_post.put()
        return self.redirect_to('main-page')

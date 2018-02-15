from handlers.base import BaseHandler
from models.models import Post
from google.appengine.api import users, memcache

import cgi
import uuid

class AddPostHandler(BaseHandler):
    def get(self):
        params = {
        'csrf_token': str(uuid.uuid4())
        }

        memcache.add(params['csrf_token'], True, 60 * 10)
        return self.render_template('add_post.html', params)

    def post(self):
        csrf_value = self.request.get('csrf-token')

        if not memcache.get(csrf_value):
            return self.write('CSRF attack detected!!')

        title = cgi.escape(self.request.get('title'))
        content = cgi.escape(self.request.get('text'))
        user = users.get_current_user()
        email = user.email()
        new_post = Post(title=title,
                        content=content,
                        user_email=email)

        new_post.put()
        return self.redirect_to('post', post_id=new_post.key.id())

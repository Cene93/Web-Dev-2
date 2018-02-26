#!/usr/bin/env python
import os
import jinja2
import webapp2
import uuid
from google.appengine.api import users, memcache
from google.appengine.ext import ndb

from models.models import Users

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}

        if self.request.cookies.get('CookieName') == 'Value':
            params['cookie'] = True

        user = users.get_current_user()
        email = ''
        if not user:
            params['url_login'] = users.create_login_url('/')

        else:
            params['url_logout'] = users.create_logout_url('/')
            email = user.email()


        params['user'] = user

        params['subs'] = Users.query().get()



        params['csrf_token'] = str(uuid.uuid4())
        memcache.add(params['csrf_token'], True, 60 * 10)

        for subscription in Users.query(Users.user_email == email):
            params['subscribe'] = subscription.subscribe

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

from handlers.base import BaseHandler
from models.models import Users
from google.appengine.api import users


class SubscribeHandler(BaseHandler):
    def post(self):
        user = users.get_current_user()
        email = user.email()

        subscribers = Users.query().get()

        if subscribers is None or subscribers.user_email != email:
            new_user = Users(user_email=email,
                             subscribe=True)
            new_user.put()
        else:
            if subscribers.subscribe:
                subscribers.subscribe = False
                subscribers.put()
            else:
                subscribers.subscribe = True
                subscribers.put()

        referrer = self.request.headers.get('referer')
        if referrer:
            return self.redirect(referrer)
        return self.redirect_to('main-page')
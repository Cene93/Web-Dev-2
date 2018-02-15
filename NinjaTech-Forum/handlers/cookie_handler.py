from handlers.base import BaseHandler

class CookieHandler(BaseHandler):
    def post(self):
        self.response.set_cookie('CookieName', 'Value')
        return self.redirect_to('main-page')
from handlers.base import BaseHandler


class CookieHandler(BaseHandler):
    def post(self):
        self.response.set_cookie('CookieName', 'Value')

        referrer = self.request.headers.get('referer')
        if referrer:
            return self.redirect(referrer)
        return self.redirect_to('main-page')

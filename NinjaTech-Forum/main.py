#!/usr/bin/env python
import webapp2
from handlers.main_handler import MainHandler
from handlers.cookie_handler import CookieHandler
from handlers.post_handler import AddPostHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/add-post', AddPostHandler),
], debug=True)

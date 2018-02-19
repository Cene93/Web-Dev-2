#!/usr/bin/env python
import webapp2

from handlers.comment_handler import CommentHandler
from handlers.main_handler import MainHandler
from handlers.cookie_handler import CookieHandler
from handlers.post_handler import AddPostHandler
from handlers.single_post_handler import PostHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/add-post', AddPostHandler, name='posts'),
    webapp2.Route('/r/<post_id:\d+>', PostHandler, name='post'),
    webapp2.Route('/r/<post_id:\d+>/new-comment', CommentHandler),
], debug=True)

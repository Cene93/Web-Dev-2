from google.appengine.ext import ndb


class Post(ndb.Model):
    content = ndb.TextProperty()
    title = ndb.StringProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty(auto_now_add=True)
    time_updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)


class Comment(ndb.Model):
    postID = ndb.StringProperty()
    content = ndb.TextProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty(auto_now_add=True)
    time_updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)



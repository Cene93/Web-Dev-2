from google.appengine.ext import ndb


class Post(ndb.Model):
    content = ndb.TextProperty()
    title = ndb.StringProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty()
    time_updated = ndb.DateTimeProperty()
    time_deleted = ndb.DateTimeProperty()


class Comment(ndb.Model):
    postID = ndb.StringProperty()
    content = ndb.TextProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty()
    time_updated = ndb.DateTimeProperty()
    time_deleted = ndb.DateTimeProperty()



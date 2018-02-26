from google.appengine.ext import ndb
from google.appengine.api import users, taskqueue


class Post(ndb.Model):
    content = ndb.TextProperty()
    title = ndb.StringProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty(auto_now_add=True)
    time_updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)


class Comment(ndb.Model):
    postID = ndb.IntegerProperty()
    content = ndb.TextProperty()
    user_email = ndb.StringProperty()
    time_posted = ndb.DateTimeProperty(auto_now_add=True)
    time_updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @staticmethod
    def save_comment(post_id, content):
        post = Post.get_by_id(int(post_id))
        user = users.get_current_user()
        email = user.email()
        new_comment = Comment(content=content,
                              user_email=email,
                              postID=post.key.id())
        new_comment.put()

        post = Post.get_by_id(int(post_id))
        taskqueue.add(url='/task/send-comment-mail',
                      params={
                          'op_email': post.user_email,
                          'comment_email': email
                      })


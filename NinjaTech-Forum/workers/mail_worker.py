from handlers.base import BaseHandler
from google.appengine.api import mail

class MailWorker(BaseHandler):
    def post(self):
        op_email = self.request.get('op_email')
        comment_email = self.request.get('comment_email')
        mail.send_mail('info@ninjaforum.si', comment_email, 'New Comment',
                       '<b>%s</b> has commented on your post.' % op_email)
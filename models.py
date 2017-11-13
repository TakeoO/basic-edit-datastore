from google.appengine.ext import ndb


class Message(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()

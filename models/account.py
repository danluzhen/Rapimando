# -*- coding: utf-8 -*-


from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import messages

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


class Accounting(ndb.Model):
    pass
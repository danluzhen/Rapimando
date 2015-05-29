# -*- coding: utf-8 -*-


from google.appengine.ext import ndb
from .user import User
from handlers import TrackerResponse, TrackerListResponse

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


class Tracker(ndb.Model):
    date_time = ndb.DateTimeProperty(auto_now_add=True)
    location = ndb.GeoPtProperty(required=True)
    user = ndb.KeyProperty(kind=User)

    @property
    def timestamp(self):
        """Property to format a datetime object to string."""
        return self.date_time.strftime(TIME_FORMAT_STRING)

    def to_message(self):
        """
        """
        response = TrackerResponse(id=self.key.id(),
                                   latitude=self.location.lat,
                                   longitude=self.location.lon,
                                   date_time=self.timestamp)
        return response

    @classmethod
    def put_from_message(cls, data):
        user = ndb.Key(User, data.id)
        entity = cls(location=ndb.GeoPt(data.latitude, data.longitude),
                     user=user)
        entity.put()
        user = user.get()
        user.current_location = ndb.GeoPt(data.latitude, data.longitude)
        user.put()
        return entity.to_message()
    @classmethod
    def get_trackers(cls, data):
        user = ndb.Key(User, data.id)
        query = cls.query(Tracker.user == user).order(-cls.date_time)
        items = [entity.to_message() for entity in query.fetch(data.per_page)]
        return TrackerListResponse(trackers=items)
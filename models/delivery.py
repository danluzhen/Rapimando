# -*- coding: utf-8 -*-


from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from handlers import DeliveryResponse
from .user import User

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


def get_endpoints_current_user(raise_unauthorized=True):
    """Returns a current user and (optionally) causes an HTTP 401 if no user.
    Args:
        raise_unauthorized: Boolean; defaults to True. If True, this method
            raises an exception which causes an HTTP 401 Unauthorized to be
            returned with the request.
    Returns:
        The signed in user if there is one, else None if there is no signed in
        user and raise_unauthorized is False.
    """
    current_user = endpoints.get_current_user()
    if raise_unauthorized and current_user is None:
        raise endpoints.UnauthorizedException('Invalid token.')
    return current_user


class Delivery(ndb.Model):
    user = ndb.KeyProperty(kind=User)
    partner = ndb.KeyProperty(kind=User)
    pickup_notes = ndb.StringProperty()
    pickup_requested = ndb.DateTimeProperty(auto_now_add=True)
    pickup_accepted = ndb.DateTimeProperty()
    pickup_address = ndb.StringProperty()
    pickup_location = ndb.GeoPtProperty()
    pickup_datetime = ndb.DateTimeProperty()
    pickup_wait = ndb.IntegerProperty()
    pickup_photo = ndb.StringProperty()
    delivery_address = ndb.StringProperty()
    delivery_location = ndb.GeoPtProperty()
    price = ndb.FloatProperty

    @property
    def to_message(self):
        """
        """
        return DeliveryResponse(id=self.key.id(),
                                user=self.user.get().to_message(),
                                partner=self.user.get().to_message(),
                                pickup_notes=self.pickup_notes,
                                pickup_requested=self.pickup_requested.strftime(TIME_FORMAT_STRING),
                                pickup_accepted=self.pickup_accepted.strftime(TIME_FORMAT_STRING),
                                pickup_address=self.pickup_address,
                                pickup_location=self.pickup_location,
                                pickup_datetime=self.pickup_datetime.strftime(TIME_FORMAT_STRING),
                                pickup_wait=self.pickup_wait,
                                pickup_photo=self.pickup_photo,
                                delivery_address=self.delivery_address,
                                delivery_location=self.delivery_location)

    @classmethod
    def put_from_message(cls, data):
        current_user = get_endpoints_current_user()
        entity = cls(user=ndb.Key(User, current_user.id),
                     pickup_notes=data.country,
                     pickup_address=data.pickup_address,
                     pickup_location=ndb.GeoPt(data.latitude, data.longitude),
                     location=ndb.GeoPt(data.latitude, data.longitude),
                     price=data.price)
        entity.put()
        # TODO: find all driver nearby and notify
        return entity.to_message()
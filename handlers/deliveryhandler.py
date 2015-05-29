# -*- coding: utf-8 -*-
from protorpc import messages
from .userhandler import UserResponse

class DeliveryRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    pickup_notes = messages.StringField(1)
    pickup_accepted = messages.StringField(2)
    pickup_address = messages.StringField(3)
    pickup_latitude = messages.FloatField(4)
    pickup_longitude = messages.FloatField(5)
    pickup_datetime = messages.StringField(6)
    pickup_wait = messages.IntegerField(7)
    pickup_photo = messages.StringField(8)
    delivery_address = messages.StringField(9)
    delivery_latitude = messages.FloatField(10)
    delivery_longitude = messages.FloatField(11)


class DeliveryResponse(messages.Message):
    """DeliveryResponse that stores a message."""
    id = messages.IntegerField(1)
    user = messages.MessageField(UserResponse, 2)
    partner = messages.MessageField(UserResponse, 3)
    pickup_notes = messages.StringField(4)
    pickup_accepted = messages.StringField(5)
    pickup_address = messages.StringField(6)
    pickup_latitude = messages.FloatField(7)
    pickup_longitude = messages.FloatField(8)
    pickup_datetime = messages.StringField(9)
    pickup_wait = messages.IntegerField(10)
    pickup_photo = messages.StringField(11)
    delivery_address = messages.StringField(12)
    delivery_latitude = messages.FloatField(13)
    delivery_longitude = messages.FloatField(14)

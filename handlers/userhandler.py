# -*- coding: utf-8 -*-
from google.appengine.ext import endpoints
from protorpc import messages


class UserRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    email = messages.StringField(1)
    password = messages.StringField(2)
    type = messages.StringField(3)
    first_name = messages.StringField(4)
    last_name = messages.StringField(5)
    gender = messages.StringField(6)
    picture = messages.StringField(7)
    mobile = messages.StringField(8)
    country = messages.StringField(9)
    site = messages.StringField(10)
    address = messages.StringField(11)
    birthday = messages.StringField(12)
    fbid = messages.StringField(13)
    gid = messages.StringField(14)
    balance = messages.StringField(16)
    access_token = messages.StringField(17)
    device_type = messages.StringField(19)
    device_id = messages.StringField(20)
    latitude = messages.FloatField(21)
    longitude = messages.FloatField(22)
    page = messages.IntegerField(23)
    per_page = messages.IntegerField(24)
    radius = messages.FloatField(25)
    status = messages.StringField(26)


class UserResponse(messages.Message):
    """UserResponse that stores a message."""
    id = messages.IntegerField(1)
    email = messages.StringField(2)
    type = messages.StringField(3)
    first_name = messages.StringField(4)
    last_name = messages.StringField(5)
    gender = messages.StringField(6)
    picture = messages.StringField(7)
    mobile = messages.StringField(8)
    country = messages.StringField(9)
    site = messages.StringField(10)
    address = messages.StringField(11)
    birthday = messages.StringField(12)
    fbid = messages.StringField(13)
    gid = messages.StringField(14)
    balance = messages.StringField(15)
    status = messages.StringField(16)


class UsersListResponse(messages.Message):
    """Collection of UserResponses."""
    users = messages.MessageField(UserResponse, 1, repeated=True)

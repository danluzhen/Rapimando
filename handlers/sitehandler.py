# -*- coding: utf-8 -*-
from protorpc import messages
from .pricehandler import PriceResponse

class SiteRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    name = messages.StringField(2)
    country = messages.StringField(3)
    locale = messages.StringField(4)
    area_code = messages.StringField(5)
    latitude = messages.FloatField(6)
    longitude = messages.FloatField(7)
    gateway = messages.StringField(8)
    price = messages.IntegerField(9)
    page = messages.IntegerField(10)
    per_page = messages.IntegerField(11)


class SiteResponse(messages.Message):
    """SiteResponse that stores a message."""
    id = messages.IntegerField(1)
    name = messages.StringField(2)
    country = messages.StringField(3)
    locale = messages.StringField(4)
    area_code = messages.StringField(5)
    latitude = messages.FloatField(6)
    longitude = messages.FloatField(7)
    gateway = messages.StringField(8)
    price = messages.MessageField(PriceResponse, 9)


class SiteListResponse(messages.Message):
    """Collection of SiteResponse."""
    sites = messages.MessageField(SiteResponse, 1, repeated=True)
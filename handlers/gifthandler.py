# -*- coding: utf-8 -*-
from protorpc import messages
from .sitehandler import SiteResponse

class GiftRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    code = messages.StringField(2)
    gift = messages.StringField(3)
    site = messages.IntegerField(4)
    page = messages.IntegerField(5)
    per_page = messages.IntegerField(6)


class GiftResponse(messages.Message):
    """GiftResponse that stores a message."""
    id = messages.IntegerField(1)
    code = messages.StringField(2)
    gift = messages.StringField(3)
    site = messages.MessageField(SiteResponse, 4)


class GiftListResponse(messages.Message):
    """Collection of PriceResponse."""
    gifts = messages.MessageField(GiftResponse, 1, repeated=True)
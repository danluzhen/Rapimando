# -*- coding: utf-8 -*-
from protorpc import messages


class PriceRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    name = messages.StringField(2)
    currency_code = messages.StringField(3)
    limit = messages.IntegerField(4)


class PriceResponse(messages.Message):
    """PriceResponse that stores a message."""
    id = messages.IntegerField(1)
    name = messages.StringField(2)
    currency_code = messages.StringField(3)


class PriceListResponse(messages.Message):
    """Collection of PriceResponse."""
    prices = messages.MessageField(PriceResponse, 1, repeated=True)
# -*- coding: utf-8 -*-
from protorpc import messages


class TransactionRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    name = messages.StringField(2)
    currency_code = messages.StringField(3)
    limit = messages.IntegerField(4)


class TransactionResponse(messages.Message):
    """PriceResponse that stores a message."""
    id = messages.IntegerField(1)
    name = messages.StringField(2)
    currency_code = messages.StringField(3)


class TransactionListResponse(messages.Message):
    """Collection of PriceResponse."""
    prices = messages.MessageField(TransactionResponse, 1, repeated=True)
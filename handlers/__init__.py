# -*- coding: utf-8 -*-
from protorpc import messages
from userhandler import UserRequest, UserResponse, UsersListResponse
from sitehandler import SiteRequest, SiteResponse, SiteListResponse
from pricehandler import PriceRequest, PriceResponse, PriceListResponse
from gifthandler import GiftRequest, GiftResponse, GiftListResponse
from trackerhanler import TrackerResponse, TrackerListResponse
from deliveryhandler import DeliveryRequest, DeliveryResponse


class BaseResponse(messages.Message):
    """PriceResponse that stores a message."""
    messages = messages.StringField(1)
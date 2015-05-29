import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import urllib
import json
import hashlib

from handlers import (
    BaseResponse,
    UserResponse,
    UserRequest,
    UsersListResponse,
    SiteRequest,
    SiteResponse,
    SiteListResponse,
    PriceRequest,
    PriceResponse,
    PriceListResponse,
    GiftRequest,
    GiftResponse,
    GiftListResponse,
    TrackerResponse,
    TrackerListResponse,
    DeliveryRequest,
    DeliveryResponse
)
from models import User, Site, Price, Gift, Tracker, Delivery


CLIENT_ID = '889708994401-c7f9oec1ph6skst1u0k7n5g42obbt0dv.apps.googleusercontent.com'

api_server = endpoints.api(name='rapimandado', version='v1',
                           description='Rapimandado API',
                           allowed_client_ids=[CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID])
@api_server.api_class(resource_name='users')
class UsersService(remote.Service):
    """User API v1."""

    @endpoints.method(UserRequest, UserResponse,
                      path='users/login/fb', http_method='GET',
                      name='loginFB')
    def login_fb(self, request):
        """Login with facebook account"""
        link = "https://graph.facebook.com/me?access_token=" + request.access_token
        f = urllib.urlopen(link)
        content = f.read()
        content = json.loads(content)
        entity = User.query_fbid(content, request.type)
        return entity

    @endpoints.method(UserRequest, UserResponse,
                      path='users/login/email', http_method='POST',
                      name='loginEmail')
    def login_email(self, request):
        """Login with email account"""
        entity = User.query_user_by_email(request.email)
        if len(entity) == 0:
            raise endpoints.NotFoundException('Email "%s" not found.' % (request.email,))
        else:
            user = entity[0]
            m = hashlib.md5()
            m.update(request.password)
            if m.hexdigest() == user.password:
                return user.to_message()
            else:
                raise endpoints.NotFoundException('Invalid password')

    @endpoints.method(UserRequest, UserResponse,
                      path='users/register', http_method='POST',
                      name='registerByEmail')
    def register_by_email(self, request):
        """Register by email"""
        entity = User.query_user_by_email(request.email)
        if len(entity) > 0:
            raise endpoints.BadRequestException('Email "%s" are ready exists.' % (request.email,))
        else:
            entity = User.register_email(request)
            return entity
    ID_USER_RESOURCE = endpoints.ResourceContainer(
        UserRequest,
        id=messages.IntegerField(1, variant=messages.Variant.INT64))

    @endpoints.method(ID_USER_RESOURCE, UserResponse,
                      path='users/{id}', http_method='PUT',
                      name='updateUser')
    def update_user(self, request):
        """Update user info"""
        entity = User.update_user(request)
        if entity:
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_USER_RESOURCE, UserResponse,
                      path='users/{id}/device', http_method='PUT',
                      name='updateUserDevice')
    def update_user_device(self, request):
        """Update device: device_id, device_type (iOS | Android)"""
        entity = User.get_by_id(request.id)
        if entity:
            entity.device_type = request.device_type
            entity.device_id = request.device_id
            entity.put()
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_USER_RESOURCE, TrackerResponse,
                      path='users/{id}/locations', http_method='POST',
                      name='updateUserLocation')
    def update_user_location(self, request):
        """Update current location of user"""
        entity = User.get_by_id(request.id)
        if entity:
            entity = Tracker.put_from_message(request)
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_USER_RESOURCE, TrackerListResponse,
                      path='users/{id}/locations', http_method='GET',
                      name='getUserLocation')
    def get_user_location(self, request):
        """Get tracker location of user"""
        entity = User.get_by_id(request.id)
        if entity:
            entity = Tracker.get_trackers(request)
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(UserRequest, UsersListResponse,
                      path='users', http_method='GET',
                      name='users.show')
    def users_show(self, request):
        """Show all users"""
        entity = User.get_users(request)
        return entity

    @endpoints.method(UserRequest, UsersListResponse,
                      path='users/nearby', http_method='GET',
                      name='getUserNearby')
    def get_user_location(self, request):
        """Get drivers near by the current location of user"""
        entity = User.get_users_nearby(request)
        return entity

@api_server.api_class(resource_name='sites')
class SitesService(remote.Service):
    """Site API v1."""

    @endpoints.method(SiteRequest, SiteResponse,
                      path='sites', http_method='POST',
                      name='sites.insert')
    def sites(self, request):
        """Create a new site"""
        entity = Site.put_from_message(request)
        return entity

    @endpoints.method(SiteRequest, SiteListResponse,
                      path='sites', http_method='GET',
                      name='sites.show')
    def sites_show(self, request):
        """Show all sites"""
        entity = Site.get_sites(request)
        return entity

    ID_SITE_RESOURCE = endpoints.ResourceContainer(
        SiteRequest,
        id=messages.IntegerField(1, variant=messages.Variant.INT64))
    @endpoints.method(ID_SITE_RESOURCE, SiteResponse,
                      path='sites/{id}', http_method='PUT',
                      name='sites.update')
    def site_update(self, request):
        """Update info a site"""
        entity = Site.site_update(request)
        if entity:
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_SITE_RESOURCE, BaseResponse,
                      path='sites/{id}', http_method='DELETE',
                      name='sites.delete')
    def site_delete(self, request):
        """Delete site"""
        entity = Site.get_by_id(request.id)
        if entity:
            entity.key.delete()
            return BaseResponse(messages="")
        else:
            raise endpoints.NotFoundException()

@api_server.api_class(resource_name='prices')
class PricesService(remote.Service):
    """Price API v1."""

    @endpoints.method(PriceRequest, PriceResponse,
                      path='prices', http_method='POST',
                      name='prices.insert')
    def prices(self, request):
        """Create new price"""
        entity = Price.put_from_message(request)
        return entity

    @endpoints.method(PriceRequest, PriceListResponse,
                      path='prices', http_method='GET',
                      name='prices.show')
    def prices_show(self, request):
        """Show all prices"""
        entity = Price.get_prices(request)
        return entity

    ID_PRICE_RESOURCE = endpoints.ResourceContainer(
        PriceRequest,
        id=messages.IntegerField(1, variant=messages.Variant.INT64))
    @endpoints.method(ID_PRICE_RESOURCE, PriceResponse,
                      path='prices/{id}', http_method='PUT',
                      name='prices.update')
    def price_update(self, request):
        """Update a price"""
        entity = Price.price_update(request)
        if entity:
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_PRICE_RESOURCE, BaseResponse,
                      path='prices/{id}', http_method='DELETE',
                      name='prices.delete')
    def price_delete(self, request):
        """Delete a price"""
        entity = Price.get_by_id(request.id)
        if entity:
            entity.key.delete()
            return BaseResponse(messages="")
        else:
            raise endpoints.NotFoundException()


@api_server.api_class(resource_name='gifts')
class GiftsService(remote.Service):
    """Gift API v1."""

    @endpoints.method(GiftRequest, GiftResponse,
                      path='gifts', http_method='POST',
                      name='gifts.insert')
    def gifts(self, request):
        """Create a new gift"""
        entity = Gift.put_from_message(request)
        return entity

    @endpoints.method(GiftRequest, GiftListResponse,
                      path='gifts', http_method='GET',
                      name='gifts.show')
    def gifts_show(self, request):
        """Show all gifts"""
        entity = Gift.get_gifts(request)
        return entity

    ID_GIFT_RESOURCE = endpoints.ResourceContainer(
        GiftRequest,
        id=messages.IntegerField(1, variant=messages.Variant.INT64))
    @endpoints.method(ID_GIFT_RESOURCE, GiftResponse,
                      path='gifts/{id}', http_method='PUT',
                      name='gifts.update')
    def gift_update(self, request):
        """Update a gift"""
        entity = Gift.gift_update(request)
        if entity:
            return entity
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_GIFT_RESOURCE, BaseResponse,
                      path='gifts/{id}', http_method='DELETE',
                      name='gifts.delete')
    def gift_delete(self, request):
        """Delete a gift"""
        entity = Gift.get_by_id(request.id)
        if entity:
            entity.key.delete()
            return BaseResponse(messages="")
        else:
            raise endpoints.NotFoundException()


@api_server.api_class(resource_name='delivery')
class DeliveryService(remote.Service):
    """Delivery API v1."""

    @endpoints.method(DeliveryRequest, DeliveryResponse,
                      path='delivery', http_method='POST',
                      name='delivery.add')
    def delivery(self, request):
        """Create a new delivery"""
        entity = Delivery.put_from_message(request)
        return entity

    ID_DELIVERY_RESOURCE = endpoints.ResourceContainer(
        DeliveryRequest,
        id=messages.IntegerField(1, variant=messages.Variant.INT64))

    @endpoints.method(ID_DELIVERY_RESOURCE, DeliveryRequest,
                      path='delivery/{id}', http_method='GET',
                      name='delivery.index')
    def delivery_index(self, request):
        """Get info of the delivery"""
        entity = Delivery.get_by_id(request.id)
        if entity:
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_DELIVERY_RESOURCE, DeliveryRequest,
                      path='delivery/{id}/estimate', http_method='POST',
                      name='delivery.estimate')
    def delivery_estimate(self, request):
        """After have detail information of request delivery, partner will send estimated time to user"""
        entity = Delivery.get_by_id(request.id)
        if entity:
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_DELIVERY_RESOURCE, DeliveryRequest,
                      path='delivery/{id}/confirm', http_method='POST',
                      name='delivery.confirm')
    def delivery_confirm(self, request):
        """User can accept or reject estimated time from partner"""
        entity = Delivery.get_by_id(request.id)
        if entity:
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_DELIVERY_RESOURCE, DeliveryRequest,
                      path='delivery/{id}/success', http_method='POST',
                      name='delivery.success')
    def delivery_success(self, request):
        """Confirm delivery success"""
        entity = Delivery.get_by_id(request.id)
        if entity:
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()

    @endpoints.method(ID_DELIVERY_RESOURCE, DeliveryRequest,
                      path='delivery/{id}/rate', http_method='POST',
                      name='delivery.rate')
    def delivery_rate(self, request):
        """After delivery success, user or partner can rate about this."""
        entity = Delivery.get_by_id(request.id)
        if entity:
            return entity.to_message()
        else:
            raise endpoints.NotFoundException()



APPLICATION = endpoints.api_server([api_server])
# -*- coding: utf-8 -*-


from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import messages
from .price import Price
from handlers import SiteResponse, SiteListResponse

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


class Site(ndb.Model):
    name = ndb.StringProperty(required=True)
    country = ndb.StringProperty()
    locale = ndb.StringProperty()
    area_code = ndb.StringProperty()
    location = ndb.GeoPtProperty()
    gateway = ndb.StringProperty()
    price = ndb.KeyProperty(kind=Price)

    @property
    def timestamp(self):
        """Property to format a datetime object to string."""
        return self.played.strftime(TIME_FORMAT_STRING)

    def to_message(self):
        """
        """
        response = SiteResponse(id=self.key.id(),
                                name=self.name,
                                country=self.country,
                                locale=self.locale,
                                area_code=self.area_code,
                                latitude=self.location.lat,
                                longitude=self.location.lon,
                                gateway=self.gateway)
        if self.price:
            response.price = self.price.get().to_message()
        return response

    @classmethod
    def put_from_message(cls, data):
        entity = cls(name=data.name,
                     country=data.country,
                     locale=data.locale,
                     area_code=data.area_code,
                     location=ndb.GeoPt(data.latitude, data.longitude),
                     gateway=data.gateway,)
        if data.price:
            price = ndb.Key(Price, data.price)
            entity.price = price
        entity.put()
        return entity.to_message()

    @classmethod
    def get_sites(cls, data):
        query = cls.query()
        items = [entity.to_message() for entity in query.fetch(data.per_page)]
        return SiteListResponse(sites=items)

    @classmethod
    def site_update(cls, data):
        entity = cls.get_by_id(data.id)
        if entity:
            entity.name = data.name
            entity.country = data.country
            entity.locale = data.locale
            entity.area_code = data.area_code
            entity.location = ndb.GeoPt(data.latitude, data.longitude)
            entity.gateway = data.gateway
            if data.price:
                price = ndb.Key(Price, data.price)
                entity.price = price
            elif entity.price and not data.price:
                del entity.price
            entity.put()
            return entity.to_message()
        else:
            return False
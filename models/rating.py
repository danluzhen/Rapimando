# -*- coding: utf-8 -*-


from google.appengine.ext import ndb
from handlers import PriceResponse, PriceListResponse

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


class Rating(ndb.Model):
    name = ndb.StringProperty(required=True)
    currency_code = ndb.StringProperty(required=True)


    @property
    def timestamp(self):
        """Property to format a datetime object to string."""
        return self.played.strftime(TIME_FORMAT_STRING)

    def to_message(self):
        """
        """
        return PriceResponse(id=self.key.id(),
                             name=self.name,
                             currency_code=self.currency_code)

    @classmethod
    def put_from_message(cls, data):
        entity = cls(name=data.name,
                     currency_code=data.currency_code)
        entity.put()
        return entity.to_message()

    @classmethod
    def get_prices(cls, data):
        query = cls.query()
        items = [entity.to_message() for entity in query.fetch(data.limit)]
        return PriceListResponse(prices=items)

    @classmethod
    def price_update(cls, data):
        entity = cls.get_by_id(data.id)
        if entity:
            entity.name = data.name
            entity.currency_code = data.currency_code
            entity.put()
            return entity.to_message()
        else:
            return False
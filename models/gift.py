# -*- coding: utf-8 -*-


from google.appengine.ext import ndb
from handlers import GiftResponse, GiftListResponse
from .site import Site
TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'


class Gift(ndb.Model):
    code = ndb.StringProperty(required=True)
    gift = ndb.StringProperty(required=True)
    site = ndb.KeyProperty(kind=Site)

    @property
    def timestamp(self):
        """Property to format a datetime object to string."""
        return self.played.strftime(TIME_FORMAT_STRING)

    def to_message(self):
        """
        """
        response = GiftResponse(id=self.key.id(),
                                code=self.code,
                                gift=self.gift)
        if self.site and self.site.get():
            response.site = self.site.get().to_message()
        return response
    @classmethod
    def put_from_message(cls, data):
        entity = cls(code=data.code,
                     gift=data.gift)
        if data.site:
            site = ndb.Key(Site, data.site)
            entity.site = site
        entity.put()
        return entity.to_message()

    @classmethod
    def get_gifts(cls, data):
        query = cls.query()
        items = [entity.to_message() for entity in query.fetch(data.per_page)]
        return GiftListResponse(gifts=items)

    @classmethod
    def gift_update(cls, data):
        entity = cls.get_by_id(data.id)
        if entity:
            entity.code = data.code
            entity.gift = data.gift
            if data.site:
                site = ndb.Key(Site, data.site)
                entity.site = site
            elif entity.site and not data.site:
                del entity.site
            entity.put()
            return entity.to_message()
        else:
            return False
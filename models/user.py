# -*- coding: utf-8 -*-


from google.appengine.ext import ndb
from handlers import UserResponse, UsersListResponse
from .site import Site
import hashlib
import math

TIME_FORMAT_STRING = '%b %d, %Y %I:%M:%S %p'



class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty()
    type = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    gender = ndb.StringProperty()
    picture = ndb.StringProperty()
    mobile = ndb.StringProperty()
    country = ndb.StringProperty()
    site = ndb.StructuredProperty(Site)
    address = ndb.StringProperty()
    birthday = ndb.StringProperty()
    fbid = ndb.StringProperty()
    gid = ndb.StringProperty()
    current_location = ndb.GeoPtProperty()
    balance = ndb.StringProperty()
    device_type = ndb.StringProperty()
    device_id = ndb.StringProperty()
    status = ndb.StringProperty()

    @property
    def timestamp(self):
        """Property to format a datetime object to string."""
        return self.played.strftime(TIME_FORMAT_STRING)

    def to_message(self):
        """
        """
        return UserResponse(id=self.key.id(),
                            email=self.email,
                            type=self.type,
                            first_name=self.first_name,
                            last_name=self.last_name,
                            gender=self.gender,
                            picture=self.picture,
                            mobile=self.mobile,
                            country=self.country,
                            site=self.site,
                            address=self.address,
                            birthday=self.birthday,
                            fbid=self.fbid,
                            gid=self.gid,
                            balance=self.balance,
                            status=self.status)

    @classmethod
    def register_email(cls, data):
        m = hashlib.md5()
        m.update(data.password)
        data.password = m.hexdigest()
        entity = cls(email=data.email,
                     type=data.type,
                     first_name=data.first_name,
                     last_name=data.last_name,
                     gender=data.gender,
                     country=data.country,
                     mobile=data.mobile,
                     address=data.address,
                     password=data.password)
        entity.put()
        return entity.to_message()

    @classmethod
    def query_user_by_email(cls, email):
        user = cls.query(cls.email == email).fetch(1)
        return user

    @classmethod
    def query_fbid(cls, data, type_user=None):
        """
        """
        if type_user is None:
            type_user = 'user'
        users = cls.query(cls.fbid == data['id']).fetch(1)
        if users:
            return users[0].to_message()
        else:
            entity = cls(email=data['email'],
                         type=type_user,
                         first_name=data['first_name'],
                         last_name=data['last_name'],
                         gender=data['gender'],
                         birthday=data['birthday'],
                         fbid=data['id'])
            entity.put()
            return entity.to_message()

    @classmethod
    def get_users(cls, data):
        query = cls.query()
        items = [entity.to_message() for entity in query.fetch(data.per_page)]
        return UsersListResponse(users=items)

    @classmethod
    def update_user(cls, data):
        updatable = {'first_name', 'last_name', 'gender', 'country', 'address', 'status'}
        entity = cls.get_by_id(data.id)
        if entity:
            for name in updatable:
                if getattr(data, name) is not None:
                    setattr(entity, name, getattr(data, name))
            entity.put()
            return entity.to_message()
        else:
            return False

    @classmethod
    def get_users_nearby(cls, request):
        """
        """
        if request.latitude is None:
            request.latitude = 51.6226785
        if request.longitude is None:
            request.longitude = -0.1950272
        if request.radius is None:
            request.radius = 3.0

        latitude1 = request.latitude - (request.radius / 111.045)
        latitude2 = request.latitude + (request.radius / 111.045)
        longitude1 = request.longitude - (request.radius / (111.045 * math.cos(math.radians(request.latitude))))
        longitude2 = request.longitude + (request.radius / (111.045 * math.cos(math.radians(request.latitude))))
        query = cls.query(cls.type == 'user',
                          cls.current_location >= ndb.GeoPt(latitude1, longitude1),
                          cls.current_location <= ndb.GeoPt(latitude2, longitude2))
        users = [entity.to_message() for entity in query.fetch()]
        return UsersListResponse(users=users)
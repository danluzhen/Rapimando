# -*- coding: utf-8 -*-
from protorpc import messages


class TrackerResponse(messages.Message):
    id = messages.IntegerField(1)
    latitude = messages.FloatField(2)
    longitude = messages.FloatField(3)
    date_time = messages.StringField(4)


class TrackerListResponse(messages.Message):
    """Collection of SiteResponse."""
    trackers = messages.MessageField(TrackerResponse, 1, repeated=True)
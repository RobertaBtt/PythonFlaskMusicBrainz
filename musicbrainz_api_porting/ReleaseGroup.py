__author__ = 'RobertaBtt'

import simplejson as json

class ReleaseGroup:

    def __init__(self, id, type_id, type):
        self._id = id
        self._type_id = type_id
        self._type = type
        self._title = None
        self._first_release_date = None

    def to_json(self):
        json_data = json.dumps(self.__dict__)
        return json_data


    # ***********
    # A Release Group List has
    # - a title
    #*************

    def set_title(self, title):
        self._title = title



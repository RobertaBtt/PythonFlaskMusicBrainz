__author__ = 'RobertaBtt'

import simplejson as json


class ReleaseGroup:
    def __init__(self, uuid):
        self.uuid = uuid

    def to_json(self):
        json_data = json.dumps(self.__dict__)
        return json_data
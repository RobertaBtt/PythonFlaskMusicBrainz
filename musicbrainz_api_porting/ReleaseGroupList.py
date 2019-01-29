__author__ = 'RobertaBtt'

import simplejson as json


class ReleaseGroupList:
    def __init__(self, count):
        self._count = count
        self._release_group = []


    def to_json(self):
        json_data = json.dumps(self.__dict__)
        return json_data


    # ***********
    # A Release Group List has a list of ReleaseGroup
    #*************

    def add_release_group(self, release_group_object):
        self._release_group.append(release_group_object)
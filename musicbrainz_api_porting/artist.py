__author__ = 'RobertaBtt'

import simplejson as json


class Artist:
    def __init__(self, id):
        self._id = id
        self._release_group_list = []
        self._name = None

    def to_json(self):
        json_data = json.dumps(self.__dict__)
        return json_data

    # ***********
    # An Artist has
    # - a name
    # - an id
    # - a list of release groups
    #*************

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def set_release_groups(self, release_group_list):
        self._release_group_list = release_group_list

    def get_release_group_list(self):
        return self._release_group_list

    def add_release_group_to_artist(self, release_group_object):
        self._release_group_list.append(release_group_object)
__author__ = 'RobertaBtt'

import simplejson as json

from . import ReleaseGroupList

class Artist:
    def __init__(self, id):
        self.id = id
        self.release_group_list = []
        self.name = None

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
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_release_groups(self, release_group_list):
        self.release_group_list = release_group_list

    def get_release_group_list(self):
        return self.release_group_list

    def add_release_group_to_artist(self, release_group_object):
        self.release_group_list.append(release_group_object)
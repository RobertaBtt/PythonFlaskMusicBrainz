__author__ = 'RobertaBtt'

import simplejson as json

from musicbrainz_api_porting import ReleaseGroup

class ReleaseGroupList:
    def __init__(self, count):
        self.count = count
        self.release_group = []

    def __str__(self):
        return self.to_json()

    def to_json(self):
        self.release_group.append(ReleaseGroup.ReleaseGroup("id", "id-type", "type"))
        json_data = json.dumps(self.__dict__)
        return json_data


    # ***********
    # A Release Group List has a list of ReleaseGroup
    #*************


    def get_count(self):
        return self.count


    def get_release_group(self):
        return self.release_group

    def add_release_group(self, release_group_object):
        self.release_group.append(release_group_object)


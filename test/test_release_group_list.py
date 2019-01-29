__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import musicbrainz_api_porting
from musicbrainz_api_porting import ReleaseGroupList
import json

class TestReleaseGroupList(unittest.TestCase):

    def setUp(self):
        self.release_group_list = ReleaseGroupList.ReleaseGroupList(685)

    def test_get_count(self):
        assert self.release_group_list.get_count() == 685

    def test_get_release_group_json(self):
        print (self.release_group_list.to_json())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import musicbrainz_api_porting
from musicbrainz_api_porting import Artist
from musicbrainz_api_porting import ReleaseGroupList

import json

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist.Artist('65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab')
        self.release_group_list = ReleaseGroupList.ReleaseGroupList(685)

    def test_get_id(self):
        assert self.artist.get_id() == '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab'
        assert len(self.artist.get_release_group_list()) == 0
        assert self.artist.get_name() == None

    def test_set_artist(self):
        self.artist.set_name("Metallica")
        assert self.artist.get_name() == "Metallica"

    def test_add_release_group_list(self):
        self.artist.add_release_group_to_artist(self.release_group_list)
        assert len(self.artist.get_release_group_list()) == 1

    def test_get_artist_json(self):
        self.artist.set_name("Metallica")
        self.artist.add_release_group_to_artist(self.release_group_list)
        print (self.artist.to_json())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
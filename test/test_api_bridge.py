__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import FleskApp
from musicbrainz_api_porting import APIBridge

import json

class TestBridge(unittest.TestCase):

    Metallica = "65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"
    Coldplay = "cc197bad-dc9c-440d-a5b5-d52ba2e14234"


    def setUp(self):


        hostname = "musicbrainz.org"
        app = "python-musicbrainz-porting"
        version = "0.1"
        format = "xml"
        contact = "https://github.com/RobertaBtt/mb_api_porting"
        self.api_bridge = APIBridge.APIBridge(hostname,app, version, contact, format)

        # hostname, app, version, format='xml'):
    def test_get_artist_by_id(self):
        artist = self.api_bridge.get_artist_by_id("65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab")
        assert artist['artist']['type'] == 'Group'
        assert artist['artist']['name'] == 'Metallica'
        assert artist['artist']['begin-area']['name'] == "Los Angeles"

    def test_get_release_group(self):
        release_group = self.api_bridge.get_release_group(TestBridge.Metallica, 10)
        assert len(release_group['release-group-list']) == 10
        assert release_group['release-group-list'][0]['title'] == "Ride the Lightning"
        assert release_group['release-group-list'][0]['type'] == "Album"

    def test_get_release_group_type_album(self):
        release_group = self.api_bridge.get_release_group_album_type(TestBridge.Coldplay, 10)
        assert release_group['release-group-list'][0]['title'] == "A Rush of Blood to the Head"

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
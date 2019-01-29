__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import musicbrainz_api_porting
from musicbrainz_api_porting import APIBridge

import json

class TestBridge(unittest.TestCase):

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

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
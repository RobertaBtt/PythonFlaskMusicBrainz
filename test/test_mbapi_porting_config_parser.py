__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import MusicbrainzPortingConfig

class TestMusicbrainzConfigParser(unittest.TestCase):

    def test_get_app(self):
        app = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('app')
        assert app == "python-musicbrainz-porting"

    def test_get_app(self):
        app = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('version')
        assert app == "0.1"

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
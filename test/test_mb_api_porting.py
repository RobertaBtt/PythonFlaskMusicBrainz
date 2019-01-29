__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import musicbrainz_api_porting
import json

class TestServer(unittest.TestCase):

    def setUp(self):
        app = musicbrainz_api_porting.app
        app.config['TESTING'] = True
        self.baseURL = "http://localhost:5000"
        self.client = app.test_client()

        return app

    def test_get_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_get_home(self):
        response = self.client.get('/undefined')
        assert response.status_code == 404

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
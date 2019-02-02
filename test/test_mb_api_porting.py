__author__ = 'RobertaBtt'

import unittest
from musicbrainz_api_porting import FleskApp
import json

class TestServer(unittest.TestCase):

    def setUp(self):
        app = FleskApp.app
        app.config['TESTING'] = True
        self.baseURL = "http://localhost:5000"
        self.client = app.test_client()

        return app

    def test_get_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_undefined(self):
        response = self.client.get('/undefined')
        assert response.status_code == 404

    def test_release_group_artist(self):
        response = self.client.get('/releasegroup/65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab/')
        assert response.status_code == 200

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
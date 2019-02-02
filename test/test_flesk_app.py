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

    def test_get_last_twelve(self):
        limit = 12
        offset = 10
        response = self.client.get('/releasegroup/65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab/'+str(limit) +'/'+ str(offset))
        assert response.status_code == 200
        assert len(json.loads(response.get_data().decode('utf-8'))['release-group-list']) == 12
        assert json.loads(response.get_data().decode('utf-8'))['release-group-list'][2]['title'] == 'Lulu'

    def test_get_all(self):
        Maneskin = '3862342a-43c4-4cdb-8250-bfdbfb5e1419'
        response = self.client.get('/releasegroup/' + Maneskin + '/')
        assert response.status_code == 200
        assert len(json.loads(response.get_data().decode('utf-8'))['release-group-list']) == 4

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
__author__ = 'RobertaBtt'

import musicbrainzngs
import simplejson
import json

class APIBridge():
    def __init__(self, hostname, app, version,contact,  format='xml'):
        # https://musicbrainz.org/ws/2/

        musicbrainzngs.set_useragent(app, version, contact)

        # musicbrainzngs.set_useragent(app, version, contact=None)
        musicbrainzngs.set_hostname(hostname)
        musicbrainzngs.set_format(format)

    def get_artist_by_id(self, id):
        return musicbrainzngs.get_artist_by_id(id, includes=[], release_status=[], release_type=[])

    def get_release_group(self, artist_id, limit=None, offset=None):
        return musicbrainzngs.browse_release_groups(artist_id, None, [], [], limit, offset)

    def get_release_group_album_type(self, artist_id, limit=None, offset=None):
        return musicbrainzngs.browse_release_groups(artist_id, None, ['album'], [], limit, offset)



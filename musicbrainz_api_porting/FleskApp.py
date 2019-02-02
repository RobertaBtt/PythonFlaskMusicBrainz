__author__ = 'RobertaBtt'

from flask import Flask, json
from musicbrainz_api_porting import MusicbrainzPortingConfig
from musicbrainz_api_porting import APIBridge

app = Flask(__name__)



@app.route("/")
def home():
    response = app.response_class(
        response=json.dumps(dict()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/releasegroup/<artistid>/")
def release_group_artist_no_limit(artistid):

    api_bridge = APIBridge.APIBridge(_get_hostname(), _get_app_name(), _get_version(), _get_contact(), _get_format())

    result = api_bridge.get_release_group(artistid, None, None)

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/releasegroup/<artistid>/<limit>/<offset>")
def release_group_artist(artistid, limit, offset):

    api_bridge = APIBridge.APIBridge(_get_hostname(), _get_app_name(), _get_version(), _get_contact(), _get_format())

    result = api_bridge.get_release_group(artistid, limit, offset)

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

staticmethod
def _get_hostname():
    return MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('hostname')


staticmethod
def _get_app_name():
    return MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('app')

staticmethod
def _get_version():
    return MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('version')


staticmethod
def _get_format():
    return MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('format')

staticmethod
def _get_contact():
    return MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('contact')

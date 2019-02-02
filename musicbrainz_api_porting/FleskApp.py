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
def release_group_artist(artistid):

    hostname = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('hostname')
    app_string = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('app')
    version = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('version')
    format = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('format')
    contact = MusicbrainzPortingConfig.MusicbrainzPortingConfig.get_confi_by_key('contact')

    api_bridge = APIBridge.APIBridge(hostname, app_string, version, contact, format)

    result = api_bridge.get_release_group(artistid, 1)
    print (result)

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

# MusicBrainz API Porting

_Working with Musicbrainz api Xml version ([MusicBrainz Xml API Version 2](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2))
 in order to retrieve JSON format._



![logo](https://staticbrainz.org/MB/images/layout/header-logo-791fb3f5ca.svg)



Instructions:

```
mkdir mb_api_porting
```
 
 
``` 
cd mb_api_porting

``` 

```
virtualenv -p /usr/bin/python3.5 MB_API_PORTING_ENV

```

Create the virtual env ONCE

```
source MB_API_PORTING_ENV/bin/activate
```


And you will find yourself in the virtual environment, ready to get the corret dependencies
without influencing other python installation and environments.



**Install the requirements for this virtual env for this project:**

```
pip install -r requirements.txt
```


---

To deactivate the virtual env:

```
deactivate
```



To run the Application server:

From the directory *mb_api_porting*
run:

```
FLASK_APP=musicbrainz_api_porting/FleskApp.py flask run
```

And then visit http://127.0.0.1:5000/  (depending on your local config file, that you are free to change)

To retrieve reliese of an artist use:
http://127.0.0.1:5000/artistid

To use limit and offset:
http://127.0.0.1:5000/artist_id/limit/offset

example: http://localhost:5000/releasegroup/3862342a-43c4-4cdb-8250-bfdbfb5e1419/4/0
limit of 4 release-group starting by 0

artist id is an uuid sequence that identify an artist in the MusicBrainz database



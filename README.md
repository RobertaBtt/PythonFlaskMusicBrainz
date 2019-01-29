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

```
source MB_API_PORTING_ENV/bin/activate
```

And you will find yourself in the virtual environment, ready to get the corret dependencies
without influencing other python installation and environments.


To deactivate the virtual env:

```
deactivate
```



To run the Application server:

From the directory *mb_api_porting*
run:

```
FLASK_APP=musicbrainz_api_porting/musicbrainz_api_porting.py flask run
```

And then visit http://127.0.0.1:5000/  (depending on your local config file, that you are free to change)

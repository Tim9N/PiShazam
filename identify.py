
"""
This is a demo program which implements ACRCloud Identify Protocol V1 with the third party library "requests".
We recomment you implement your own app with "requests" too.
You can install this python library by:
1) sudo easy_install requests 
2) sudo pip install requests
"""

import base64
import hashlib
import hmac
import os
import sys
import time

import requests

import spotifyapi as s

'''
Replace "###...###" below with your project's host, access_key and access_secret.
'''
access_key = "b3d2281b54b82efd4f104dc269b03fb6"
access_secret = "WgLDJ1Cv59IiEZJBdtv91ZI0T8R4AKiFSRQrtDdF"
requrl = "https://identify-us-west-2.acrcloud.com/v1/identify"

http_method = "POST"
http_uri = "/v1/identify"
# default is "fingerprint", it's for recognizing fingerprint,
# if you want to identify audio, please change data_type="audio"
data_type = "audio"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
    timestamp)

sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                 digestmod=hashlib.sha1).digest()).decode('ascii')

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
# File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better
f = open(sys.argv[1], "rb")
sample_bytes = os.path.getsize(sys.argv[1])

files = [
    ('sample', ('test.mp3', open(sys.argv[1], 'rb'), 'audio/mpeg'))
]
data = {'access_key': access_key,
        'sample_bytes': sample_bytes,
        'timestamp': str(timestamp),
        'signature': sign,
        'data_type': data_type,
        "signature_version": signature_version}

r = requests.post(requrl, files=files, data=data)
r.encoding = "utf-8"

r = r.json()

if (r['status']['code'] == 0):
    title = r['metadata']['music'][0]['title']
    artist = r['metadata']['music'][0]['artists'][0]['name']
    album = r['metadata']['music'][0]['album']['name']
    print("Title: ", title)
    print("Artist: ", artist)
    print("Album: ", album)


    spotify_album_id = r['metadata']['music'][0]['external_metadata']['spotify']['album']['id']
    spotify_artist_id = r['metadata']['music'][0]['external_metadata']['spotify']['artists'][0]['id']
    spotify_track_id = r['metadata']['music'][0]['external_metadata']['spotify']['track']['id']

    print("Spotify Album ID: ", spotify_album_id)
    print("Spotify Artist ID: ", spotify_artist_id)
    print("Spotify Track ID: ", spotify_track_id)

    isrc = s.getIsrc(spotify_track_id)
    print("ISRC: ", isrc)

    lyrics = s.getLyrics(isrc)
    print("Lyrics: ", lyrics)

    s.getImage(spotify_album_id, title)


else:
    print("Error: ", r['status']['msg'])



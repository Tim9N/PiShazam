import requests
import os

spotify_client_id = 'acede88d55e44fadb5c65ba81926f067'
spotify_secret = '3f5e05741dae4006b7f93e4d8c620b71'

def getToken():
    """
    Get a token for the Spotify API.
    """
    data = "grant_type=client_credentials&client_id=" + spotify_client_id + "&client_secret=" + spotify_secret
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    response = response.json()
    if ('error' in response):
        print('Error getting token')
        print(response)
        return
    
    access_token = response['access_token']

    return access_token

def getImage(albumID, songName):
    """
    Get the album art for the album with the given ID.
    """
    url = 'https://api.spotify.com/v1/albums/' + albumID

    token = getToken()
    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    imageUrl = data['images'][0]['url']

    f = open(songName + '.jpg','wb')
    f.write(requests.get(imageUrl).content)
    f.close()

def getLyrics(isrc):
    """
    Get the lyrics for the song with the given ID.
    """
    apikey = 'e68c122c330449508515fdc012b2d33f'
    # use the IRSC to get lyrics from Musixmatch
    url = 'https://api.musixmatch.com/ws/1.1/track.get?track_isrc=' + isrc + '&apikey=' + apikey

    #track.get?track_irsc=' + irsc + '&apikey=e68c122c330449508515fdc012b2d33f'

    response = requests.get(url)
    data = response.json()

    track_id = data['message']['body']['track']['track_id']

    url = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id=' + str(track_id) + '&apikey=' + apikey

    response = requests.get(url)
    data = response.json()

    lyrics = data['message']['body']['lyrics']['lyrics_body']
    return lyrics

def getIsrc(trackID):
    """
    Get the IRSC for the song with the given ID.
    """
    url = 'https://api.spotify.com/v1/tracks/' + trackID

    token = getToken()
    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    isrc = data['external_ids']['isrc']
    return isrc

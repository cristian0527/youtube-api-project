import requests
import os

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
})

auth_response_data = auth_response.json()
#print(auth_response_data)
access_token = auth_response_data['access_token']
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
#3BUc2A0MJ53FHwiy3eohBt?si=dc7adc64e11a4c09 track id
print(r.json())
print("Status Code: ", r.status_code)

#sudo NANO/vim BOTTOM
#export SPOTIFY_CLIENT_ID=clientidcode
#export SPOTIFY_CLIENT_SECRET=client_secret
#now exit nano

#source -/.bashrc
#now change client id client secert with os.environ.get('SPOTIFY_CLIENT_...)

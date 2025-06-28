import requests

API_KEY = os.environ.get('YOUTUBE_API_KEY')

search = input('Enter what you want to search: ')

url = 'https://www.googleapis.com/youtube/v3/search'

#parameters from youtube 
params = {
  'part': 'snippet',
  'q': search,
  'type': 'video',
  'maxResults': 5,
  'key': YOUTUBE_API_KEY
}

response = requests.get(url, params=params)
data = response.json()

print(data)
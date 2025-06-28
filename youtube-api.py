import requests

YOUTUBE_API_KEY = 'AIzaSyAZAOwH88SEB-6B6KkhUGhMX6jxu_tR7CM'

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
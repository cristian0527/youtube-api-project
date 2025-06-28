import requests
import json
import os

API_KEY = os.environ.get('YOUTUBE_API_KEY')
print(f"API_KEY loaded: {bool(API_KEY)}")

search = input('Enter what you want to search: ')
max_results = input('How many results do you want to see? (1-50): ')

try:
  max_results = int(max_results)
  if max_results < 1 or max_results > 50:
    raise ValueError
except ValueError:
  print("Invalid! Will default to default max results: 5")
  max_results = 5

url = 'https://www.googleapis.com/youtube/v3/search'

#parameters from youtube 
params = {
  'part': 'snippet',
  'q': search,
  'type': 'video',
  'maxResults': max_results,
  'key': API_KEY
}

response = requests.get(url, params=params)
data = response.json()

#print(json.dumps(data, indent=2)) 
#'items' json key: returns info needed
#print(json.dumps(items, indent=2))

items = data.get('items', []) #if dne, then returns None, so if we add the condtion after the key, we get a return empty string if dne
for item in items:
  snippet = item.get('snippet', {})
  title = snippet.get('title')
  channel = snippet.get('channelTitle')
  video_id = item['id'].get("videoId")

  print(f"🎥 {title} - {channel}")
  print(f"https://www.youtube.com/watch?v={video_id}", "\n")
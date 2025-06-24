import requests

text_input = input("Enter a text to analyze: ")

url = "https://text-processing.com/api/sentiment/"
myobj = {'text': text_input}
response = requests.post(url, data=myobj)
#print(response.json())

print("Status Code: ", response.status_code)
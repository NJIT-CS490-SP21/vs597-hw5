#from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import requests
import os
import json

#app = Flask(__name__)
load_dotenv(find_dotenv()) 
auth_url = "https://accounts.spotify.com/api/token"

response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
})

data = response.json()
access_token = data['access_token']

browse_url = "https://api.spotify.com/v1/browse/new-releases?country=US&limit=10"
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

songs = requests.get(browse_url, headers=headers)
songs = songs.json()

for i in range(0,10):
    print(songs['albums']['items'][i]['name']), songs['albums']['items'][i]['artists'])
#[i]['artists']['name'])
# @app.route('/')
# def topTen():
#     print("App started")
# s_items = s.items()
# first_ten = list(s_items)[:11]
# print("10 new releases: " + str(first_ten))

# app.run(
#     port=int(os.getenv('PORT', 8080)),
#     host=os.getenv('IP', '0.0.0.0'),
#     debug=True
# )
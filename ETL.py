# cInput: Asks for user own API
# Spotify API connection
# variable that receives the data from cInput
from sqlite3.dbapi2 import Timestamp
import sqlalchemy
import requests
import json
import pandas as pd
from sqlalchemy.orm import sessionmaker
import datetime
import time
import sqlite3


print("----------------------------------------------------------------")
time.sleep(1);
print("This small software was designed merely for learning purposes!")
time.sleep(1);
print("----------------------------------------------------------------");

time.sleep(1.5);

DATABASE_DIR = "sqlite:///played_tracks.sqlite"
USER_ID = ""# "What is your Spotify User ID"
API_TOKEN = "" # "What is the Authorization Token"

if __name__ == "__main__":
   
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token = API_TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time = yesterday_unix_timestamp), headers = headers)

    data = r.json()

    print(data)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artists_name", "played_at_list", "timestamps"])
    
    print(song_df)
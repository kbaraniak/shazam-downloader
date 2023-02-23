from libs.music_download import download_music
from libs.read_csv import csv_to_list
import os

def list_files_csv():
    listcsv = []
    for x in os.listdir("list/"):
        if x.endswith(".csv"):
            listcsv.append(x)
    return listcsv

csv_files = list_files_csv()

for csvfile in csv_files:
    listdir = "list/" + csvfile
    list_songs = csv_to_list(listdir)
    for song in list_songs:
        print("Downloading: ", song)
        download_music(song)

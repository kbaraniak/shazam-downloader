from libs.music_download import download_music
from libs.read_csv import csv_to_list
import os, sys

# Required steps
try:
    os.listdir("list")
    step1 = True
except:
    exit("Directory 'list' not exists ")

if(step1):
    if(len(os.listdir("list/")) == 0):
        exit("Directory 'list' is empty")
    else:
        if not any(fname.endswith('.csv') for fname in os.listdir('list/')):
            exit("No found 'csv' files on dir")


# Optional arguments
if(len(sys.argv) > 1):
    if(sys.argv[1] == "--disable-sort"):
        optionalArg = "nosort"
    else:
        optionalArg = ""
else:
    optionalArg = ""

# Main code
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
        download_music(song, optionalArg)


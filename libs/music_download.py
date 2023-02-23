import json
import yt_dlp

# Predefined Variables
# year = ""
# month = ""

def __hook(d):
    if d['status'] == 'finished':
        filename = d['filename'].split(".")[0]
        print(" [saved on", filename + ".mp3]") # Here you will see the PATH where was saved.
        print("———————————————————————————————")

def __predef_conf(optArg=""):
    conf = { 
        'format': 'bestaudio/best',
        'outtmpl': f'music2/{optArg}/%(title)s.%(ext)s', # You can change the PATH as you want
        'download_archive': 'downloaded.txt',
        'noplaylist': True,   
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [__hook]
    }
    return conf

def __client(video_url, ydl_opts=__predef_conf("nodate"), download=False):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         return ydl.extract_info(video_url, download=download)

def __gen_config(date):
    if(date == 0):
        ydl_opts = __predef_conf()
    else:
        ydl_opts = { 
            'format': 'bestaudio/best',
            'outtmpl': f'music2/{date[0]}/{date[1]}/%(title)s.%(ext)s', # You can change the PATH as you want
            'download_archive': 'downloaded.txt',
            'noplaylist': True,   
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [__hook]
        }
    return ydl_opts

# Only for Debug

# song = '1,"Miley Cyrus","Flowers"'
# result = json.dumps(client(f'ytsearch:{song}', download=True))
# print_json(result)

def __unpack_date(date):
    if(date == "downloaded"):
        print("Skipping [music downloaded]")
        print("———————————————————————————————")
    elif(date == "nodate"):
        print(f"No date published")
    elif(date == "nosort"):
        return 0
    else:
        print(f"Published on: {date}")
    date_music = []
    if (len(date) > 1):
        year = date[0:4]
        month = date[4:6]
        date_music = [year, month]
        return date_music
    else:
        return ["nodate", ""]

def __download_music(query, optionalArg=""):
    try:
        result = json.dumps(__client(f'ytsearch:{query}', download=False))
        download = True
    except:
        print("Sorry, song no available for download")          
        download = False
    if(download):
        parseData = json.loads(result)
        try:
            releasedate = parseData["entries"][0]["release_date"]
        except:
            try:
                releasedate = parseData["entries"][0]["upload_date"]   
            except:
                if(len(parseData["entries"]) > 1):
                    releasedate = "nodate"
                else:
                    releasedate = "downloaded"
        if(optionalArg == "nosort"):
            releasedate = "nosort"
        new_config = __gen_config(__unpack_date(releasedate))
        __client(f'ytsearch:{query}', new_config, download=True)


def download_music(query, optionalArg=""):
    try:
        __download_music(query, optionalArg)
    except KeyboardInterrupt:
        exit("\nCanceled by user")
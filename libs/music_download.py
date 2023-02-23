# import json
# from rich import print_json
import yt_dlp # pip install yt_dlp

def __hook(d):
    if d['status'] == 'finished':
        filename = d['filename']
        print(filename) # Here you will see the PATH where was saved.

def __client(video_url, download=False):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         return ydl.extract_info(video_url, download=download)

ydl_opts = { 
        'format': 'bestaudio/best',
        'outtmpl': 'music/%(title)s.%(ext)s', # You can change the PATH as you want
        'download_archive': 'downloaded.txt',
        'ffmpeg_location': 'C://ffmpeg//bin',
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

song = '1,"Miley Cyrus","Flowers"'

# result = json.dumps(__client(f'ytsearch:{song}', download=True))

def download_music(query):
    __client(f'ytsearch:{query}', download=True)
from __future__ import unicode_literals
import youtube_dl

quality=input("Quality of the video(best/worst): ")

playlist=input("Do you want to download a playlist(Y/N): ")
if playlist=='Y' or playlist=='y':
    start=1
    end=-1
    try:
        start=int(input('Playlist starting number: '))
    except:
        pass
    try:
        end=int(input("Playlist ending number: "))
    except:
        pass
    ydl_opts = {'format': quality,'playliststart':start,'playlistend':end,'outtmpl':'%(playlist_index)s%(title)s.%(ext)s'}

else:
    ydl_opts = {'format' : quality,'noplaylist':1}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input('Enter the url: ')])

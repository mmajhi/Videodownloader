from __future__ import unicode_literals
import youtube_dl
import traceback

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download_mp3():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([input('Enter the youtube url: ')])
        except:
            print traceback.format_exc()


def download_webm():
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([input('Enter the youtube url: ')])
        except:
            print traceback.format_exc()


if __name__ == '__main__':
    download_webm()
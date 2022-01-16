import pytube
from pytube import YouTube
import requests

url = input('Enter video url: ')
try:
    yt = YouTube(url)
    print('\nVideo found \nTitle: ', yt.title, end='\n\n')
    yt.streams.filter(only_audio=False, only_video=False, progressive=True)
    chosen_vid = yt.streams.get_highest_resolution()
    dl = 'Downloading...'
    print(dl, end='')
    chosen_vid.download('videos')
    for i in range(len(dl)):
        print('', end='\b')
    print('Success')
except pytube.exceptions.RegexMatchError as exception:
    print('\nVideo not found')

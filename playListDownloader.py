
from pytube import Playlist
from pytube import YouTube

p = Playlist(
    'https://www.youtube.com/playlist?list=PLTuxjD1pItJXiUZi2GnvKEBoDAx7DYwEP')
urlList = []
print(f'Downloading: {p.title}')

# set video_urls arry size to download the number of videos in playlist
for url in p.video_urls[:32]:
    urlList.append(url)

# unComment the following line to skip downloaded videos in the array
#del urlList[0:13]

for url in urlList:
    try:

        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(url)
    except:
        # to handle exception
        print("Connection Error")

    stream = yt.streams.filter(progressive=False)
    stream = yt.streams.get_by_itag(140)
    try:
        print("Downloading: " + stream.default_filename)
        stream.download()

    except Exception as e:
        print(e)
print('Task Completed!')

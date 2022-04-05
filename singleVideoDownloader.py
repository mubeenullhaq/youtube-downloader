
from pytube import YouTube

# object creation using YouTube
# which was imported in the beginning
yt = YouTube(
    "https://www.youtube.com/watch?v=Q533ZU8EccI&list=PLY_KlBDsZD4UPonuByS2zSiIaqtHfM9cr&index=11")

stream = yt.streams.filter(progressive=False)
stream = yt.streams.get_by_itag(140)
try:
    print("Downloading: "+stream.default_filename)
    stream.download()

except Exception as e:
    print(e)

print('Task Completed!')

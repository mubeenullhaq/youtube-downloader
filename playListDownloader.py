import yt_dlp

# Playlist URL
playlist_url = 'https://www.youtube.com/watch?v=XTp5jaRU3Ws&list=PLO7-VO1D0_6NYoMAN0XncJu4tvibirSmN'

# Configure yt-dlp options for MP3 download
ydl_opts = {
    'format': 'bestaudio/best',  # Download best audio quality
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Extract audio
        'preferredcodec': 'mp3',      # Convert to MP3
        'preferredquality': '192',    # Audio quality (192 kbps)
    }],
    'outtmpl': '%(title)s.%(ext)s',   # Output filename template
    'quiet': False,                   # Show progress
    'no_warnings': False,             # Show warnings
}

print(f'Starting download of playlist...')

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download entire playlist as MP3
        ydl.download([playlist_url])
    print('Task Completed! All videos downloaded as MP3 files.')
except Exception as e:
    print(f'Error: {e}')

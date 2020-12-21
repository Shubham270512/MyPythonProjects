import pytube
import re
url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'
m=re.match(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",url)
if m:
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('/Downloads')
else:
    print("Invalid url")


#encoding=utf8
from pydub.utils import mediainfo
song = mediainfo("data/1.wav")
print song

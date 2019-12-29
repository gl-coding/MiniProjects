#encoding=utf8
from pydub import AudioSegment

# 音频文件路径
input_path = "data/1.wav"
output_path = "data/3.mp3"

# 读取音频文件，设置采样率<default=44100>
song = AudioSegment.from_wav(input_path)
song.export(output_path, format='mp3')

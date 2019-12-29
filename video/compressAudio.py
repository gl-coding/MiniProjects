#encoding=utf8
from pydub import AudioSegment


# 读取音频文件，设置采样率<default=44100>
song = AudioSegment.from_wav(input_path)
song = song.set_frame_rate(11025)
# 按32k的bitrate导出文件到指定路径,这里是直接覆盖原文件
song.export(output_path, format='wav', bitrate='32k')

# 音频文件路径
input_path = "data/1.wav"
output_path = "data/3.wav"

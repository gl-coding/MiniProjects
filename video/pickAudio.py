#encoding=utf8
from moviepy.editor import *
from pydub import AudioSegment

def video_to_audio(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    #mp3是有损格式，wav是无损格式，按需选择
    audio.write_audiofile(output_path)

#video_to_audio("data/1.mkv", "data/1.mp3")

def compress_audio(input_path, output_path):
    # 读取音频文件，设置采样率<default=44100>
    song = AudioSegment.from_wav(input_path)
    song = song.set_frame_rate(11025)
    # 按32k的bitrate导出文件到指定路径,这里是直接覆盖原文件
    song.export(output_path, format='wav', bitrate='64k')

#compress_audio("data/1.wav", "data/1_com.wav")

def get_audio_seg(input_path, output_path, start=0, end=-1):
    start_int = int(start*1000)
    end_int = end if end == -1 else int(end*1000)

    mp3 = AudioSegment.from_wav(input_path) # 打开mp3文件
    mp3[start_int:end_int].export(output_path, format="wav") # 切割前17.5秒并覆盖保存

#get_audio_seg("data/1.wav", "data/1_seg.wav", 17.5, 20)

if __name__ == "__main__":
    #video_to_audio("data/1.mkv", "data/1.mp3")
    print "main"

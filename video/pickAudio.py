#encoding=utf8
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from moviepy.editor import *
from pydub import AudioSegment

base = "/Users/guolei08/Documents/"

def rename_strategy(name, stype=""):
    res = ""
    if stype == "sanguo":
        res = name.split(".")[-2].replace("EP", "")
        return res
    elif stype == "xiyouji":
        res = name.split("/")[-1].replace(".mpg", "")
        return res
    elif stype == "zxc":
        res = name.split("/")[-1].replace(".mkv", "")
        return res
    elif stype == "kangxi":
        res = name.split("/")[-1]
        idx = res.find("Dynasty")
        res = res[idx+9:idx+11]
        return res
    elif stype == "shuihu":
        #res = name.split("/")[-1].replace("水浒传", "").replace(".mkv", "")
        res = name.split("/")[-1].replace("水浒传", "").replace(".mpg", "")
        return res
    elif stype == "hulu":
        res = name.split("/")[-1].replace(".rmvb", "").replace("葫芦兄弟", "")
        return res
    return res

def video_to_audio(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    #mp3是有损格式，wav是无损格式，按需选择
    audio.write_audiofile(output_path)

#video_to_audio("data/1.mkv", "data/1.mp3")

def trans_videos(dirname, convert=True):
    src = base + "video/" + dirname
    tar = "data_audio/" + dirname
    for root, dirs, files in os.walk(src):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            filename = os.path.join(root, f)
            #tar_name  = rename_strategy(filename, "sanguo")
            #tar_name  = rename_strategy(filename, "xiyouji")
            #tar_name  = rename_strategy(filename, "zxc")
            #tar_name  = rename_strategy(filename, "kangxi")
            #tar_name  = rename_strategy(filename, "shuihu")
            tar_name  = rename_strategy(filename, dirname)
            new  = tar + os.sep + tar_name + ".mp3"
            print filename, new
            #print tar
            if convert:
                video_to_audio(filename, new)

#trans_videos(base + "video/liangjian", "data_audio/liangjian")
#trans_videos(base + "video/sanguo", "data_audio/sanguo")
#trans_videos(base + "video/xiyouji", "data_audio/xiyouji")
#trans_videos(base + "video/zhouxingchi", "data_audio/zhouxingchi")
#trans_videos(base + "video/kangxi", "data_audio/kangxi")
#trans_videos("shuihu")
trans_videos("hulu")

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

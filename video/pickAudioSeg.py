#encoding=utf8
from pydub import AudioSegment

input_file = "data/1.mp3"
output_file = "data/2.mp3"

start = 17.5
start_int = int(start*1000)

end = 20
end_int = int(end*1000)

mp3 = AudioSegment.from_wav(input_file) # 打开mp3文件
mp3[start_int:end_int].export(output_file, format="wav") # 切割前17.5秒并覆盖保存

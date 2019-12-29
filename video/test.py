import os
import pickAudio as pa

dir_path = "/Users/guolei08/Documents/liangjian/"

for d in os.listdir(dir_path):
    name = d.split(".")[0]
    input_path = dir_path + name + ".mkv"
    output_path = dir_path + name + ".mp3"
    print file_path

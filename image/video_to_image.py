#encoding=utf8
# 导入cv2模块
import cv2
# 利用VideoCapture捕获视频，这里使用本地视频
video_path = "/Users/guolei08/Downloads/1.mp4"
images_path = "/Users/guolei08/Downloads/images"

cap = cv2.VideoCapture(video_path)  # 要分解的视频的路径
flag = 0

if cap.isOpened():
    flag = 1
else:
    flag = 0

i = 0
imgPath = ""

if flag == 1:
    while True:
        ret, frame = cap.read()  # 读取视频帧
        if ret == False:  # 判断是否读取成功
            break
        i += 1  # 使用i为图片命名
        imgPath = images_path + "/%s.jpg" % str(i)  # 存储图片的路径
        cv2.imwrite(imgPath, frame)  # 将提取的视频帧存储进imgPath

print("finish!")  # 提取结束，打印finish

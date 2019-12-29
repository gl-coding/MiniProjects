#encoding=utf8
import cv2
print(cv2.__version__)
videoCapture = cv2.VideoCapture('gogo.mp4')
 
fps = 120 #保存视频的帧率
size = (1920,1080) #保存视频的大小
 
videoWriter =cv2.VideoWriter('haha.mp4',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size)
i = 0
 
while True:
    success,frame = videoCapture.read()
    if success:
        i += 1
        print('i = ',i)
        #if(i>=3930 and i <= 5250):
        videoWriter.write(frame)
    else:
        print('end')   
        break     

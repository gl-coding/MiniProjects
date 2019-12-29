#encoding=utf8
import cv2

input_file = "data/1.mkv"
output_file = "data/1.jpg"

video_filename = 'data/1.mkv'
videoCap = cv2.VideoCapture(video_filename)

# 帧频
fps = videoCap.get(cv2.CAP_PROP_FPS)
# 视频总帧数
total_frames = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
# 图像尺寸
image_size = (int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)))

print(fps)
print(total_frames)
print(image_size)

for i in range(14000):
    sucess, frame = videoCap.read()

from PIL import Image
img = Image.fromarray(frame)
img.show()
img.save(output_file)

im = frame[:, :, 0]
im = im[595:670, :]     #确定字幕的范围，注意不同的视频文件剪切的索引值不同
img = Image.fromarray(im)
img.show()
#img.save("1.jpg")

thresh = 220
_, im = cv2.threshold(im, thresh, 255, cv2.THRESH_BINARY)
img = Image.fromarray(im)
img.show()
#img.save("1.jpg")

print((im ** 2).sum() / im.size * 100)

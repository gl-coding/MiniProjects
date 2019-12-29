#encoding=utf8
from PIL import Image
import numpy as np
import sys
import os
import shutil
 
def convert_image(image_path, out_image_path):
    a = np.asarray(Image.open(image_path).convert('L')).astype('float')
 
    depth = 10.                        # (0-100)
    grad = np.gradient(a)              #取图像灰度的梯度值
    grad_x, grad_y =grad               #分别取横纵图像梯度值
    grad_x = grad_x*depth/100.
    grad_y = grad_y*depth/100.
    A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
    uni_x = grad_x/A
    uni_y = grad_y/A
    uni_z = 1./A
 
    vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
    vec_az = np.pi/4.                    # 光源的方位角度，弧度值
    dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
    dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
    dz = np.sin(vec_el)                  #光源对z 轴的影响
 
    b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
    b = b.clip(0,255)
 
    im = Image.fromarray(b.astype('uint8'))      #重构图像

    im.save(out_image_path)

def get_image_rewrite_path(image_path):
    split_res   = image_path.split("/")
    tail        = split_res[-1]
    dirname     = split_res[-2]
    tardir      = dirname + "_rewrite"

    out_image_dir_base = "/".join(split_res[:-2]) + "/" + tardir
    out_image_path = out_image_dir_base + "/" + tail

    return out_image_path

if __name__ == "__main__":
    images_path = sys.argv[1]
    split_res   = images_path.split("/")
    dirname     = split_res[-1]
    tardir      = dirname + "_rewrite"

    out_image_dir_base = "/".join(split_res[:-1]) + "/" + tardir

    if os.path.exists(out_image_dir_base):
        shutil.rmtree(out_image_dir_base)
    print out_image_dir_base
    os.mkdir(out_image_dir_base)

    for i in os.listdir(images_path):
        if len(i.split(".")[0]) == 0:
            continue
        image_path = os.path.join(images_path,i)  #拼接绝对路径
        #if os.path.isdir(path2):      #判断如果是文件夹,调用本身
        #    func(path2)
        #else:
            #print(i)
        image_path_new = get_image_rewrite_path(image_path)
        print image_path_new
        convert_image(image_path, image_path_new)

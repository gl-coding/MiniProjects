#https://blog.csdn.net/ucsheep/article/details/82788067
import pickle
 
from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking, to_fxfy
 
 
# 加载clip，截取一个卓别林电影的6‘51-7’01之间的片段
clip = VideoFileClip("../../videos/chaplin.mp4").subclip((6,51.7),(7,01.3))
 
# 手动跟踪标记头部
 
# 下面的三行代码，手动跟踪，然后把结果保存进文件，应该在一次运行之后就完成量跟踪标记
# 注意：我们保存的格式是一个(ti,xi,yi)list，不是函数fx和fy
 
#txy, (fx,fy) = manual_tracking(clip, fps=6)
#with open("../../chaplin_txy.dat",'w+') as f:
#    pickle.dump(txy)
 
 
 
# 已经完成手动跟踪人脸并标记的情况下
# fx(t),fy(t)的形式加载跟踪标记的数据
 
with open("../../chaplin_txy.dat",'r') as f:
    fx,fy = to_fxfy( pickle.load(f) )
 
 
# 在clip中，模糊卓别林的头部
 
clip_blurred = clip.fx( vfx.headblur, fx, fy, 25)
 
 
# 生成文本，灰色背景
 
txt = TextClip("Hey you ! \n You're blurry!", color='grey70',
               size = clip.size, bg_color='grey20',
               font = "Century-Schoolbook-Italic", fontsize=40)
               
               
# 把卓别林的vedio clip和TextClip连接起来，添加audio clip
 
final = concatenate_videoclips([clip_blurred,txt.set_duration(3)]).\
          set_audio(clip.audio)
 
# 将比特率修改为3000k是为了画面不至于太丑
 
final.write_videofile('../../blurredChaplin.avi', bitrate="3000k")

import os
from pip._internal.utils.misc import get_installed_distributions

# 安装依赖项
d = os.path.dirname(__file__) if '_file_' in locals() else os.getcwd()
installed_packages_list = [i.key for i in get_installed_distributions()]
requirements = open(os.path.join(d, 'requirements.txt')).read()
if requirements:
  req_list = requirements.split('\n')
  result = all(ele in installed_packages_list for ele in req_list)
  if not result:
    os.system('pip install -r requirements.txt --user')
  else:
      pass

# 安装第三方库
from PIL import Image
import numpy as np

out_pic = 'sketch.png'          #生成的图片名称
if os.path.exists(out_pic):
  os.system('rm' + out_pic)

# 检测用户上传的图片
imgs = [f for f in os.listdir('.') if f.split('.')[1] in ['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG']]      #上传图片的格式
if not imgs:
  print("请点击左侧目录下方上传图片按钮，上传一张图片")
else:
  if len(imgs) == 1:
    im = imgs[0]
  else:
    for idx, img in enumerate(imgs):
      print(f"{idx}:  {img} ")
    idx = int(input("请输入图片编号："))
    im = imgs[idx]
  a = np.asarray(Image.open(im).convert('L')).astype('float')
  depth = 10.       # (0-100)
  grad = np.gradient(a)
  grad_x, grad_y = grad
  grad_x = grad_x * depth / 100.
  grad_y = grad_y * depth / 100.
  A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
  uni_x = grad_x / A
  uni_y = grad_y / A
  uni_z = 1. / A

  vec_el = np.pi / 2.2
  vec_az = np.pi / 4.
  dx = np.cos(vec_el) * np.cos(vec_az)
  dy = np.cos(vec_el) * np.sin(vec_az)
  dz = np.sin(vec_el)

  b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
  b = b.clip(0, 255)

  im = Image.fromarray(b.astype('uint8'))
  im.save(out_pic)
  print("转换成功，点击左侧目录，找到‘sketch.png’,打开预览吧！")

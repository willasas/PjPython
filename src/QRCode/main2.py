from captcha.image import ImageCaptcha
import random
import string
# captcha库实现随机生成图片二维码验证

chr_all = string.ascii_letters + string.digits
chr_4 = ''.join(random.sample(chr_all, 4))
image = ImageCaptcha().generate_image(chr_4)
image.save('./%s.jpg' % chr_4)

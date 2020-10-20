import gvcode

# gvcode库实现随机生成图片二维码验证

s, v = gvcode.generate()
s.save('./%s.jpg' % v)

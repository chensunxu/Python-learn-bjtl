import pytesseract as pt

from PIL import Image

image = Image.open("/home/dz/桌面/1.jpg")

# 调用pytesseract，吧图片转成文字
# 返回结果就是转换后的结果
text = pt.image_to_string(image)
print(text)

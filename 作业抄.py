import os
from PIL import Image
from PIL import ImageEnhance

base_dir='.'
files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]

def changecolor(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
                r,g,b=image.getpixel((x,y))
                if r>230 and g>230 and b>230:
                    image.putpixel((x,y),(250,249,222))

for s in files:
    if s[-3:]=='jpg':

        img_01 = Image.open(s)
        img_01 = img_01.convert("L")
        contrast = ImageEnhance.Contrast(img_01)
        img_01 = contrast.enhance(2.5)
        brirghtness=ImageEnhance.Brightness(img_01)
        img_01 = brirghtness.enhance(2.5)
        img_01=img_01.resize((img_01.size[0],int(0.75*img_01.size[0])))
        img_01 = img_01.convert("RGB")
        changecolor(img_01)
        img_01.save('.\\product\\'+s[2:-4]+"_L.jpg")
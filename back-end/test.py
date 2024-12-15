from glob import glob
import os

img_path = os.path.join("D:\\img", "*.jpg")
imgs = glob(img_path)
for i in range(len(imgs)):
        img = imgs[i]
        img = os.path.basename(img)
        imgs[i] = img
print(imgs)

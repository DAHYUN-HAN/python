import shutil
import os
from tqdm import tqdm

# shutil.copyfile(original_image, copy_image)

image_list = os.listdir("D:/원본 이미지/")
for image in tqdm(image_list) :
    shutil.copyfile("D:/원본 이미지/" + image, "D:/복사 이미지/" + image)
    

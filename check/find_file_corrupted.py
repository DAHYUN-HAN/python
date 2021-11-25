from PIL import Image, UnidentifiedImageError
import os
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = 933120000

error_list = []
root_dir = "D:/test/"
for (root, dirs, files) in os.walk(root_dir):
    if len(files) > 0:
        for file_name in tqdm(files):
            try :
                Image.open("{}/{}".format(root, file_name))
            except UnidentifiedImageError:
                print("{}/{}".format(root, file_name))
                error_list.append("{}/{}".format(root, file_name))

with open("error_list.txt", 'w', encoding = 'utf-8') as file:
    for line in error_list :
        file.write(line + '\n')
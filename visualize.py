import cv2
from PIL import Image
import numpy as np
import glob
from tqdm import tqdm

image_files = glob.glob("afaf_mdian_test/*.png") ## mask 이미지 경로

for file in tqdm(image_files):
    img = cv2.imread(file)
    img_array = np.asarray(img)

    for i in range(len(img_array)):
        for j in range(len(img_array[0])):
            if img_array[i][j][0]==1:
                img_array[i][j][0] =255
            elif img_array[i][j][0]==2:
                img_array[i][j][1] = 255
            elif img_array[i][j][0]==3:
                img_array[i][j][2] = 255
    img_pil = Image.fromarray(img_array)
    img_pil.save("afaf_mdian_test/"+"a"+file[-8:]) ## 시각화 이미지 경로
import cv2
from PIL import Image
import numpy as np
import glob
from tqdm import tqdm

mdian_files = glob.glob("mdian/*.png") ## result1 폴더
bbb_files = glob.glob("afaf/*.png")    ## result2 폴더
for index in tqdm(range(len(mdian_files))):
    img_mdian = cv2.imread(mdian_files[index], cv2.IMREAD_UNCHANGED)
    img_bbb = cv2.imread(bbb_files[index], cv2.IMREAD_UNCHANGED)
    mdian_array = np.asarray(img_mdian)
    bbb_array = np.asarray(img_bbb)

    mdian_array = np.where(mdian_array==0, bbb_array, mdian_array)

    img_pil = Image.fromarray(mdian_array)
    img_pil.save("afaf_mdian_test/"+mdian_files[index][-8:]) ## 저장경로
import os
import sys

import cv2 as cv
import numpy as np
import getChampion


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def matching(pilImageList):
    result = []

    # 1) 캡처 이미지 가져옴
    relativePath = 'imgs\\sprite-champion-set.png'
    print('resource_path : ', resource_path(relativePath))
    ordImg = cv.imread(resource_path(relativePath), cv.IMREAD_GRAYSCALE)
    #capturedImg = cv.imread(path, cv.IMREAD_GRAYSCALE)
    for pilImage in pilImageList:
        capturedImg = cv.cvtColor(np.array(pilImage), cv.COLOR_RGB2GRAY)


        #ordImg = cv.resize(ordImg, dsize=(65, 65), interpolation=cv.INTER_AREA)

        # 2) 캡쳐된 이미지의 너비(w)와 높이(h)를 가져옴
        w, h = capturedImg.shape[::-1]

        #methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
        #            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

        # 3) 템플릿 매칭에 여러 방법이 있는데, 그 중 하나를 택함
        #methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        methods = ['cv.TM_SQDIFF_NORMED']

        for meth in methods:
            img = ordImg.copy()
            method = eval(meth)

            res = cv.matchTemplate(ordImg, capturedImg, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

            #print(min_loc)
            result.append(getChampion.parsePick(min_loc)['id'])

            #print(getChampion.getChampion(min_loc))

            #if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            #    top_left = min_loc
            #else:
            #    top_left = max_loc
            #bottom_right = (top_left[0] + w, top_left[1] + h)

            #cv.rectangle(img,top_left, bottom_right, 255, 2)

            #plt.subplot(121),plt.imshow(res,cmap = 'gray')
            #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            #plt.subplot(122),plt.imshow(img,cmap = 'gray')
            #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            #plt.suptitle(meth)
            #plt.rcParams["figure.figsize"] = (20,5)
            #plt.show()

    return result

# Test
'''
from PIL import Image
for i in range(0, 35, 2):
    path = "C:\\captureTest\\pic\\image" + str(i) + ".png"
    path2 = "C:\\captureTest\\pic\\image" + str(i+1) + ".png"
    print('\nimage', str(i), '.png, image', str(i+1), '.png => ')
    print(matching([Image.open(path), Image.open(path2)]))
'''
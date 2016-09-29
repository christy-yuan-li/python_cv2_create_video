mport cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os

def make_video(images, outvid='output.mov', fps=5, size=None, is_color=True, format="DIVX"):

    fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
    vout = None

    for img in images:
        print(img.shape)
        if vout is None:
            if size is None:
                size = (img.shape[1], img.shape[0])
            vout = cv2.VideoWriter()
            if not vout.open('aa.mov', fourcc, fps, size, True):
                print("ERROR: didn't succeed in opening the video")
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vout.write(img)
    vout.release()
    return vout


if __name__ == '__main__':
    img = cv2.imread('menpofit-logo.png')
    images = []
    for i in range(100):
        images.append(img)
    make_video(images)



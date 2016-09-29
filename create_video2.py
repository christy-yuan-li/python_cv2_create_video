mport cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from matplotlib import pyplot as plt

def make_video(images, outvid='output.mov', fps=2, size=None, is_color=False):

    fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
    vout = None

    for img in images:
        # for current code
        # img = img[:, :, 0:1]
        # plt.figure(1)
        # plt.imshow(img, cmap='gray')

        # for menpo usage
        img = np.array(img*255, dtype=np.uint8)
        img = np.expand_dims(img, axis=2)

        img = np.concatenate((img, img, img), axis=2)
        # print(img.shape)

        if vout is None:
            if size is None:
                size = (img.shape[1], img.shape[0]) # width, height
            vout = cv2.VideoWriter()
            if not vout.open(outvid, fourcc, fps, size, is_color):
                print("ERROR: didn't succeed in opening the video")
        if size[0] != img.shape[1] or size[1] != img.shape[0]:
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



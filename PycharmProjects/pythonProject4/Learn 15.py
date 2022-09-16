import cv2
import numpy as np


def pixel2char(pixel):
    char_list = "@#$%&erytuioplkszxcv=+---.     "
    index = int(pixel / 256 * len(char_list))
    return char_list[index]


def get_char_img(img, scale=4, font_size=5):
    # 调整图片大小
    h, w = img.shape
    re_im = cv2.resize(img, (w//scale, h//scale))
    # 创建一张图片用来填充字符
    char_img = np.ones((h//scale*font_size, w//scale*font_size), dtype=np.uint8)*255
    font = cv2.FONT_HERSHEY_SIMPLEX
    # 遍历图片像素
    for y in range(0, re_im.shape[0]):
        for x in range(0, re_im.shape[1]):
            char_pixel = pixel2char(re_im[y][x])
            cv2.putText(char_img, char_pixel, (x*font_size, y*font_size), font, 0.5, (0, 0, 0))
    return char_img


if __name__ == '__main__':
    img = cv2.imread('dl.jpg', 0)
    res = get_char_img(img)
    cv2.imwrite('d.jpg', res)


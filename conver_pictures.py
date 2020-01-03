"""
This is a very simple script to convert all images to proper size etc.
It uses imagemagic 'convert' tool.
"""

import argparse
import subprocess
import os
import cv2

parser = argparse.ArgumentParser('convert-images')
parser.add_argument('-i', '--input-folder', type=str)
parser.add_argument('-o', '--output-folder', type=str)
args = vars(parser.parse_args())

source_folder = args['input_folder']
target_folder = args['output_folder']

for file in os.listdir(args['input_folder']):
    if not file.endswith('.jpg'):
        continue
    pic_source = source_folder + file
    pic_target = target_folder + file
    subprocess.run(['aspectcrop',
                    '-a', '1:1',
                    '-g', 'c',
                    pic_source, pic_target])
    subprocess.run(['convert',
                    pic_target,
                    # resolution high enough to be analyzed,
                    # but low enough to upload to cloud-training
                    '-resize', '288x288',
                    pic_target])
    img = cv2.imread(pic_target, 0)
    template = cv2.imread('template.jpg', 0)
    w, h = template.shape[::-1]
    method_str = 'cv2.TM_CCOEFF'
    method = eval(method_str)
    result = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cropped_img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    cv2.imwrite(pic_target, cropped_img)

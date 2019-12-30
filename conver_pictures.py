"""
This is a very simple script to convert all images to proper size etc.
It uses imagemagic 'convert' tool.
"""

import subprocess
import os

# This is just dir before project dir
# To not mess dataset with git-controlled code files
root_dir = '../'
pictures_all_dir = 'pictures_all/'
pictures_ready_dir = 'pictures_ready_to_class/'

for file in os.listdir(root_dir + pictures_all_dir):
    if not file.endswith('.jpg'):
        continue
    pic_source = root_dir + pictures_all_dir + file
    pic_target = root_dir + pictures_ready_dir + file
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

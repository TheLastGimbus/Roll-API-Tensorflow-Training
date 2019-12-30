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
    subprocess.run(['convert',
                    root_dir + pictures_all_dir + file,
                    # resolution high enough to be analyzed,
                    # but low enough to upload to cloud-training
                    '-resize', '512x288',
                    root_dir + pictures_ready_dir + file])

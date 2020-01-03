"""
This is a very simple script to convert all images to proper size etc.
It uses imagemagic 'convert' tool.
"""

import argparse
import subprocess
import os

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

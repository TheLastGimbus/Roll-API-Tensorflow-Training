"""
This script is to easily classify images by human.
It shows you image, you press button which side of dice is it (or is it spinning/blurry)
and it moves certain pic to proper folder.
It moves it, so you can close it and come back later, and your work won't be mixed.
"""

import os
import shutil
import cv2


# This is just dir before project dir
# To not mess dataset with git-controlled code files
root_dir = '../'
classes_folder = 'classes/'
pictures_folder = 'pictures_ready_to_class/'

class_names = ['1', '2', '3', '4', '5', '6', 'moving']

# Create folders if they don't exist yet
for class_name in class_names:
    folder_dir = root_dir + classes_folder + class_name
    os.makedirs(folder_dir, exist_ok=True)

ready_to_class_list = os.listdir(root_dir + pictures_folder)

for pic in ready_to_class_list:
    pic_path = root_dir + pictures_folder + pic
    frame = cv2.imread(pic_path)
    cv2.namedWindow(pic, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(pic, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(pic, frame)
    key = cv2.waitKey(100000000)
    if key == 27:
        cv2.destroyAllWindows()
        break

    number_key = key-48 # because number key codes start from 49
    for x in range(1, 8):  # from 1 to 7
        if number_key == x:
            # move it to proper folder
            shutil.move(pic_path, root_dir + classes_folder + class_names[x - 1])
    if number_key == 9:  # remove pic from dataset
        os.remove(pic_path)
        
    cv2.destroyAllWindows()

print('You are done!')

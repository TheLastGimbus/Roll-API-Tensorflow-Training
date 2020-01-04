'''
This is a script that will get pictures of rolled dice
and put it in a directory so we can have a nice big dataset.

We still need to manually categorise them later,
using categorise_images.py
'''

import requests
import shutil
import subprocess
import os

def internet_error():
    subprocess.Popen(['notify-send', 'Python script has internet problem!'])
    print('Closing')
    exit()

while True:
    # ip of my phone with roll-android-server running
    url = "http://192.168.1.10:8822"
    shake_req = requests.get(url)
    if shake_req.status_code != 200:
        internet_error()
        break
    json = shake_req.json()

    img_url = url + json["picture_url"]
    img_req = requests.get(img_url, stream=True)
    if img_req.status_code != 200:
        internet_error()
        break

    pic_file_name = json['picture_url'][9:]
    print(pic_file_name)
    # save picture from roll-api
    with open('pictures/' + pic_file_name, 'wb') as out_file:
        img_req.raw.decode_content = True
        shutil.copyfileobj(img_req.raw, out_file)
    saved_pics = os.listdir('../pictures_lg_right/')
    if len(saved_pics) >= 300:
        print("DONE! 300!")
        break

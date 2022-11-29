import requests
from PIL import ImageGrab
import schedule
import time
import glob
import os
from datetime import datetime


# def take_screenshot():
#     print("Taking screenshot...")

#     image_date = f"screenshot-{str(datetime.now())}"
#     screenshot = ImageGrab.grab()
#     image_list = list(image_date)
#     image_list[25] = '.'
#     image_list[28] = '.'
#     image_list[30] = ','
#     image_name = ''.join(image_list)
#     filepath = f"./screenshots/{image_name}.png"
#     #

#     screenshot.save(f"{image_name}")

#     # post = requests.post('http://127.0.0.1:8000/api/post-frames/', data={'frames': frame})

#     print("Screenshot taken...")
#     return filepath

def take_screenshot():
    print("Taking screenshot...")

    image_date = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab(bbox=None)
    image_list=list(image_date)
    image_list[24]='.'
    image_list[27]='.'
    image_name= ''.join(image_list)
    filepath = f"C:\\Users\\mrbnu\\Desktop\\Projects\\DreamLine\\screenshot_py_app\\screenshots\\{image_name}.png"
    screenshot.save(filepath)
    send_img = open(f"C:\\Users\\mrbnu\\Desktop\\Projects\\DreamLine\\screenshot_py_app\\screenshots\\{image_name}.png", 'rb')
    post = requests.post('http://127.0.0.1:8000/api/post-frames/', files={'frame': send_img})
    
    
    print("Screenshot taken...",post.text)

    return filepath





def main():
    schedule.every(1).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()

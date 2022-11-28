

import pyscreenshot as ImageGrab

import schedule
import time

from datetime import datetime


def take_screenshot():
    print("Taking screenshot...")

    image_date = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab()
    image_list=list(image_date)
    image_list[24]='.'
    image_list[27]='.'
    image_name= ''.join(image_list)
    filepath = f"./screenshots/{image_name}.png"

    screenshot.save(filepath)

    print("Screenshot taken...")

    return filepath


def main():
    schedule.every(1).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)

        
if __name__ == '__main__':
    main()
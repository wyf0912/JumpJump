# coding: utf-8

from img import *
import random
import os
import time

press_coefficient = 1.68/2*pow(3,0.5)  #1.63
swipe_x1 = 0; swipe_y1 = 0; swipe_x2 = 0; swipe_y2 = 0

SCREENSHOT_WAY = 1


def pull_screenshot():
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen(
            'adb shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        f = open('autojump.png', 'wb')
        f.write(binary_screenshot)
        f.close()
    elif SCREENSHOT_WAY == 0:
        os.system('adb shell screencap -p /sdcard/autojump.png')
        os.system('adb pull /sdcard/autojump.png .')


def set_button_position(im):
    global swipe_x1, swipe_y1, swipe_x2, swipe_y2
    w, h = im
    left = int(w / 2)
    top = int(1584 * (h / 1920.0))
    left = int(random.uniform(left-50, left+50))
    top = int(random.uniform(top-10, top+10))    # 随机防 ban
    swipe_x1, swipe_y1, swipe_x2, swipe_y2 = left, top, left, top


def jump(distance):
    global press_coefficient
    set_button_position([1080,1920])
    press_time = distance * press_coefficient
    press_time = max(press_time, 200)   # 设置 200ms 是最小的按压时间
    press_time = int(press_time)
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=swipe_x1,
        y1=swipe_y1,
        x2=swipe_x2,
        y2=swipe_y2,
        duration=press_time
    )
    print(cmd)
    os.system(cmd)


def main():
    while 1:
        pull_screenshot()
        im = cv2.imread( './autojump.png')
        self_pos = self_detect(im)
        goal_pos = goal_detect(im, self_pos)
        im = cv2.resize(im,(540,960))
        cv2.imshow("test",im)
        cv2.waitKey(int(random.uniform(3000, 1000)))
        jump(pow(pow(goal_pos[0] - self_pos[0],2)+pow(goal_pos[1] - self_pos[1],2),0.5))
        cv2.waitKey(1500)

main()

import pyautogui as p
import os
import lib.level_up as level_up

p.moveTo(300, 300)

for staff_img in os.listdir("./img/toad/staff"):
    staff = './img/toad/staff/{staff}'.format(staff=staff_img)
    print(staff)
    staffs_pos = p.locateAllOnScreen(staff)
    for pos in staffs_pos:
        level_up.raiseStaffReelAndOneStar(pos)
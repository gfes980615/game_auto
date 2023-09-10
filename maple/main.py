import pyautogui as p
import os
import lib.tool as tool


try:
    open_cube = tool.openCube()
    if open_cube == True:
        for staff_img in os.listdir("./img/staff"):
            staff = './img/staff/{staff}'.format(staff=staff_img)
            staffs_pos = p.locateAllOnScreen(staff)
            tool.start_from_positions(staffs_pos)
    else:
        print("cube not found")
        
except (KeyboardInterrupt, SystemExit):
    print()
    print('Use maple_cube count: ', tool.maple_cube_total)
    print('Use weird_cube nums: ', tool.weird_cube_total)

import pyautogui as p
import time

p.PAUSE = 0.5

# get position
# while True:
#     print(p.position())
#     time.sleep(5)


# screenshot
locate_file='../img/staff/ears.png'
print('Screenshot')
p.screenshot(imageFilename=locate_file, region=(1879, 63, 24, 18))

# staff_img = locate_file
# staffs_pos = p.locateAllOnScreen(staff_img)
# for staff in staffs_pos:
#     staff_pos = p.locateOnScreen(staff_img, region=staff)
#     p.moveTo(staff_pos)
#     print(staff_pos)
#     p.moveTo(100,100)
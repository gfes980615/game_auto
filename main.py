import pyautogui as p

# while True:
#     print(pyautogui.position())
#     time.sleep(1)

# p.moveTo(1343, 37) # move to 裝飾 position
# p.click()
print()
# pos=p.locateCenterOnScreen('./楓之谷/property/STR6.bmp', grayscale=False)
pos=p.locateCenterOnScreen('./image/str_3.png', grayscale=False)
if pos == None:
    print('not found')
else:
    print(pos)
    p.moveTo(pos)


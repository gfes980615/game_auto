import lib.tool as tool
import time
import pyautogui as p
import pydirectinput as pp
import time
import lib.screen as screen
import lib.level_up as l

pp.PAUSE = 0.01

with open('./tmp.txt', 'r') as file:
    lines = file.readlines()



lines = [line.strip() for line in lines]

for numbers in lines:
    p.moveTo(x=955,y=488)
    p.click()
    p.hotkey('ctrl','a')
    pp.press('backspace')
    for n in numbers: 
        pp.press(n.lower())
    p.moveTo(x=952,y=588)
    time.sleep(0.5)
    p.click()
    time.sleep(0.5)
    p.moveTo(x=963,y=731)
    time.sleep(0.5)
    p.click()
    time.sleep(0.5)
    with open('record.txt', 'a') as record_file:
        record_file.write('\n' + numbers)
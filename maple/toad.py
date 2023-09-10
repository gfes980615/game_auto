import pyautogui as p
import os
import lib.tool as tool

inherit_map_120_to_130={
    'u_suit1': 'suit_130'
}

pos = p.locateOnScreen('./img/toad/suit_130.png')

for i in pos:
    p.click(i)
    print(i)

    # click inherit reel
    p.moveTo(922, 568)
    p.click()
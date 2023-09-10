import pyautogui as p
import pydirectinput as pp
import time

p.PAUSE = 0.1  
pp.PAUSE = 0.1

logo_pos=p.locateCenterOnScreen('./img/logo.png')

p.click(100, 10)

while True:
    buff_dict = dict({
        'exp_2h_10pa': '6',
        'exp_2h_20pa': '7',
        'exp_1h_100pa': '8',
    })

    for buff, press_key in buff_dict.items():
        print(buff, press_key)
        buff_pos = p.locateCenterOnScreen('./img/{buff}.png'.format(buff = buff))
        if buff_pos == None:
            print('Not found\nUse {buff}'.format(buff=buff))
            pp.press(press_key)
            pp.press('enter')
            pp.press('enter')
        else:
            print(buff_pos)
            print('still have {buff}'.format(buff=buff))
            buff_pos = None
    
    while True:
        pos=p.locateOnScreen('./img/tab_monster.png')
        if pos == None:
            pp.press('tab')
        else:
            print('found!')
            break               
    pp.press('1')                                                                                                               
    time.sleep(5.8)                                                                                         
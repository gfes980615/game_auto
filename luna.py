import pyautogui as p
import pydirectinput as pp
import time

p.PAUSE = 1
pp.PAUSE = 1

logo_pos=p.locateCenterOnScreen('./luna_image/logo.png')

while True:
    if logo_pos == None:
        print('Not found luna, finish')
        break
    else:
        p.moveTo(logo_pos)
        p.click()

    buff_dict = dict({
        'exp_2h_10pa': '6',
        'mp': '7',
        'exp_2h_20pa':'8',
        'exp_1h_100pa': '9',
    })

    for buff, press_key in buff_dict.items():
        print(buff, press_key)
        buff_pos = p.locateCenterOnScreen('./luna_image/{buff}.png'.format(buff = buff))
        while True: 
            if buff_pos == None:
                print('Not found\nUse {buff}'.format(buff=buff))
                pp.press(press_key)
                pp.press('enter')
                pp.press('enter')
            else:
                print(buff_pos)
                print('still have {buff}'.format(buff=buff))
                buff_pos = None
                break
    time.sleep(10)
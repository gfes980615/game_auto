import pyautogui as p
import pydirectinput as pp
import time

p.PAUSE = 0.5
pp.PAUSE = 0.5
# 選擇第一個卷軸
def clickReelButtom():
    p.moveTo(1015,476)
    p.click()

def clickStartRaiseReelButton():
    clickImagePos('./img/select_raise_reel_button.png')

def clickCancelRaiseReelButton():
    clickImagePos('./img/select_cancel_reel_button.png')

def clickConfirmButton():
    clickImagePos('./img/confirm_raise_button.png')

def clickFinalConfirmButton():
    p.moveTo(961,598)
    p.click()

def clickStarRaiseButton():
    p.moveTo(920,640)
    p.click()

def clickStarCancelButton():
    p.moveTo(1000,640)
    p.click()

def clickStarRaiseConfirmButton():
    p.moveTo(926,600)
    p.click()

def clickStarRaiseStopButton():
    p.moveTo(964,640)
    p.click()

def clickImagePos(img=''):
    pos = p.locateOnScreen(img)
    if pos != None:
        p.moveTo(pos)
        p.click()
        return True
    return False

def raiseStaffReelAndOneStar(staff_pos=None):
    p.click(300, 300)
    pp.press('o')
    p.moveTo(staff_pos)
    p.click()
    p.moveTo(p.locateOnScreen('./img/raise_star_logo.png'))
    p.click()
    clickReelButtom()

    while True:
        star_raise_logo = p.locateOnScreen('./img/star_raise_logo.png')
        if star_raise_logo != None:
            break
        else:
            clickStartRaiseReelButton()
            clickConfirmButton()
            time.sleep(1.5)
            clickFinalConfirmButton()

    clickStarRaiseButton()
    clickStarRaiseConfirmButton()
    time.sleep(2)
    clickStarRaiseStopButton()
    time.sleep(2)
    clickFinalConfirmButton()
    clickStarCancelButton()
    pp.press('esc')
        
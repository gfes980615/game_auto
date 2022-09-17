import pyautogui as p
import pydirectinput as pp
import time
import screen
import level_up as l
import os

p.PAUSE = 0.5
pp.PAUSE = 0.5

def findField(field=''):
    pos_1 = p.locateCenterOnScreen('./img/field/{field}.png'.format(field=field))
    pos_2 = p.locateCenterOnScreen('./img/field/{field}_2.png'.format(field=field))
    pos = None

    if pos_1 != None:
        pos = pos_1
    elif pos_2 != None:
        pos = pos_2
    return pos

def clickCubeCenter():
    pos = p.locateCenterOnScreen('./img/cube_center.png')
    if pos == None:
        return False
    p.moveTo(pos)
    p.click()
    return True

def findImg(img=''):
    pos = p.locateCenterOnScreen('./img/{img}.png'.format(img=img))
    if pos == None:
        return None, False
    return pos, True

def clickCubeConfirmButtom():
    p.moveTo(939, 664)
    p.click()

def clickCubeCancelButtom():
    p.moveTo(983, 664)
    p.click()

def clickWeirdCubeConfirmButtom():
    p.moveTo(939, 664)
    p.click()

def clickWeirdCubeCancelButtom():
    p.moveTo(1028, 664)
    p.click()

def isLevelUp():
    pos = p.locateCenterOnScreen('./img/level_up.png')
    if pos == None:
        return False
    return True

def onlyTwoLine():
    normal_pos = p.locateCenterOnScreen('./img/normal.png')
    block_pos = p.locateCenterOnScreen('./img/block.png', region=(887, 623, 973, 641))
    if (normal_pos != None) and (block_pos != None):
        return True
    return False

def levelUp():
    print('Start level up.')
    while True:
        if isLevelUp():
            clickCubeCancelButtom()
            print('Level up success!')
            return True
        if onlyTwoLine():
            clickCubeCancelButtom()
            print('Only two line, do not level up.')
            return False
        clickCubeConfirmButtom()
        pp.press('enter')
        time.sleep(1)

def openPackage():
    p.moveTo(300, 300)
    p.click()
    pp.press('i')

def openCube():
    print('Start open cube.')
    decorate_pos = findField('decorate')
    if decorate_pos == None:
        print('Open the package.')
        openPackage()
        decorate_pos = findField('decorate')

    p.moveTo(decorate_pos)
    p.click()

    cube_pos = p.locateCenterOnScreen('./img/cube.png')
    if cube_pos == None:
        print('Not fount cube, need to get it.')
        return False
    p.moveTo(cube_pos)
    p.doubleClick()
    print('Open cube success!')
    moveMouseOutPackagePosition()
    return True

def moveMouseOutPackagePosition():
    p.moveTo(300, 300)
    print('Mouse move to another place.')

def ninePercentage(staff_pos=None):
    consume_pos = findField('consume')
    p.moveTo(consume_pos)
    p.click()
    cube_pos, exist = findImg('weird_cube')
    if exist == False:
        print('Not found weird cube.')
        return False
    p.moveTo(cube_pos)
    p.doubleClick()

    moveMouseOutPackagePosition()

    p.moveTo(staff_pos)
    p.click()
    pp.press('enter')
    time.sleep(2)
    while True:
        if screen.okAttributes() == False:
            clickWeirdCubeConfirmButtom()
            pp.press('enter')
            pp.press('enter', _pause=False)
            print('continue')
            time.sleep(1)
        else:
            print('ninePercentage finish')
            break
        if screen.existingWeirdCube() == False:
            return ninePercentage(staff_pos)
    
    clickWeirdCubeCancelButtom()
    return True

# TODO: Open equirement field first

def start(staff_img=''):
    open_cube = openCube()
    if open_cube == False:
        print('Not found cube')

    staffs_pos = p.locateAllOnScreen(staff_img)
    num = 1
    for staff in staffs_pos:
        print('Start! item: ', num)
        num += 1
        open_cube = openCube()
        if open_cube == False:
            print('Not found cube')
            break
        p.moveTo(staff)
        p.click()

        cube_center = clickCubeCenter()
        if cube_center == False:
            print('Not open the cube, cancel.')
            break

        level_up = levelUp()
        if level_up == True:
            print('Start 9 percentage attributes')
            nine_percentage = ninePercentage(staff_pos=staff)

            print('Start raise the reel and star')
            l.raiseStaffReelAndOneStar(staff)
        print('End.')
        print('=================')
        
    print('Finish ',staff_img)
    print()

# for staff in os.listdir("./img/staff"):
#     print('start {file}'.format(file=staff))
#     start('./img/staff/{staff}'.format(staff=staff))
start('./img/staff/{staff}'.format(staff='suit1.png'))
start('./img/staff/{staff}'.format(staff='suit2.png'))
start('./img/staff/{staff}'.format(staff='suit3.png'))
start('./img/staff/{staff}'.format(staff='suit4.png'))
start('./img/staff/{staff}'.format(staff='suit5.png'))
# for staff in os.listdir("./img/staff"):
#     staffs_pos = p.locateAllOnScreen('./img/staff/{staff}'.format(staff=staff))
#     for pos in staffs_pos:
#         print(staff, pos)
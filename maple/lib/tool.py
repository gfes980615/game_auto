import pyautogui as p
import pydirectinput as pp
import time
import lib.screen as screen
import lib.level_up as l

p.PAUSE = 0.5
pp.PAUSE = 0.5

maple_cube_total=0
weird_cube_total=0

def findField(field=''):
    pos_1 = p.locateCenterOnScreen('./img/field/{field}.png'.format(field=field))
    pos_2 = p.locateCenterOnScreen('./img/field/{field}_2.png'.format(field=field))
    pos = None

    if pos_1 != None:
        pos = pos_1
    elif pos_2 != None:
        pos = pos_2
    return pos

def findImg(img=''):
    pos = p.locateCenterOnScreen('./img/{img}.png'.format(img=img))
    if pos == None:
        return None, False
    return pos, True

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
    global maple_cube_total
    print('Start level up.')
    level_up_counter = 0
    while True:
        if level_up_counter >= 200:
            print('Cost too much money')
            return False
        if isLevelUp():
            clickCubeCancelButtom()
            print()
            print('Level up success!')
            maple_cube_total += level_up_counter
            return True
        if onlyTwoLine():
            clickCubeCancelButtom()
            print('Only two line, do not level up.')
            return False
        clickCubeConfirmButtom()
        pp.press('enter')
        level_up_counter += 1
        print('count: ', level_up_counter, ', not yet, countinue.', end='\r')
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
    # print('Mouse move to another place.')

def ninePercentage(staff_pos=None):
    global weird_cube_total
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
    
    weird_cube_counter = 0
    print("Counter")

    while True:
        weird_cube_counter += 1
        if weird_cube_counter >= 100:
            print('Cost too many werid cube, ignore this time.')
            return False
        if screen.okAttributes() == False:
            print('count: ', weird_cube_counter, ', not yet, countinue.', end='\r')
            clickWeirdCubeConfirmButtom()
            pp.press('enter')
            pp.press('enter', _pause=False)
            time.sleep(1)
        else:
            print('count: ', weird_cube_counter, ', success! Finish.')
            print('ninePercentage finish')
            weird_cube_total += weird_cube_counter
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
            if nine_percentage == True:
                print('Start raise the reel and star')
                l.raiseStaffReelAndOneStar(staff)
        print('End.')
        print('=================')
        
    print('Finish ',staff_img)
    print()

def start_from_positions(postions):
    num = 1
    for pos in postions:
        print('Start! item: ', num)
        num += 1
        open_cube = openCube()
        if open_cube == False:
            print('Not found cube')
            break
        p.moveTo(pos)
        p.click()

        cube_center = clickCubeCenter()
        if cube_center == False:
            print('Not open the cube, cancel.')
            break

        level_up = levelUp()
        if level_up == True:
            print('Start 9 percentage attributes')
            if ninePercentage(staff_pos=pos):
                print('Start raise the reel and star')
                l.raiseStaffReelAndOneStar(pos)
        else:
            print(pos)
        print('End.')
        print('=================')
        
    print('Finish=========')
    print()

def clickCubeConfirmButtom():
    p.moveTo(940, 655)
    p.click()
    # cube_pos = p.locateCenterOnScreen('./img/cube_confirm_button.png')
    # if cube_pos is not None:
    #     p.moveTo(cube_pos)
    #     p.click()
    # else:
    #     print('Not fount cube, need to get it.')
    

def clickCubeCancelButtom():
    p.moveTo(985, 655)
    p.click()
    # cube_pos = p.locateCenterOnScreen('./img/cube_cancel_button.png')
    # if cube_pos is not None:
    #     p.moveTo(cube_pos)
    #     p.click()
    # else:
    #     print('Not fount cube, need to get it.')

def clickWeirdCubeConfirmButtom():
    p.moveTo(939, 664)
    p.click()

def clickWeirdCubeCancelButtom():
    p.moveTo(1028, 664)
    p.click()

def clickCubeCenter():
    pos = p.locateCenterOnScreen('./img/cube_center.png')
    if pos == None:
        return False
    p.moveTo(pos)
    p.click()
    return True

def clickKeyboard(char):
    pos = p.locateCenterOnScreen('./img/keyboard/'+char+'.png')
    if pos == None:
        return False
    p.moveTo(pos)
    p.click()

def pressEnter():
    pp.press('enter')

def pressKeyboard(key):
    pp.press(key)
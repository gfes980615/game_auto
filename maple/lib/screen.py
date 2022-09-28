from PIL import Image
import pyautogui as p
import pytesseract
import re

p.PAUSE = 1

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def okAttributes(cube='weird'):
    attributes = []
    for i in range(0, 3):
        if cube == 'weird':
            p.screenshot(imageFilename=str(i)+'.png', region=(875, 584+i*13, 100, 13)) # weird cube position
        elif cube == 'green':
            p.screenshot(imageFilename=str(i)+'.png', region=(884, 604+i*13, 150, 13)) # green cube position
        else:
            print('Not support cube type: {cube}'.format(cube=cube))
            return False
        img = Image.open(str(i)+'.png')
        text = pytesseract.image_to_string(img, lang='eng')
        text = text.replace("\n","")
        text = text.replace("\t","")
        text = text.replace(" ","")
        attributes.append(text)

    # print(attributes)
    attrMap_6 = dict(
        str=re.compile('.*STR.*6(8|%).*'),
        int=re.compile('.*INT.*6(8|%).*'),
        dex=re.compile('.*DE.*6(8|%).*'),
        luk=re.compile('.*LU.*6(8|%).*'),
    )
    attrMap_3 = dict(
        str=re.compile('.*STR.*3(8|%).*'),
        int=re.compile('.*INT.*3(8|%).*'),
        dex=re.compile('.*DE.*3(8|%).*'),
        luk=re.compile('.*LU.*3(8|%).*'),
    )

    count_6 = dict(
        str = 0,
        int = 0,
        dex = 0,
        luk = 0,
    )

    count_3 = dict(
        str = 0,
        int = 0,
        dex = 0,
        luk = 0,
    )

    for attr in attributes:
        for key in attrMap_6:
            r = attrMap_6.get(key)
            if r.search(attr) != None:
                count_6[key] += 1
                break
        for key in attrMap_3:
            r = attrMap_3.get(key)
            if r.search(attr) != None:
                count_3[key] += 1
                break

    # print(count_6)
    # print(count_3)

    for key in count_6:
        if count_6[key] >= 2:
            print()
            print('success', key)
            return True
        elif count_6[key] >= 1 and count_3[key] >=1:
            print()
            print('success', key)
            return True

    return False

def existingWeirdCube():
    exist = p.locateOnScreen('./img/weird_cube_opening.png')
    if exist == None:
        return False
    return True


p.screenshot(imageFilename='staff.png', region=(1711, 231-42, 24, 18))
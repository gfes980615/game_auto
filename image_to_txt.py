from PIL import Image
import pyautogui as p
import pytesseract
  
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


for i in range(0, 3):
    p.screenshot(imageFilename=str(i)+'.png', region=(884, 604+i*13, 150, 13))
    img = Image.open(str(i)+'.png')
    text = pytesseract.image_to_string(img, lang='eng')
    text = text.replace("\n","")
    text = text.replace("\t","")
    text = text.replace(" ","")
    print(text)

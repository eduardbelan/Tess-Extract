import pytesseract
import cv2
from pytesseract import Output
from PIL import Image

# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\eduar\\Tesseract-OCR\\tesseract.exe'

# Configure psm and oem
myconfig = r"--psm 6 --oem 3"


def extract_txt_to_console():
    """Extract text to Console."""
    extracted_txt = pytesseract.image_to_string(Image.open("umweltschutz-arbeitsschutz.png"), config=myconfig)
    print(extracted_txt)


extract_txt_to_console()

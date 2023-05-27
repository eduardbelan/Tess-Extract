# OCR Text Extraction with Tesseract - Tess-Extract

## Description
Tess-Extract is a Python script that utilizes optical character recognition (OCR) techniques to extract text from an image file. It uses the pytesseract library, along with cv2 (OpenCV), pytesseract's Output, and PIL (Python Imaging Library).

## Installation
To use Tess-Extract, follow these steps:

1. Ensure you have Python installed on your system.
2. Visit [GitHub pytesseract](https://github.com/tesseract-ocr/tesseract) and follow the instructions to install pytesseract.

## Usage
To use Tess-Extract, follow these steps:

1. Import the necessary libraries: _(Install them if needed)_
```python
import pytesseract
import cv2
from pytesseract import Output
from PIL import Image
```
2. Load an image file. _(Put the image file in the directory where tess-extract.py is located and just enter the image name, no path needed)._
```python
img = cv2.imread("path\\to\\image.jpg")
# or like this when the image is in the root directory
img = cv2.imread("image.jpg")
```
3. tess-extract.py has three main functions. Find them at the bottom of the file and uncomment the function you want to run.
```python
# This function extracts the text from the image and prints it to the console.
def extract_txt_to_console():
# This function detects single characters and draws bounding boxes around each character found in the image.
def box_around_character():
# This function identifies words in the image and draws bounding boxes around them.
# Change the confidence level with the confidence parameter.
def box_around_word(confidence):
```
## Snippets
The function `"extract_txt_to_console()"` is available in the snippets.py file as a separate and fully functional program.

## Run in Console
It is possible to run the program in the console directly. Here are some useful commands:
```bash
# Extract text form images in the shell
tesseract <image.jpg> stdout
# Specify pgm
tesseract <image.jpg> stdout --psm <num>
# Specify pgm and oem
tesseract <image.jpg> stdout --psm <num> --oem <num>
# Specify language
tesseract <image.jpg> stdout -l deu
# Save extracted text to txt file (no need to specify .txt - automatically done)
tesseract <image.jpg> <txt_file_name>
# Save extracted text to txt file and specify selected language to deu
tesseract <image.jpg> <txt_file_name> -l deu
```

Feel free to explore and modify the Tess-Extract program according to your specific requirements.

## License
Tess-Extract is released under the [MIT License](https://opensource.org/licenses/MIT).

**Note:** This program is provided as-is without any warranty. Use it at your own risk.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.

Enjoy using Tess-Extract.
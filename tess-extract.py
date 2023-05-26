import pytesseract
import cv2
from pytesseract import Output
from PIL import Image


# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\eduar\\Tesseract-OCR\\tesseract.exe'

# Extract text form images in the shell
#   - tesseract <image.jpg> stdout
# Specify pgm
#   - tesseract <image.jpg> stdout --psm <num>
# Specify pgm and oem
#   - tesseract <image.jpg> stdout --psm <num> --oem <num>
# Specify language
#   - tesseract <image.jpg> stdout -l deu
# Save extracted text to txt file (no need to specify .txt - automatically done)
#   - tesseract <image.jpg> <txt_file_name>
# Save extracted text to txt file and specify selected language to deu
#   - tesseract <image.jpg> <txt_file_name> -l deu


""""""
"""
Page segmentation modes:
     0    Orientation and script detection (OSD) only.
     1    Automatic page segmentation with OSD.
     2    Automatic page segmentation, but no OSD, or OCR.
     3    Fully automatic page segmentation, but no OSD. (Default)
     4    Assume a single column of text of variable sizes.
     5    Assume a single uniform block of vertically aligned text.
     6    Assume a single uniform block of text.
     7    Treat the image as a single text line.
     8    Treat the image as a single word.
     9    Treat the image as a single word in a circle.
    10    Treat the image as a single character.
    11    Sparse text. Find as much text as possible in no particular order.
    12    Sparse text with OSD.
    13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
"""
"""
OCR Engine Mode
     0    Legacy engine only.
     1    Neural nets LSTM engine only.
     2    Legacy + LSTM engines.
     3    Default, based on what is available.
"""
# Configure psm and oem
myconfig = r"--psm 6 --oem 3"


def extract_txt_to_console():
    """Extract text to Console."""
    extracted_txt = pytesseract.image_to_string(Image.open("umweltschutz-arbeitsschutz.png"), config=myconfig)
    print(extracted_txt)


def box_around_character():
    """Draw Boxes around each Character."""

    # Load image with cv2.imread method
    img = cv2.imread("kassenbon.jpg")
    # Get the height and width of the image using the shape attribute
    height, width, _ = img.shape

    # Use Tesseract-OCR on the image to detect the bounding boxes for each character
    boxes = pytesseract.image_to_boxes(img, config=myconfig)

    # Loop over each line of text (each detected character) in result returned by pytesseract.image_to_boxes() method
    for box in boxes.splitlines():
        # Split the line of text (detected character) into a list of substrings using split() method with space (" ")
        box = box.split(" ")
        # Extract the coordinates of the bounding box for the detected character
        x1, y1, x2, y2 = int(box[1]), height - int(box[2]), int(box[3]), height - int(box[4])
        # Draw a rectangle around the bounding box of the detected character using the cv2.rectangle() method
        # The color of the rectangle is set to blue (255, 0, 0) with a thickness of 1 pixel
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
        # Print the text of the detected character above the rectangle in red
        # cv2.putText(image, char, coordinates, font, fontScale, color, thickness, cv2.LINE_AA, True/False)
        # Get the character of the detected character
        char = box[0]
        # Print the character of the detected character above the rectangle in red using the cv2.putText method
        img = cv2.putText(img, char, (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the final image with the bounding boxes drawn around each detected character using the cv2.imshow() method
    # The title of the window will be "image"
    cv2.imshow("image", img)
    # Wait until a key is pressed before closing the window using cv2.waitKey() method
    cv2.waitKey(0)


def box_around_word(confidence):
    """Draw Boxes around each detected Word"""

    # Load image with cv2.imread method
    img = cv2.imread("kassenbon.jpg")
    # Get the height and width of the image using the shape attribute
    height, width, _ = img.shape

    # Use Tesseract-OCR engine to detect text in image
    data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
    # print(data.keys()) # shows the keys of the dict
    # print(data["text"]) # shows the words that were detected
    # print(data["conf"]) # shows the confidence with which every single word was detected
    # Extract number of boxes detected in the image
    amount_boxes = len(data["text"])

    # Loop through all text boxes detected in image
    for i in range(amount_boxes):
        # Filter out text boxes with low confidence level
        if float(data["conf"][i]) > confidence:
            # Extract coordinates and dimensions of the text box
            (x, y, width, height) = (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
            # Draw a blue rectangle as the text box
            # cv2.rectangle(image, start_point, end_point, color, thickness)
            img = cv2.rectangle(img, (x, y), (x+width, y+height), (255, 0, 0), 2)
            # Print the text of the detected word below the rectangle in red
            # cv2.putText(image, <text>, coordinates, font, fontScale, color, thickness, cv2.LINE_AA, True/False)
            img = cv2.putText(img, data["text"][i], (x, y+height+20),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the final image with the bounding boxes drawn around each detected character using the cv2.imshow() method
    # The title of the window will be "image"
    cv2.imshow("image", img)
    # Wait until a key is pressed before closing the window using cv2.waitKey() method
    cv2.waitKey(0)


# Extract text to Console
# extract_txt_to_console()

# Show Boxes around each Character
# box_around_character()

# Show Boxes around each Word
#   - enter confidence parameter from 0 to 100
# box_around_word(confidence=50)

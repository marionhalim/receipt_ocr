import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import re

""" @param url 
    @return a string of the image"""
def process_jpg_image(url):
    image = _get_image(url)
    image = sharpen(image, 1)
    return pytesseract.image_to_string(image)

""" @param url 
    @return an image"""
def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

""" 
@param input a url of the image 
@param num number of times to to sharpen image
@return a sharpened image of the original image, default 1
"""
def sharpen(input, num): 
	image = input.filter(ImageFilter.SHARPEN)
	sharpen_more = num - 1
	for n in sharpen_more: 
		image = image.filter(ImageFilter.SHARPEN)
	return image

"""
Takes in an image, calls pytesseract and returns a string
"""
def image_to_string(img):
    return pytesseract.image_to_string(img)

"""
@param str returned by the OCR on the receipt
@return a dictionary with keys as item names, and values as prices (in string)
"""    
def collect_names_prices(string_receipt):
    lines = string_receipt.split("\n")
    output = {}
    for line in lines:
        name_and_price = get_name_and_price(line)
        if (name_and_price):
            name = name_and_price[0]
            price = name_and_price[1]
            output[name] = price
    return output

"""
@param LINE is a string representing a single line returned by the OCR
@return a tuple of (name, price) if it is an item and None otherwise

Assumptions:
-price is in decimal
-item and price are on the same line

"""
def get_name_and_price(line):
    m = re.search("\s*(.*)\s+[\$]?(\d{1,})\.(\d{0,2})", line)
    if m!=None:
        name = m.group(1)
        price = m.group(2) + "." + ( "00" if m.group(3) == "" else m.group(3))
        return (name, price)
    else:
        return None

# Temporary. Takes in a file name for ease of testing
def file_to_string(filepath):
    return image_to_string(Image.open(filepath))




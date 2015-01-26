import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import re

"""
"""
def process_jpg_image(url):
    image = _get_image(url)
    image = sharpen(image, 1)
    return pytesseract.image_to_string(image)

    #Sharpen 
    #Smooth 
    #Smooth_more

def process_png_image(url):
	image = _get_image(url)
	return pytesseract.image_to_string(image)

# Passes in a URL and grabs the image 
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

#EVERYTHING BELOW IS ONLY FOR TESTING
a = "50 Marion 12.00 SALE"
b = "2 books .00"
c ="44 G1nger Lover $9.50"
d = "Brown R1ce $2.00"
e = "Iota] 2 item(s) $11.50"
x = "Brown Rice 12.00"
y = "Pad Thai 13"
z = "Super awesome Indonesian mie tek tek $12.99"
print get_name_and_price(a)
print get_name_and_price(b)
print get_name_and_price(c)
print get_name_and_price(d)
print get_name_and_price(e)

print get_name_and_price(x)
print get_name_and_price(y)
print get_name_and_price(z)

stuff = file_to_string("images/restaurant.png")
print stuff
x = (collect_names_prices(stuff))
print "Printing all that are collected"
print x
for name in x:
    print (name, x[name])


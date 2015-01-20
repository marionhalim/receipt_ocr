import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

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


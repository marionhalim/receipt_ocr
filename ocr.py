import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

# Sharpens and process the image
def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

# Passes in a URL and grabs the image 
def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))

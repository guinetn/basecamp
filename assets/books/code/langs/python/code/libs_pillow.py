'''
pillow
https://pypi.org/project/Pillow/
https://pillow.readthedocs.io/en/stable/
https://github.com/python-pillow/Pillow

Fork of the Python Image Library
To manipulate digital images
To create thumbnails, convert between file formats, rotate, apply filters, display images...
'''

from PIL import Image

im = Image.open("kittens.jpg")
im.show()
print(im.format, im.size, im.mode)
# JPEG (1920, 1357) RGB

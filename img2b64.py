#!/usr/bin/python2
import base64
import sys
from PIL import Image
from io import BytesIO

if len(sys.argv) > 1:
    filename = sys.argv[1]

    if filename[-4:] == '.png':
        with open(filename, "rb") as image_file:
            print base64.b64encode(image_file.read())
    else:
        print 'file name is not end with \".gif\"'
else:
    print 'incorrect file name!'

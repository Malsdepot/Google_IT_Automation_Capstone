#!/usr/bin/python3

import os
from PIL import Image

src = os.path.expanduser("~/images")
dst = "/opt/icons/"
outputFormat = "JPEG"
outSize = (128,128)
outputRotation = 90

for f in os.listdir(src):
    if f != "imageProcessor.py":
        try:
            im=Image.open(f)
        except OSError:
            print("Unable to open: " + str(f))
            next
        im = im.rotate(outputRotation)
        im = im.resize(outSize)
        im = im.convert("RGB")
        outfile = dst+f
        im.save(outfile, outputFormat)
        print("Saved as: " + str(outfile))

print ("Test output")
testImage = Image.open("/opt/icons/ic_edit_location_black_48dp")
print(testImage.format, testImage.size)











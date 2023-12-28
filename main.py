from PIL_and_Tkinter import *
import sys

import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

pilImage = Image.open(r"Portrait.JPG")
showPIL(pilImage, "white")
pilImage2 = Image.open(r"Landscape.JPG")
showPIL(pilImage2, "black")

print("heck freaking yeah")
print(f"maybe not")
from PIL_and_Tkinter import *
import sys
import subprocess

import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

subprocess.run(["python3", "dependancies.py"])
print(f"ran subprocess")

pilImage = Image.open(r"Portrait.JPG")
showPIL(pilImage, "white")
pilImage2 = Image.open(r"Landscape.JPG")
showPIL(pilImage2, "black")
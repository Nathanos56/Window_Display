from PIL_and_Tkinter import *
import sys
import subprocess

subprocess.run(["python3", "dependancies.py"])



pilImage = Image.open(r"Portrait.JPG")
showPIL(pilImage, "white")
pilImage2 = Image.open(r"Landscape.JPG")
showPIL(pilImage2, "black")
from PIL_and_Tkinter import *
import sys
import subprocess

subprocess.run(["python3", "dependancies.py"])



pilImage = Image.open(r"Portrait.jpg")
showPIL(pilImage, "white")
pilImage2 = Image.open(r"Landscape.jpg")
showPIL(pilImage2, "black")
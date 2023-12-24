from PIL_and_Tkinter import *
import sys


pilImage = Image.open(r"Portrait.jpg")
showPIL(pilImage, "white")
pilImage2 = Image.open(r"Landscape.jpg")
showPIL(pilImage2, "black")
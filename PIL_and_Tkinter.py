import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage, color):
    global tkimage
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.configure(bg = color)
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), root.destroy()))
    pilImage = my_resize(pilImage, h, w)
    tkimage = ImageTk.PhotoImage(pilImage)
    label = tkinter.Label(root)
    label.image = tkimage  
    label.configure(image=tkimage)
    label.pack()
    root.mainloop()


def my_resize(input_image, h, w):
    # Get the original image dimensions
    imgw, imgh = input_image.size

    # Calculate the scaling factors
    wdif = imgw / w
    hdif = imgh / h

    # Check the aspect ratio of the image
    aspect_ratio = imgh / imgw

    # Rotate the image if it is in portrait mode
    if aspect_ratio > 1:
        input_image = input_image.rotate(90, expand=True)
        # Update the image dimensions after rotation
        imgw, imgh = input_image.size
        # Recalculate the scaling factors
        wdif = imgw / w
        hdif = imgh / h
        # Calculate the aspect ratio of rotated image
        aspect_ratio = imgh / imgw

    # Determine which dimension is the limiting factor
    if hdif < wdif:
        # Width is the limiting factor, so scale by wdif
        newimg = input_image.resize((w, int(imgh / wdif)), Image.LANCZOS)
    else:
        # Height is the limiting factor, so scale by hdif
        newimg = input_image.resize((int(imgw / hdif), h), Image.LANCZOS)

    # Return the resized image
    return newimg
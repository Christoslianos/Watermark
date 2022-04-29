
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image, ImageDraw, ImageFont

# create the GUI interface
window = Tk()
window.title("Watermark me")
window.geometry('600x600')
window.resizable(width=True, height=True)



def open_img():
    x = openfilename()
    # open the image
    image = Image.open(x)
    # resize picture
    image = image.resize((round(image.size[0] * 0.5), round(image.size[1] * 0.5)))

    # edit the image (watermark), load font and position
    drawing = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    drawing.text((0, 0), "@christoslianos", font=font, fill=(255, 0, 0))
    img = ImageTk.PhotoImage(image)
    # display the image on a label on the screen
    label = Label(window, image=img)
    label.image = img
    label.grid(row=3)
    # save the image in the image folder
    image.save(f"images/{img}.jpeg")


def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

buttom = Button(window, text='open file', command=open_img).grid(
    row=2, columnspan=4)



window.mainloop()

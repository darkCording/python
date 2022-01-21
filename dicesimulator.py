from tkinter import *
from PIL import Image,ImageTk
import random


def imgList():
    global images

    # create thumbanials of all images
    img1 = Image.open('images/one.png')
    img1.thumbnail((600, 650))  # 650 --> 550
    img2 = Image.open('images/two.png')
    img2.thumbnail((600, 650))
    img3 = Image.open('images/three.png')
    img3.thumbnail((600, 650))
    img4 = Image.open('images/four.png')
    img4.thumbnail((600, 650))
    img5 = Image.open('images/five.png')
    img5.thumbnail((600, 650))
    img6 = Image.open('images/six.png')
    img6.thumbnail((600, 650))
    # open images to use with labels
    image1 = ImageTk.PhotoImage(img1)
    image2 = ImageTk.PhotoImage(img2)
    image3 = ImageTk.PhotoImage(img3)
    image4 = ImageTk.PhotoImage(img4)
    image5 = ImageTk.PhotoImage(img5)
    image6 = ImageTk.PhotoImage(img6)
    # create list of images
    imageS = [image1, image2, image3, image4, image5, image6]
    return imageS
#image slideshow
def slideShow():
    global i, show
    if i >= (len(images) - 1):
        i = 0
        displayCanvas.config(image=images[i])
    else:
        i = i + 1
        displayCanvas.configure(image=images[i])
    show = displayCanvas.after(100, slideShow)
#run slide show
def roll():
    slideShow()
# stop slideshow
def clean():
    global show
    displayCanvas.after_cancel(show)
#stop
def stop():

    clean()
    #show random selected image
    displayCanvas.config(image=images[random.choice(range(0,6))])


if __name__ == "__main__":

    root = Tk()
    root.geometry('400x350')
    root.resizable(0, 0)
    root.title("Dice simulator")
    root.iconbitmap(r'images/dice.ico')
    root.configure(bg='#09525E')
    root.columnconfigure(2, weight=2)
    titlelbl = Label(root,text ="Roll to bet your luck",font=("Helvatical bold", 20),bg="#015567",fg="#FFFFFF")
    titlelbl.grid(row=0,columnspan=3,column=0)
    images = imgList()
    i=0
    displayCanvas = Label(root,image = images[i])
    displayCanvas.grid(row=1,column=2)


    btn1 = Button(root , text = "ROLL ON",font=("Helvatical bold", 15),bg="#0084B5", fg="white" ,width=8,command= lambda: roll())
    btn1.grid(row=2,column=2,pady=5)
    btn2 = Button(root, text="STOP",font=("Helvatical bold", 15),bg="#0084B5", fg="white", width=8,command=lambda: stop())
    btn2.grid(row=3,column=2)



    root.mainloop()

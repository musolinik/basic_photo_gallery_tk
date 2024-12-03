from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Photo Gallery")

first_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MUSOLINI\\Documents\\Python Advance\\1.jpeg"))
second_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MUSOLINI\\Documents\\Python Advance\\2.jpeg"))
third_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MUSOLINI\\Documents\\Python Advance\\3.jpeg"))
fourth_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MUSOLINI\\Documents\\Python Advance\\4.jpeg"))
fifth_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MUSOLINI\\Documents\\Python Advance\\5.jpeg"))

images = [first_image, second_image, third_image, fourth_image, fifth_image]

label = Label(image=images[0])
label.grid(row=0, column=0, columnspan=3)

def back(index):
    
    global label
    global next_button
    global back_button

    if (index == 0):
        return

    label.grid_forget()

    label = Label(image=images[index-1])
    label.grid(row=0, column=0, columnspan=3)

    next_button = Button(root, text="Next", command=lambda:next(index - 1))
    back_button = Button(root, text="Back", command=lambda:back(index-1))

    next_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    return

def next(index):
    
    global label
    global back_button
    global next_button

    if (index == 4):
        return

    label.grid_forget()

    label = Label(image=images[index + 1])
    label.grid(row=0, column=0, columnspan=3)

    back_button = Button(root, text="Back", command=lambda:back(index + 1))
    next_button = Button(root, text="Next", command=lambda:next(index + 1))

    back_button.grid(row=1,column=0)
    next_button.grid(row=1, column=2)

    return

back_button = Button(root, text="Back", command=lambda:back(0))
next_button = Button(root, text="Next", command=lambda:next(0))
exit_button = Button(root, text="Exit", command= root.quit)

back_button.grid(row=1, column=0)
next_button.grid(row=1, column=2)
exit_button.grid(row=1, column=1)

root.mainloop()
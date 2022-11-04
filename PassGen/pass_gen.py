from random import choice, randint
from tkinter import *
import string


def generate_password():
    password_min = 8
    password_max = 10
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for i in range(randint(password_min, password_max)))
    gen.delete(0, END)
    gen.insert(0, password)


window = Tk()
window.title("Password Generator")
window.minsize(480, 360)
window.geometry("720x480")
window.state("zoomed")
window.iconbitmap("amongus.ico")
window.config(background="#2d7e95")

frame = Frame(window, bg="#2d7e95")

title = Label(frame, text="Password", font=("Comic sans ms", 40), bg="#2d7e95", fg="white")
title.grid(row=0, column=0)

photo = PhotoImage(file="pass_gen.png")
image = Canvas(frame, width=300, height=300, bg="#2d7e95", bd=0, highlightthickness=0)
image.create_image(150, 150, image=photo)
image.grid(row=1, column=0)

bottom_frame = Frame(frame, bg="#2d7e95")

gen = Entry(bottom_frame, font=("Comic sans ms", 20), bg="white", fg="black")
gen.pack()

button = Button(bottom_frame, text='Generate', font=("Comic sans ms", 15), bg="black", fg="white",
                command=generate_password)
button.pack(pady=10)

bottom_frame.grid(row=2, column=0)

frame.pack(expand=YES)

author = Label(window, text="WaLiD ©\nAll rights reserved.", font=("Times New Roman", 16), bg="#2d7e95", fg="black")
author.place(relx=1, rely=1, anchor="se")

window.mainloop()

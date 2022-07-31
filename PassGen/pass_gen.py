from tkinter import *

window = Tk()
window.title("Password Generator")
window.minsize(480, 360)
window.geometry("720x480")
window.state("zoomed")
window.iconbitmap("amongus.ico")
window.config(background="#060760")

frame = Frame(window, bg="#060760")

photo = PhotoImage(file="pass_gen.png")
image = Canvas(frame, width=300, height=300, bg="#060760", bd=0, highlightthickness=0)
image.create_image(150, 150, image=photo)
image.grid(row=1, column=0)

title = Label(frame, text="Password", font=("Comic sans ms", 40), bg="#060760", fg="white")
title.grid(row=0, column=0)

frame.pack(expand=YES)

author = Label(window, text="WaLiD ©\nAll rights reserved.", font=("Times New Roman", 16), bg="#060760", fg="cyan")
author.place(relx=1, rely=1, anchor="se")

window.mainloop()

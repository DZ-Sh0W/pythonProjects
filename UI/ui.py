from tkinter import *
import webbrowser


def open_button():
    webbrowser.open_new("https://github.com/WaLiD-DK")


window = Tk()

window.title("Dicsord")
window.minsize(480, 360)
window.geometry("500x400")
window.iconbitmap("amongus.ico")
window.config(background="black")

ui_title = Label(window, text="Welcome to Dicsord !\nThe Discord new generation.", font=("Comic sans ms", 26),
                 bg="white", fg="green", bd=5, relief=RAISED)
ui_title.pack(side=TOP)

frame = Frame(window, bg="black")

ui_subtitle = Label(frame, text="Winter is coming !", font=("Comic sans ms", 20), bg="black", fg="blue")
ui_subtitle.pack()

ui_button = Button(frame, text="Click here to join Valhalla !", font=("Comic sans ms", 18), bg="white", fg="red",
                   command=open_button)
ui_button.pack()

frame.pack(expand=YES)

window.mainloop()

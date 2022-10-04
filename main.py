import webbrowser
from tkinter import *
from PIL import Image, ImageTk
from pyshorteners import Shortener
import validators
import clipboard


def clear():
    e.delete(0, "end")
    l.config(text="")


def copy():
    clipboard.copy(l.cget("text"))
    c = Label(win, text="copied!", bg="green")
    c.pack()
    win.after(2000, c.destroy())


def shorten():
    link = e.get()
    valid = validators.url(link)

    if valid:
        short = Shortener().tinyurl.short(link)
        l.config(text="Your short link is:    "+short)

    else:
        l.config(text="Invalid URL")


def go():
    url = e.get()
    short = Shortener().tinyurl.short(url)
    webbrowser.open_new_tab(short)


win = Tk()
win.title("URL Shortener")
win.geometry("700x300")

canvas= Canvas(win, width= 1000, height= 750, bg="SpringGreen")

canvas.create_text(350, 30, text="Enter your URL below -", fill="black", font=('Helvetica 15 bold'))
canvas.pack()

e = Entry(win, font=28)
e.place(relwidth=.6, rely=.2, relx=.2)

shorten_btn = Button(win, text="Shorten Link", command=shorten)
shorten_btn.place(relx=.44, rely=.35)

clear_btn = Button(win, text="Clear", command=clear)
clear_btn.place(relx=.74, rely=.35)

l = Label(win, bg="White", font=28, relief="sunken")
l.place(relwidth=.6, relx=.2, rely=.55)

open_btn = Button(win, text="Open Link", command=go)
open_btn.place(relx=.45, rely=.65)

win.mainloop()

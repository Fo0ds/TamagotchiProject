'''
    Made this to test random features for fun.
'''

from cProfile import label
from tkinter import *
from tkinter import simpledialog

def remind_user():
    window = Tk()
    window.geometry("200x30")
    window.title("Reminder")
    window.resizable(False, False)

    message = "Don't forget about your pet!"

    label = Label(window, text = message)
    label.pack()
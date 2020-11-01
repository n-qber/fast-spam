from pynput.keyboard import Controller
from time import sleep, time
from tkinter import *
from threading import Thread

def spam():
    global text, time_var
    text_to_spam = text.get("1.0", END).replace("\n", "\r\n")
    time_to_spam = time_var.get()
    time_btw_spam = time_to_spam/len(text_to_spam)

    sleep(5)

    for char in text_to_spam:
        keyboard.press(char)
        keyboard.release(char)
        sleep(time_btw_spam)

spam = Thread(target=spam).start
    

keyboard = Controller()

window = Tk()
window.title("Fast Spam")

text = Text()
text.grid(columnspan=2)

Label(text="Time:").grid(row=1, column=0)

time_var = DoubleVar()
time = Entry(textvariable=time_var)
time.grid(row=1, column=1)

spam_button = Button(text="SPAM", command=spam)
spam_button.grid(columnspan=2)

window.mainloop()

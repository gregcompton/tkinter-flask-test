
# STEP 1: Create the GUI as a Class
from tkinter import *
import time

import threading

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x350+50+50')
        self.label = Label(text="")
        self.label.pack()
        self.update_clock()

        self.displayVar = StringVar()
        self.displayLab = Label(self.root, textvariable=self.displayVar)
        self.displayLab.pack()
        self.updateDisplay('this is just a test')

        # IMPORTANT: DON'T CALL THE mainloop at initialization

    def start_mainloop(self):
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def updateDisplay(self, myString):
        self.displayVar.set(myString + '---' + time.ctime())

# create an instance of the GUI Class, but don't call mainloop in __init__
tk_app=App()
print('After tk-app=App()')

# STEP 2: create the Flask app (or define some other functions that need to reference "updater" functions
# in the GUI
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    tk_app.updateDisplay('from hello world browser')  #Note how this references the GUI Class instance
    return 'Hello, World!'

@app.route('/another')
def another_route():
    tk_app.updateDisplay('WOOHOO! It works!')
    return 'It is really working'

# STEP 3: create and start a thread for Flask (or some other blocking function).
# NOTE: the threaded function must have some condition that allows threading to work.
# Anything with a while True probably won't work
x = threading.Thread(target=app.run)
x.start()

# STEP 4: finally, start the GUI Class mainloop
tk_app.start_mainloop()


# if __name__ == '__main__':
    # app.run()
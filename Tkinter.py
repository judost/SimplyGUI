from tkinter import *

# -----------------------------------------

import logging 
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time
from datetime import datetime
from random import randint


longname = datetime.now().strftime('./Mine/logg/mylog.log_%Y%m%d.log')


LogHandler = TimedRotatingFileHandler(filename=f'{longname}', when='midnight', interval=1, encoding='utf-8')
LogHandler.setFormatter(logging.Formatter('%(asctime)s / %(message)s'))
LogHandler.suffix = "./Mine/logg/mylog.log_%Y%m%d.log"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(LogHandler)



# -----------------------------------------
'''
longname = datetime.now().strftime('./Mine/logg/mylog.log_%Y%m%d.log')

LHandler = RotatingFileHandler(f'{longname}', maxBytes=32*5, backupCount=5)
LHandler.setFormatter(logging.Formatter('%(asctime)s / %(message)s' ))
MyLogHandler = TimedRotatingFileHandler(filename=f'{longname}', when='midnight', interval=1, encoding='utf-8')
MyLogHandler.suffix = "./Mine/logg/mylog.log_%Y%m%d.log"
logger = logging.getLogger(__name__)
logger.addHandler(LHandler)
logger.setLevel(logging.DEBUG)
'''
# -----------------------------------------

mainGUI = Tk()
mainGUI.title('MyProject')
mainGUI.geometry('240x500')
mainGUI.resizable(False, False)
mainFrame = Frame(mainGUI, bg='black')
mainFrame.pack(fill='both', expand=True)


from random import randint
def Title_Update():
    ranNum = randint(0, 1000)
    label0.config(text=ranNum)
    ranNum1 = randint(0, 1000)
    label1.config(text=ranNum1)
    
    logger.debug(f'{ranNum}, {ranNum1}')
    
    mainGUI.after(1000, Title_Update)


# Title
label0=Label(mainFrame, text='Horizontal Layout', bg = 'black', padx=5, pady=5, fg='white')
label0.config(font=('Helvetica', 18))
label0.pack(fill='x')

# Horizontal Layout
Horizontal_Frame = Frame(mainFrame, bg='gray')

label4 = Label(Horizontal_Frame, text='Num1', bg ='pink', fg = 'red', padx = 5, pady = 50, relief=SUNKEN)
label4.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')   # nsew : Reactive 

label5 = Label(Horizontal_Frame, text='Num2', bg ='pink', fg = 'red', padx = 10, pady = 10, relief=GROOVE)
label5.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

label6 = Label(Horizontal_Frame, text='Num3', bg ='pink', fg = 'red', padx = 50, pady = 10, relief=FLAT)
label6.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

label7 = Label(Horizontal_Frame, text='Num4', bg ='pink', fg = 'red', padx = 10, pady = 10, relief=RAISED)
label7.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')


    # Reactive
for i in range(0,4):
    Horizontal_Frame.grid_columnconfigure(i, weight=1)

Horizontal_Frame.pack(fill='x')


# Title
label1=Label(mainFrame, text='Vertical layout', bg = 'black', padx=5, pady=5, fg = 'white')
label1.config(font=('Helvetica', 18))
label1.pack(fill='x')


# Vertical layout
Vertical_Frame=Frame(mainFrame, bg='gray')

item1=Label(Vertical_Frame, text='1. Write Something Here', bg='green', padx=20, pady=20, fg='blue', relief=RIDGE)
item1.pack(fill='x', padx=10, pady=10, side=LEFT)

item2=Label(Vertical_Frame, text='2', bg='blue', padx=20, pady=20, fg='green')
item2.pack(fill='x', padx=10, pady=10)

Vertical_Frame.pack(fill='x')


# List Box
listbox = Listbox(mainGUI, bg='skyblue')
listbox.pack(fill='x')

for i in ['1. Num1', '2. Num2', '3. Num3', '4. Num4']:
    listbox.insert(END, i)


# Update
Title_Update()

mainGUI.mainloop()

from tkinter import *
master=Tk()
demo_text="This is a sample demo of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='lightgreen', font=('time',24,'italic'))
msg.pack()

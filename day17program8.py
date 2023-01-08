from tkinter import*
import match
root=Tk()
root.title("Calculator")
e =Entry(root)
e.grid(row=0,column=0, column=6)
e.focus_set()


def clearall():
    e.delete(0,END)
def clear1():
    txt=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)
def fund0():
    txt=e.get()
    txt +'0'
    e.delete(0,END)
    e.insert(0,txt)

def fund1():
    txt=e.get()
    txt +'1'
    e.delete(0,END)
    e.insert(0,txt)
 def fund2():
    txt=e.get()
    txt +'2'
    e.delete(0,END)
    e.insert(0,txt)
def fund3():
    txt=e.get()
    txt +'3'
    e.delete(0,END)
    e.insert(0,txt)
def fund4():
    txt=e.get()
    txt +'4'
    e.delete(0,END)
    e.insert(0,txt)
def fund5():
    txt=e.get()
    txt +'5'
    e.delete(0,END)
    e.insert(0,txt)
def fund6():
    txt=e.get()
    txt +'6'
    e.delete(0,END)
    e.insert(0,txt)
def fund7():
    txt=e.get()
    txt +'7'
    e.delete(0,END)
    e.insert(0,txt)
def fund8():
    txt=e.get()
    txt +'8'
    e.delete(0,END)
    e.insert(0,txt)
def fund9():
    txt=e.get()
    txt +'9'
    e.delete(0,END)
    e.insert(0,txt)

def fundp():
    txt=e.get()
    txt +'.'
    e.delete(0,END)
    e.insert(0,txt)
def fundadd():
    txt=e.get()
    txt +'+'
    e.delete(0,END)
    e.insert(0,txt)
def fundmult():
    txt=e.get()
    txt +'*'
    e.delete(0,END)
    e.insert(0,txt)
def fundsub():
    txt=e.get()
    txt +'-'
    e.delete(0,END)
    e.insert(0,txt)
def funddiv():
    txt=e.get()
    txt +'/'
    e.delete(0,END)
    e.insert(0,txt)
def fundpow():
    txt=e.get()
    txt +'**'
    e.delete(0,END)
    e.insert(0,txt)

def fundparenthopen():
    txt=e.get()
    txt +'('
    e.delete(0,END)
    e.insert(0,txt)
def fundparenthclose():
    txt=e.get()
    txt +')'
    e.delete(0,END)
    e.insert(0,txt)

def answer():
    txt=e.get()
    e.delete(0,END)
    ans=eval(txt)
    e.insert(0,ans)   
def squreroot():
    txt=e.get
    ans=math.sqrt(float(e.get()))
    e.insert(0,ans)
def percentage():
    txt=e.get()
    e.delete(0,END)
    ANS=EVAL(txt)
    ANS=ANS/100
    E.INSERT(0,ANS)
    B1
    
    

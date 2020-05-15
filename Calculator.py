from tkinter import *

parent=Tk()
parent.title("CALCULATOR")
parent.configure(background='Light Gray')
parent.geometry('205x275')
txtin=StringVar()
operator=""
result=""
def fun1(num):
    global operator
    operator=operator+str(num)
    txtin.set(operator)

def clr():
    global operator
    txtin.set("")
    operator=""

def cal():
    global operator
    a=eval(operator)
    txtin.set(a)

display=Entry(parent,textvar=txtin,width=25,bg='light blue',bd=5,relief='ridge')
display.grid(column=1,columnspan=5,padx=7,pady=10,ipady=3)

one=Button(parent,text='1',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(1))
one.grid(row=2,column=1)
two=Button(parent,text='2',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(2))
two.grid(row=2,column=2)
three=Button(parent,text='3',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(3))
three.grid(row=2,column=3)
four=Button(parent,text='4',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(4))
four.grid(row=3,column=1)
five=Button(parent,text='5',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(5))
five.grid(row=3,column=2)
six=Button(parent,text='6',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(6))
six.grid(row=3,column=3)
seven=Button(parent,text='7',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(7))
seven.grid(row=4,column=1)
eight=Button(parent,text='8',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(8))
eight.grid(row=4,column=2)
nine=Button(parent,text='9',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(9))
nine.grid(row=4,column=3)
zero=Button(parent,text='0',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1(0))
zero.grid(row=5,column=2)
plus=Button(parent,text='+',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1('+'))
plus.grid(row=5,column=1)
minus=Button(parent,text='-',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1('-'))
minus.grid(row=5,column=3)
mul=Button(parent,text='*',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1('*'))
mul.grid(row=2,column=4)
div=Button(parent,text='/',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1('/'))
div.grid(row=3,column=4)
equal=Button(parent,text='=',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=cal)
equal.grid(row=4,column=4)
clear=Button(parent,text='Del',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=clr)
clear.grid(row=5,column=4)
point=Button(parent,text='.',pady=5,padx=5,bd=5,font=('helvetica',12,'bold'),command=lambda:fun1('.'))
point.grid(row=2,column=5,rowspan=10)
parent.mainloop()


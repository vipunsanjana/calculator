from tkinter import *

expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set(expression)
    
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""

    except:    
        equation.set("Syntax Error!")
        expression=""


gui=Tk()
gui.configure(background="light green")
gui.title("CALCULATOR")
gui.geometry("600x300")


equation=StringVar()
expression_field=Entry(gui,textvariable=equation,font=("Arial Bold",15))
expression_field.grid(columnspan=4,ipadx=189)


btn1=Button(gui,text="1",bg="yellow",fg="red",width=12,height=2,command=lambda:press(1))
btn1.grid(row=1,column=0)

btn2=Button(gui,text="2",bg="yellow",fg="red",width=12,height=2,command=lambda:press(2))
btn2.grid(row=1,column=1)

btn3=Button(gui,text="3",bg="yellow",fg="red",width=12,height=2,command=lambda:press(3))
btn3.grid(row=1,column=2)

btn4=Button(gui,text="4",bg="yellow",fg="red",width=12,height=2,command=lambda:press(4))
btn4.grid(row=2,column=0)

btn5=Button(gui,text="5",bg="yellow",fg="red",width=12,height=2,command=lambda:press(5))
btn5.grid(row=2,column=1)

btn6=Button(gui,text="6",bg="yellow",fg="red",width=12,height=2,command=lambda:press(6))
btn6.grid(row=2,column=2)

btn7=Button(gui,text="7",bg="yellow",fg="red",width=12,height=2,command=lambda:press(7))
btn7.grid(row=3,column=0)

btn8=Button(gui,text="8",bg="yellow",fg="red",width=12,height=2,command=lambda:press(8))
btn8.grid(row=3,column=1)

btn9=Button(gui,text="9",bg="yellow",fg="red",width=12,height=2,command=lambda:press(9))
btn9.grid(row=3,column=2)

btn0=Button(gui,text="0",bg="yellow",fg="red",width=12,height=2,command=lambda:press(0))
btn0.grid(row=4,column=1)

btnplus=Button(gui,text="+",bg="Maroon",fg="Lime",width=15,height=2,command=lambda:press("+"))
btnplus.grid(row=1,column=3)

btnminus=Button(gui,text="-",bg="Maroon",fg="Lime",width=15,height=2,command=lambda:press("-"))
btnminus.grid(row=2,column=3)

btnproduct=Button(gui,text="x",bg="Maroon",fg="Lime",width=15,height=2,command=lambda:press("*"))
btnproduct.grid(row=3,column=3)

btndivide=Button(gui,text="/",bg="Maroon",fg="Lime",width=15,height=2,command=lambda:press("/"))
btndivide.grid(row=4,column=3)

btnfloat=Button(gui,text=".",bg="yellow",fg="red",width=12,height=2,command=lambda:press("."))
btnfloat.grid(row=4,column=0)

btnclear=Button(gui,text="Clear",bg="yellow",fg="red",width=12,height=2,command=clear)
btnclear.grid(row=5,column=1)

btnequal=Button(gui,text="=",bg="yellow",fg="red",width=12,height=2,command=equalpress)
btnequal.grid(row=4,column=2)

gui.mainloop()

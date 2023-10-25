import tkinter 
calc=tkinter.Tk()
l=[]
z=0
def button1():
    global l
    global z
    if z==0:
        a=""
        l.append(button1["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button1["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button2():
    global l
    global z
    if z==0:
        a=""
        l.append(button2["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button2["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button3():
    global l
    global z
    if z==0:
        a=""
        l.append(button3["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button3["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)
    
def button4():
    global l
    global z
    if z==0:
        a=""
        l.append(button4["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button4["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button5():
    global l
    global z
    if z==0:
        a=""
        l.append(button5["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button5["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button6():
    global l
    global z
    if z==0:
        a=""
        l.append(button6["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button6["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button7():
    global l
    global z
    if z==0:
        a=""
        l.append(button7["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button7["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button8():
    global l
    global z
    if z==0:
        a=""
        l.append(button8["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button8["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button9():
    global l
    global z
    if z==0:
        a=""
        l.append(button9["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button9["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button10():
    global l
    global z
    if z==0:
        a=""
        l.append("*")
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append("*")
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button11():
    global l
    global z
    if z==0:
        a=""
        l.append("+")
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append("+")
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button12():
    global l
    global z
    if z==0:
        a=""
        l.append("-")
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append("-")
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button13():
    global l
    global z
    if z==0:
        a=""
        l.append("/")
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append("/")
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

def button14():
    operation=text_var.get()
    resultat=eval(operation)
    text_var.set(resultat)

def button15():
    text_var.set("")

def button16():
    global l
    global z
    if z==0:
        a=""
        l.append(button16["text"])
        for i in l:
            f=a+i
        z+=1
        text_var.set(f)
        print(f)

    else:
        a=text_var.get()
        l.append(button16["text"])
        f=a+l[-1]
        text_var.set(f)
        print(f)
        print(l)

text_var=tkinter.StringVar()


label=tkinter.Label(calc,width=30,bg="green",textvariable=text_var)
button1=tkinter.Button(calc,width=10,height=5,text="7",bg="yellow",command=button1)
button2=tkinter.Button(calc,width=10,height=5,text="8",bg="yellow",command=button2)
button3=tkinter.Button(calc,width=10,height=5,text="9",bg="yellow",command=button3)
button4=tkinter.Button(calc,width=10,height=5,text="4",bg="yellow",command=button4)
button5=tkinter.Button(calc,width=10,height=5,text="5",bg="yellow",command=button5)
button6=tkinter.Button(calc,width=10,height=5,text="6",bg="yellow",command=button6)
button7=tkinter.Button(calc,width=10,height=5,text="1",bg="yellow",command=button7)
button8=tkinter.Button(calc,width=10,height=5,text="2",bg="yellow",command=button8)
button9=tkinter.Button(calc,width=10,height=5,text="3",bg="yellow",command=button9)
button10=tkinter.Button(calc,width=10,height=5,text="x",bg="yellow",command=button10)
button11=tkinter.Button(calc,width=10,height=5,text="+",bg="yellow",command=button11)
button12=tkinter.Button(calc,width=10,height=5,text="-",bg="yellow",command=button12)
button13=tkinter.Button(calc,width=10,height=5,text="/",bg="yellow",command=button13)
button14=tkinter.Button(calc,width=10,height=5,text="=",bg="yellow",command=button14)
button15=tkinter.Button(calc,width=10,height=5,text="C",bg="yellow",command=button15)
button16=tkinter.Button(calc,width=10,height=5,text="0",bg="yellow",command=button16)

label.grid(row=0,column=0,columnspan=3)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button10.grid(row=4,column=0)
button11.grid(row=4,column=1)
button12.grid(row=4,column=2)
button13.grid(row=5,column=0)
button14.grid(row=5,column=2)
button15.grid(row=6,column=1)
button16.grid(row=5,column=1)


calc.config(bg="pink")
calc.mainloop()

from tkinter import *
def click(event):
    global scvalue
    value=event.widget.cget("text") #Gets the value of an option (aka a configuration key) from a widget.
   
    if value == "=":
       if scvalue.get().isdigit():
          value=int(scvalue.get())
       else:
          value=eval(scvalue.get()) # eval=Evaluates a string as a Python expression.

          scvalue.set(value)
          screen.update()
    elif(value=="Cut"):
       scvalue.set("")
       screen.update()
    else:
        scvalue.set(scvalue.get() + value)
        screen.update()
root=Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="light blue")
l1=Label(root,text="Simple calculator",font="Arial 10 bold")
l1.pack(anchor="nw")
scvalue=StringVar()
scvalue.set("")
#screen
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(ipadx=20,fill=X,pady=8)
#frame1
f1=Frame(root,bg="black")
numbers=["9","8","7"]
for number in numbers:
 b1=Button(f1,text=number,padx=15,pady=10)
 b1.pack(side=LEFT,padx=10,pady=4)
 b1.bind('<Button-1>',click)
f1.pack(pady=5)
#frame2    
f2=Frame(root,bg="black")
numbers=["6","5","4"]
for number in numbers:
 b2=Button(f2,text=number,padx=15,pady=10)
 b2.pack(side=LEFT,padx=10,pady=4)
 b2.bind('<Button-1>',click)
f2.pack(pady=5)
#frame3
f3=Frame(root,bg="black")
numbers=["3","2","1"]
for number in numbers:
 b3=Button(f3,text=number,padx=15,pady=10)
 b3.pack(side=LEFT,padx=10,pady=4)
 b3.bind('<Button-1>',click)
f3.pack(pady=5)

f4=Frame(root,bg="black")
numbers=["%","0","."]
for number in numbers:
 b4=Button(f4,text=number,padx=15,pady=10)
 b4.bind('<Button-1>',click)
 b4.pack(side=LEFT,padx=10,pady=4)
f4.pack(pady=5)


f5=Frame(root,bg="black")
numbers=["="]
for number in numbers:
 b5=Button(f5,text=number,padx=15,pady=10)
 b5.bind('<Button-1>',click)
 b5.pack(side=LEFT,padx=10,pady=4)
f5.pack(pady=5)



f6=Frame(root,bg="black")
numbers=["+","-","*","/","Cut"]
for number in numbers:
 b6=Button(f6,text=number,font=20,padx=10)
 b6.bind('<Button-1>',click)
 b6.pack(side=RIGHT)
 f6.pack(pady=20)

root.mainloop()
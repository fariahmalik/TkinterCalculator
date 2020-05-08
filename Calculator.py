welcome to Smart Programmer
from tkinter import *
window=Tk()
window.geometry("350x460")
window.title("Calculator")

# a text variable to store the data what ever entered in entry field.
txt=StringVar()
expression= ""
# Function to update expression
# in the text entry box
def click(num):

    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    txt.set(expression)
# Function to evaluate the final expression

def equal():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        global expression
        # e1.delete(0,END)
        add = str(eval(expression))
        txt.set(add)
        # initialize the expression variable
        # by empty string
        expression = " "

        # if error is generate then handle
        # by the except block
    except:
        expression.set("Error")
        expression=""
# defining a clear function
def clr():
    # to clear an individual entry
    global expression
    length = len(txt.get())
    e1.delete(length - 1, 'end')


def clearAll():
    # for all text to be cleared
    global expression
    expression = ""
    txt.set("")


# creating frames
frame1=Frame(window,width=390,height=100,bg="white")
frame1.pack(side=TOP)
frame2=Frame(window,width=390,height=368,bg="#F7A43A")
frame2.pack(side=BOTTOM)
# creating a label
l1=Label(frame1,text="Basic Calculator",font=("Arial Bold",20))
l1.pack(side=TOP,expand=YES)
# creating an entry field
e1=Entry(frame1,textvariable=txt,width=30,bd=10,font=("Arial Bold",12),
         fg="black",bg="#F7BD7B",relief=RIDGE,justify=RIGHT)
e1.pack(side=TOP)
e1.insert(0,"0")

# Adding buttons
# when user press the button, the command or
# function affiliated to that button is executed .
# The padx and pady attributes add extra horizontal and vertical space to the widgets.
# Python place() method in Tkinter It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window.
but1=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(7),text="7",font=("Courier New",16,'bold'))

but1.place(x=5,y=10)

but2=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(4),text="4",font=("Courier New",16,'bold'))
but2.place(x=5,y=81)

but3=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(1),text="1",font=("Courier New",16,'bold'))
but3.place(x=5,y=152)

but4=Button(frame2,padx=48,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(0),text="0",font=("Courier New",16,'bold'))
but4.place(x=5,y=223)

but5=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(8),text="8",font=("Courier New",16,'bold'))
but5.place(x=72,y=10)

but6=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(5),text="5",font=("Courier New",16,'bold'))
but6.place(x=72,y=81)

but7=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(2),text="2",font=("Courier New",16,'bold'))
but7.place(x=72,y=152)

but8=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click("."),text=".",font=("Courier New",16,'bold'))
but8.place(x=139,y=223)

but9=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
            command=lambda:click(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=139,y=10)

but10=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click(6), text="6", font=("Courier New", 16,'bold'))
but10.place(x=139,y=81)

but11=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click(3),text="3",font=("Courier New",16,'bold'))
but11.place(x=139,y=152)

but12=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click("+"),text="+",font=("Courier New",16,'bold'))
but12.place(x=205,y=10)

but13=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click("-"),text="-",font=("Courier New",16,'bold'))
but13.place(x=205,y=81)

but14=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click("*"),text="x",font=("Courier New",16,'bold'))
but14.place(x=205,y=152)

but15=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#F78C19',
             command=lambda:click("/"),text="/",font=("Courier New",16,'bold'))
but15.place(x=205,y=223)

but16=Button(frame2,padx=14,pady=84,bd=4,fg="black",bg='#F78C19',
             command=clr,text="CE",font=("Courier New",16,'bold'))
but16.place(x=270,y=10)

but17=Button(frame2,padx=153,pady=14,bd=4,fg="black",bg='#F78C19',
             command=equal,text="=",font=("Courier New",16,'bold'))
but17.place(x=5,y=294)

but18=Button(frame2,padx=14,pady=14,bd=4,fg="black",bg='#F78C19',
             command=clearAll,text="CA",font=("Courier New",16,'bold'))
but18.place(x=270,y=223)
# start the GUI
window.mainloop()

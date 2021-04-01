from tkinter import *
#if you are only using one piece of functionality its good to just type import tkinter
#however its better to use from tkinter import * if you are using a lot of different functions
#this prevents you from having to type tkinter.label() tkinter.Button() etc

window = Tk()
window.title("GUI")
window.minsize(width=500, height = 300)


#label- create it and say how it will be laid out


my_label = Label(text="label", font=("Arial", 22, "bold"))
#without pack the label will not appear
my_label.pack(side="top")

my_label.config(text="new text")

#button
def button_clicked():
    #to capture what is typed lines 23-24
    new_text= input.get()
    my_label.config(text= new_text)
    print("i got clicked")

button = Button(text="click me", command=button_clicked) #when calling a function as method you do not need ()
button.pack()

#entry
input = Entry(width = 10)
input.pack()













window.mainloop()
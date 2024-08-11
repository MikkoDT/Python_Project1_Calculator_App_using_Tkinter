from tkinter import *
import tkinter.font as tkFont

root = Tk()
custom_font = tkFont.Font(family="Helvetica",size=14)
display = Entry(root,width=40,font=custom_font)
display.grid(row=1,columnspan=6)

counter =1
for x in range(3):
    for y in range(3):
        button = Button(root,text=counter,width=7,height=2,font=custom_font)
        button.grid(row=x+2,column=y)
        counter+=1

button  = Button(root,text="0",width=7,height=2,font=custom_font)
button.grid(row=5,column=1)

count = 0
operations = ['+','-','*','/',"*3.14","%","(","**",")","**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root,text=operations[count],width=7,height=2,font=custom_font)
            count+=1
            button.grid(row=x + 2, column=y + 3)



root.mainloop()
from tkinter import *
import tkinter.font as tkFont

i = 0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

root = Tk()
custom_font = tkFont.Font(family="Helvetica",size=14)
display = Entry(root,width=40,font=custom_font)
display.grid(row=1,columnspan=6)

numbers = [1,2,3,4,5,6,7,8,9]

counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=button_text,width=7,height=2,font=custom_font,command=lambda text=button_text:get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1

button  = Button(root,text="0",width=7,height=2,font=custom_font,command=lambda :get_number(0))
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
from tkinter import *


gui = Tk()
gui.title('Temperature Convector')
gui.minsize(width=300, height=400)

celcius_var= IntVar
fahrenheit_var =IntVar


l1=LabelFrame(gui,text='Celsius To Fahrenheit',padx=20, pady=20)
l1.grid(row=2, column=0)
E1=Entry(l1,state='disable')
E1.grid(row=4, column=0)

def Cel_Active():
    E2.configure(state='disable')
    E1.configure(state='normal')

btn_active=Button(gui,text='Activate -Celsius to Fahrenheit', command=Cel_Active)
btn_active.grid(row=6, column=0)

l2=LabelFrame(gui, text='Fahrenheit to Celsius',padx=20, pady=20)
l2.grid(row=2, column=5)
E2=Entry(l2,state='disable')
E2.grid(row=4, column=5)

def Far_Active():
    E1.configure(state='disable')
    E2.configure(state='normal')
btn_active1=Button(gui,text='Activate -Fahrenheit to Celsius', command=Far_Active)
btn_active1.grid(row=6, column=5)



def exit():
    gui.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=13, column=2)

def convert_C():
    if E1:
        celcius = float(E1.get())
        fahrenheit = (celcius*9/5)+32
        result_entry.insert(0, str(fahrenheit))

def convert_f():
    if E2:
        fahrenheit = float(E2.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.insert(0, celcius)

result_bnt=Button(gui, text='Convert Celsius-Fahrenheit',command=convert_C)
result_bnt.grid(row=7, column=1)


result_bnt2=Button(gui, text='Convert Fahrenheit-Celsius',command=convert_f)
result_bnt2.grid(row=7, column=4)
result_entry=Entry(gui, bg='green')
result_entry.grid(row=8, column=2)


def Clear():
    E1.configure(state="disable")
    E2.configure(state="disable")
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)
Clear_btn=Button(gui, text='Clear',command=Clear)
Clear_btn.grid(row=9, column=2)

gui.mainloop()

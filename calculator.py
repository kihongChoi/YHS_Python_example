import tkinter as tk
import time
import random

window = tk.Tk()

window.title('Calculator')
window.geometry('400x400')
window.resizable(False,False)
label=tk.Label(window,text='Complex variable 1 :')
label.place(x=50,y=100)
label2=tk.Label(window,text='Complex variable 2 :')
label2.place(x=50,y=130)
label3=tk.Label(window,text='Output')
label3.place(x=100,y=290)
label4=tk.Label(window,text='+j')
label4.place(x=275,y=100)
label5=tk.Label(window,text='+j')
label5.place(x=275,y=130)
label6=tk.Label(window,text='Time')
label6.place(x=100,y=310)

button=tk.Button(window,width=10,height=1,text='Calculate',command=lambda:calculate())
button.place(x=200,y=250)
button2=tk.Button(window,width=10,height=1,text='Close',command=window.destroy)
button2.place(x=200,y=350)
button3=tk.Button(window,width=10,height=1,text='Reset',command=lambda:clear())
button3.place(x=100,y=350)

entry=tk.Entry(window,width=7)
entry.place(x=200,y=100)
entry2=tk.Entry(window,width=7)
entry2.place(x=310,y=100)
entry3=tk.Entry(window,width=7)
entry3.place(x=200,y=130)
entry4=tk.Entry(window,width=7)
entry4.place(x=310,y=130)
entry5=tk.Entry(window,width=10)
entry5.place(x=200,y=290)
entry6=tk.Entry(window,width=10)
entry6.place(x=200,y=310)

RadioVariety=tk.IntVar()

radio=tk.Radiobutton(window,text='Sum',value=1,variable=RadioVariety)
radio.place(x=100,y=200)
radio2=tk.Radiobutton(window,text='Subtract',value=2,variable=RadioVariety)
radio2.place(x=190,y=200)
radio3=tk.Radiobutton(window,text='Multiply',value=3,variable=RadioVariety)
radio3.place(x=290,y=200)

def calculate():
    i=0
    start=time.time()
    while i<100:
        number1=random.randint(0,65535)
        number2=random.randint(0,65535)
        number3=random.randint(0,65535)
        number4=random.randint(0,65535)
        entry.delete(0,'end')
        entry.insert(0,number1)
        entry2.delete(0, 'end')
        entry2.insert(0, number2)
        entry3.delete(0, 'end')
        entry3.insert(0, number3)
        entry4.delete(0, 'end')
        entry4.insert(0, number4)
        front=0
        back=0
        if RadioVariety.get()==1:
            front=number1+number3
            back=number2+number4
            result=str(front)+'+j'+str(back)
            entry5.delete(0,'end')
            entry5.insert(0,result)
        if RadioVariety.get()==2:
            front=number1-number3
            back=number2-number4
            result = str(front) + '+j' + str(back)
            entry5.delete(0,'end')
            entry5.insert(0,result)
        if RadioVariety.get()==3:
            front=(number1*number3)-(number2*number4)
            back=(number1*number4)+(number2*number3)
            result = str(front) + '+j' + str(back)
            entry5.delete(0,'end')
            entry5.insert(0,result)
        i+=1
    end=time.time()
    entry6.delete(0,'end')
    entry6.insert(0,end-start)

def clear():
    entry.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(0,'end')
    entry5.delete(0,'end')
    entry6.delete(0,'end')

window.mainloop()
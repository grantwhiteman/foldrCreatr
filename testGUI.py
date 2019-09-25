#! python3
import tkinter
from tkinter import *

##def printt(): #printt command for button
##    print('Demo tkinter')

def exit1():
    exit()

window = Tk()
window.geometry('600x300')
window.title('Welcome')

label1=Label(window,text='Welcome to FolderMakerLite',fg='black',bg='white',relief='flat',font=('arial',16,'bold')).pack()
#label1.place(x=90,y=53)

label2=Label(window,text='Client name',fg='black',bg='white',relief='solid',font=('arial',10,'bold'))
label2.place(x=90,y=30)

label3=Label(window,text='Test number',fg='black',bg='white',relief='solid',font=('arial',10,'bold'))
label3.place(x=90,y=60)

button1=Button(window,text='Produce fucking folder',fg='black',bg='red',relief='ridge',font=('arial',10,'bold'))
button1.place(x=90,y=150)

button2=Button(window,text='Just fuck off',fg='black',bg='red',relief='ridge',font=('arial',10,'bold'), command=exit1)
button2.place(x=90,y=200)



##window.mainloop()

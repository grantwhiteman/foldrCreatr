#! python3

# TODO:
# Change logo file
# insert inpute for client name and test number
# insert inputs for test standard and furnace size
# insert code that actually fucking does something

import tkinter, shutil, os
from tkinter import *
import PIL
from PIL import Image,ImageTk #pip install pillow


root = Tk()
root.geometry ('555x555')
root.title('imgeCFR')

imge=Image.open(r'C:\Users\Grant\Pictures\logo.png');
photo=ImageTk.PhotoImage(imge);

lab=Label(image=photo);
lab.pack();


fn=StringVar()
ln=StringVar()
var1=StringVar()
var2=StringVar()

def exit1():
    exit()
def printt(): #printt command for button
    clientName=fn.get()
    testNo=ln.get()
    testStd=var1.get()
    testScl=var2.get()
    print(f'The test code (and folder name) is {clientName}{testNo}')
    print(f'This is a {testScl} {testStd} test')

''
def makeFoldr():
    clientName=fn.get()
    testNo=ln.get()
    testStd=var1.get()
    testScl=var2.get()
    folderName = clientName + ' ' + testNo;
    folDir = ('R:\TEST REPORTS DATA PHOTOS\\' + folderName)
    os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName);
    os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
    os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\Survey Photos');
    os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\Test Photos');
    os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\Obsolete');
    if testScl == 'Full':
        if testStd == 'BS':
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Ful Furnace\BS Test\Data Template Master BS Ful.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
        else:
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Ful Furnace\EN Test\Data Template Master EN Ful.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
    else:
        if testStd == 'BS':
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Med Furnace\BS Test\Data Template Master Med BS.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
        else:
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Med Furnace\EN Test\Data Template Master EN Med.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
    os.startfile(folDir)

                




##window = Tk()
##window.geometry('600x300')
##window.title('Welcome')

#Create title
label1=Label(root,text='Welcome to FolderMakerLite',fg='black',bg='white',relief='flat',font=('arial',16,'bold')).pack()
#label1.place(x=90,y=53)

#Client name: text
label2=Label(root,text='Client name:',fg='black',bg='white',relief='flat',font=('arial',10,'bold'))
label2.place(x=90,y=190)

#Client name user entry
entry1=Entry(root,textvar=fn)
entry1.place (x=240, y=190)

#Test number: text
label3=Label(root,text='Test number:',fg='black',bg='white',relief='flat',font=('arial',10,'bold'))
label3.place(x=90,y=220)

#Test number user entry
entry2=Entry(root,textvar=ln)
entry2.place (x=240, y=220)

#Test standard: text
label4=Label(root,text='Test standard:',fg='black',bg='white',relief='flat',font=('arial',10,'bold'))
label4.place(x=90,y=250)

#Test standard dropbox
list1=['BS','EN']
droplist=OptionMenu(root,var1,*list1)
var1.set('Select standard')
droplist.config(width=15)
droplist.place(x=240, y=250)

#Furnace: text
label5=Label(root,text='Furnace:',fg='black',bg='white',relief='flat',font=('arial',10,'bold'))
label5.place(x=90,y=280)

#Furnace: dropbox
list2=['Med','Full']
droplist=OptionMenu(root,var2,*list2)
var2.set('Select standard')
droplist.config(width=15)
droplist.place(x=240, y=280)

button1=Button(root,text='Produce folder',fg='black',bg='red',relief='ridge',font=('arial',10,'bold'),command=makeFoldr)
button1.place(x=90,y=350)

button2=Button(root,text='Close',fg='black',bg='red',relief='ridge',font=('arial',10,'bold'), command=exit1)
button2.place(x=350,y=350)


##
##root.mainloop()

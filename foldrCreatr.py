#Python 3.7.2
#Folder creatr
import shutil, os
os.chdir('R:\TEST REPORTS DATA PHOTOS')
print('Client name:');
clientName = input();
print('Test Number:');
testNo = input();
while True:
        print('Test standard: (BS/EN)');
        testStd = input();
        if testStd=='BS':
                break
        elif testStd=='EN':
                break
        else:
                print('please enter BS or EN');

while True:
        print('Furnace scale: (M/F)');
        testScl = input();
        if testScl=='M':
                break
        elif testScl=='F':
                break
        else:
                print('please enter M or F');

folderName = clientName + ' ' + testNo;
os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName);
os.makedirs('R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
if testScl == 'F':
        if testStd == 'BS':
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Ful Furnace\BS Test\Data Template Master BS Ful.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
        else:
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Ful Furnace\EN Test\Data Template Master EN Ful.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
else:
        if testStd == 'BS':
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Med Furnace\BS Test\Data Template Master Med BS.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');
        else:
                shutil.copy('R:\Templates and Forms CURRENT\Templates for Report writing\Test Data Sheets\Data Sheets\Med Furnace\EN Test\Data Template Master EN Med.xlsx', 'R:\TEST REPORTS DATA PHOTOS\\' + folderName +'\data');

                



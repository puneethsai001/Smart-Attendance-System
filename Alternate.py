import pandas as pd
from tkinter import filedialog as fd
import datetime as dt

unknown_fp = fd.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
if not unknown_fp:
    print("[Log 0] No input File: Code Terminated")
    exit()

from deepface import DeepFace

print(unknown_fp)

df = pd.read_csv('Student.csv', delimiter=',')

presentees=[]
absentees=[]

dateObj = dt.datetime.now()
dateStr = str(dateObj.date())

pfname = 'Presentees '+dateStr+'.csv'
afname = 'Absentees '+dateStr+'.csv'

print('[Log 0] Verifying')

for index, row in df.iterrows():
    if index == 4:
        print("[Log 1] Half Done Succesfully")

    StudPath = row['File Path']

    result = DeepFace.verify(img1_path = StudPath, img2_path = unknown_fp)

    if result.get('verified') == True:
        presentees.append([row['Reg No'],row['Name']])

    else:
        absentees.append([row['Reg No'],row['Name']])

pr_df = pd.DataFrame(columns=['Reg No','Name'])
abs_df = pd.DataFrame(columns=['Reg No','Name'])

for i in presentees:
    pr_df.loc[len(pr_df)] = i

for j in absentees:
    abs_df.loc[len(abs_df)] = j

print('[Log 3] Updated the data frames')

pr_df.to_csv(pfname, sep=',', index=False, encoding='utf-8')
abs_df.to_csv(afname, sep=',', index=False, encoding='utf-8')

print('[Log 4] Flushed the data to CSV files')

print('[Log 5] Attenadance Success')
print('Presentees File: ',pfname)
print('Absentees File: ', afname)
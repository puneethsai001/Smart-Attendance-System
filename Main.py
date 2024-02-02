import pandas as pd
from tkinter import filedialog as fd
import datetime as dt

unknown_fp = fd.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])

import face_recognition as fr

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

    knownImage = fr.load_image_file(StudPath)
    unknownImage = fr.load_image_file(unknown_fp)

    knownEncoding = fr.face_encodings(knownImage)[0]
    unknownEncoding = fr.face_encodings(unknownImage)

    for i in range(0,len(unknownEncoding)):
        results = fr.compare_faces([knownEncoding], unknownEncoding[i])
        
        if results[0] == True:
            presentees.append([row['Reg No'],row['Name']])
            break
        
    list = [row['Reg No'],row['Name']]

    if list not in presentees:
        absentees.append(list)

pr_df = pd.DataFrame(columns=['Reg No','Name'])
abs_df = pd.DataFrame(columns=['Reg No','Name'])

print('[Log 2] Created new data frames')

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
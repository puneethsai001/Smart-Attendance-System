import pandas as pd
from tkinter import filedialog as fd

unknown_fp = fd.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])

from deepface import DeepFace

df = pd.read_csv('Student.csv', delimiter=',')

presentees=[]
absentees=[]

print('Verifying...')

for index, row in df.iterrows():
    StudPath = row['File Path']
    result = DeepFace.verify(img1_path = StudPath, img2_path = "Reference Images\Richard_Kit.jpg")
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

pr_df.to_csv('Presentees.csv', sep=',', index=False, encoding='utf-8')
abs_df.to_csv('Absentees.csv', sep=',', index=False, encoding='utf-8')

print('Success')

        

        
import face_recognition as fr
import pandas as pd

df = pd.read_csv('Student.csv', delimiter=',')

presentees=[]
absentees=[]

for index, row in df.iterrows():
    StudPath = row['File Path']

    knownImage = fr.load_image_file(StudPath)
    unknownImage = fr.load_image_file("Reference Images\Scarlet_Chris.jpg")

    knownEncoding = fr.face_encodings(knownImage)[0]
    unknownEncoding = fr.face_encodings(unknownImage)

    for i in range(0,len(unknownEncoding)):
        results = fr.compare_faces([knownEncoding], unknownEncoding[i])
        
        if results[0] == True:
            presentees.append([row["Reg No"],row["Name"]])
            break
        
    list = [row["Reg No"],row["Name"]]

    if list not in presentees:
        absentees.append(list)

pr_df = pd.DataFrame(columns=["Reg No","Name"])
abs_df = pd.DataFrame(columns=["Reg No","Name"])

for i in presentees:
    pr_df.loc[len(pr_df)] = i

for j in absentees:
    abs_df.loc[len(abs_df)] = j

pr_df.to_csv("Presentees.csv", sep=',', index=False, encoding='utf-8')
abs_df.to_csv("Absentees.csv", sep=',', index=False, encoding='utf-8')

print("Success")
#This file is only for testing certain functions and not a part of the project
import pandas as pd
import face_recognition as fr

df = pd.read_csv('Student.csv', delimiter=',')

presentees=[]
absentees=[]

print('[Log 0] Verifying')

unknownImage = fr.load_image_file("Reference Images\Richard_Kit.jpg")
unknownEncoding = fr.face_encodings(unknownImage)

peopleCount = range(0,len(unknownEncoding))
peopleCount = list(peopleCount)

for index, row in df.iterrows():
    if index == 4:
        print("[Log 1] Half Done Succesfully")

    StudPath = row['File Path']

    knownImage = fr.load_image_file(StudPath)
    knownEncoding = fr.face_encodings(knownImage)[0]


    for i in peopleCount:
        results = fr.compare_faces([knownEncoding], unknownEncoding[i])
        
        if results[0] == True:
            peopleCount.remove(i)
            presentees.append([row['Reg No'],row['Name']])
            break
        
    list = [row['Reg No'],row['Name']]

    if list not in presentees:
        absentees.append(list)

print('Presentees:')
for i in presentees:
    print(i[0],' ',i[1])
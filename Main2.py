import face_recognition
import pandas as pd

df = pd.read_csv('Student.csv', delimiter=',')

for index, row in df.iterrows():
    StudPath = row['File Path']

    knownImage = face_recognition.load_image_file(StudPath)
    unknownImage = face_recognition.load_image_file("Reference Images\Daniel_Emma_Rupert.jpg")

    knownEncoding = face_recognition.face_encodings(knownImage)[0]
    unknownEncoding = face_recognition.face_encodings(unknownImage)

    for i in range(0,len(unknownEncoding)):
        results = face_recognition.compare_faces([knownEncoding], unknownEncoding[i])
        if results[0] == True:
            print(row['Name'])
            break

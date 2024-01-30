import pandas as pd
from deepface import DeepFace

df = pd.read_csv('Student.csv', delimiter=',')
for index, row in df.iterrows():
    StudPath = row['File Path']
    result = DeepFace.verify(img1_path = StudPath, img2_path = "Reference_Images\Scarlet_Chris.jpg")
    if result.get('verified') == True:
        print(row['Name'])


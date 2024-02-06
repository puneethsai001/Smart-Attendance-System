import pandas as pd
from tkinter import filedialog as fd
import datetime as dt
import concurrent.futures
import face_recognition as fr

unknown_fp = fd.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])

print(unknown_fp)

df = pd.read_csv('Student.csv', delimiter=',')

presentees = []
absentees = []

dateObj = dt.datetime.now()
dateStr = str(dateObj.date())

pfname = 'Presentees ' + dateStr + '.csv'
afname = 'Absentees ' + dateStr + '.csv'

print('[Log 0] Verifying')

unknownImage = fr.load_image_file(unknown_fp)
unknownEncoding = fr.face_encodings(unknownImage)

peopleCount = range(0, len(unknownEncoding))
peopleCount = list(peopleCount)

def compare_faces_with_index(index, row, unknown_encoding):
    StudPath = row['File Path']
    known_encoding = fr.face_encodings(fr.load_image_file(StudPath))[0]
    
    result = fr.compare_faces([known_encoding], unknown_encoding[index])
    
    if result[0]:
        return [row['Reg No'], row['Name']]
    else:
        return None

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(
        lambda i: compare_faces_with_index(i, row, unknownEncoding),
        peopleCount
    ))

presentees = [result for result in results if result is not None]

pr_df = pd.DataFrame(columns=['Reg No', 'Name'])
abs_df = pd.DataFrame(columns=['Reg No', 'Name'])

print('[Log 2] Created new data frames')

for i in presentees:
    pr_df.loc[len(pr_df)] = i

# Assuming you want to add absentees to abs_df, adjust this loop accordingly
for j in absentees:
    abs_df.loc[len(abs_df)] = j

print('[Log 3] Updated the data frames')

pr_df.to_csv(pfname, sep=',', index=False, encoding='utf-8')
abs_df.to_csv(afname, sep=',', index=False, encoding='utf-8')

print('[Log 4] Flushed the data to CSV files')

print('[Log 5] Attendance Success')
print('Presentees File: ', pfname)
print('Absentees File: ', afname)

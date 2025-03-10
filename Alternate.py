import pandas as pd
import face_recognition as fr
from tkinter import filedialog as fd
from multiprocessing import Pool, cpu_count

class FaceRecognitionAttendance:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, delimiter=',')
        self.presentees = []
        self.absentees = []
        
    def load_and_encode(self, image_path):
        """Loads an image and returns its face encodings."""
        image = fr.load_image_file(image_path)
        encodings = fr.face_encodings(image)
        return encodings[0] if encodings else None
    
    def verify_faces(self, student_data):
        """Compares student face encodings with the unknown image."""
        reg_no, name, stud_path, unknown_encodings = student_data
        known_encoding = self.load_and_encode(stud_path)
        
        if known_encoding is None:
            return None  # Skip students whose faces couldn't be encoded
        
        for unknown_encoding in unknown_encodings:
            if fr.compare_faces([known_encoding], unknown_encoding)[0]:
                return (reg_no, name, True)
        return (reg_no, name, False)

    def process_attendance(self, unknown_fp):
        """Processes attendance by verifying student faces in parallel."""
        unknown_encodings = fr.face_encodings(fr.load_image_file(unknown_fp))
        if not unknown_encodings:
            print("[Error] No face detected in the unknown image.")
            return
        
        student_data = [(row['Reg No'], row['Name'], row['File Path'], unknown_encodings) for _, row in self.df.iterrows()]
        
        with Pool(processes=cpu_count()) as pool:
            results = pool.map(self.verify_faces, student_data)
        
        for result in results:
            if result is None:
                continue
            reg_no, name, present = result
            if present:
                self.presentees.append([reg_no, name])
            else:
                self.absentees.append([reg_no, name])
        
    def save_results(self):
        """Saves presentees and absentees to CSV files."""
        pd.DataFrame(self.presentees, columns=['Reg No', 'Name']).to_csv('Presentees.csv', index=False)
        pd.DataFrame(self.absentees, columns=['Reg No', 'Name']).to_csv('Absentees.csv', index=False)
        print("Attendance processed successfully")
        print("Presentees File: Presentees.csv")
        print("Absentees File: Absentees.csv")

if __name__ == "__main__":
    unknown_fp = fd.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if not unknown_fp:
        print("No input File: Code Terminated")
        exit()
    
    attendance = FaceRecognitionAttendance('Student.csv')
    attendance.process_attendance(unknown_fp)
    attendance.save_results()
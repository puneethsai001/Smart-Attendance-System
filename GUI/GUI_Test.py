from tkinter import *
from tkinter import filedialog
import pandas as pd
import datetime as dt
import face_recognition as fr
import sys

processed_files = None  

def process_image(filepath=None):
    global processed_files  

    if filepath is None:
        filepath = filedialog.askopenfilename(title='Choose Your Image!')
        if not filepath:
            print("[Log 0] No input File: Code Terminated")
            return

    print(filepath)
    df = pd.read_csv('Student.csv', delimiter=',')
    presentees = []
    absentees = []
    dateObj = dt.datetime.now()
    dateStr = str(dateObj.date())
    pfname = 'Presentees ' + dateStr + '.csv'
    afname = 'Absentees ' + dateStr + '.csv'
    print('[Log 0] Verifying')

    unknownImage = fr.load_image_file(filepath)
    unknownEncoding = fr.face_encodings(unknownImage)

    peopleCount = list(range(0,len(unknownEncoding)))

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
                presentees.append([row['Reg No'], row['Name']])
                break

        row_list = [row['Reg No'], row['Name']] 

        if row_list not in presentees:
            absentees.append(row_list)

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

    print('[Log 5] Attendance Success')
    print('Presentees File: ', pfname)
    print('Absentees File: ', afname)

    
    processed_files = (pfname, afname)

def download_presentees(filename, download_location):
    presentees_file = filedialog.asksaveasfilename(defaultextension=".csv", initialdir=download_location, filetypes=[("CSV files", "*.csv")])
    if not presentees_file:
        return
    with open(filename, 'rb') as f_in:
        with open(presentees_file, 'wb') as f_out:
            f_out.write(f_in.read())

def download_absentees(filename, download_location):
    absentees_file = filedialog.asksaveasfilename(defaultextension=".csv", initialdir=download_location, filetypes=[("CSV files", "*.csv")])
    if not absentees_file:
        return
    with open(filename, 'rb') as f_in:
        with open(absentees_file, 'wb') as f_out:
            f_out.write(f_in.read())

def download():
    global processed_files  
    if processed_files is None:
        print("Please process an image first!")
        return

    pfname, afname = processed_files
    
   
    download_location = filedialog.askdirectory(title="Select Download Location")
    
    if download_location:
        
        download_presentees(pfname, download_location)
        download_absentees(afname, download_location)

gui = Tk()

icon = PhotoImage(file='GUI/logo.png')
button_image = PhotoImage(file='GUI/click.png')
download_image = PhotoImage(file='GUI/download.png')

gui.geometry("900x900")
gui.title("Smart Attendance System")
gui.iconphoto(True, icon)
gui.config(background="#121212")

canvas = Canvas(gui, width=900, height=900, bg="#121212", highlightthickness=0)
canvas.pack(fill="both", expand=True)

background_photo = PhotoImage(file='GUI/background.png')
canvas.create_image(0, 0, image=background_photo, anchor='nw')

label = Label(gui,
              text="Smart Attendance System",
              font=('Elianto', 25, 'bold'),
              fg='white',
              bg='#121212')
label.place(x=250, y=100)

def openfile():
    process_image()

button = Button(gui,
                text='Choose Image!',
                font=('Comic Sans', 18, 'bold'),
                fg='#00FF00',
                bg='black',
                activeforeground='black',
                activebackground='white',
                image=button_image,
                compound='right',
                command=openfile)
button.place(x=330, y=200)

download_button = Button(gui,
                         text='Download Presentees and Absentees file!',
                         font=('Comic Sans', 18, 'bold'),
                         fg='#00FF00',
                         bg='black',
                         activeforeground='black',
                         activebackground='white',
                         image=download_image,
                         compound='right',
                         command=download)
download_button.place(x=200, y=400)

menubar = Menu(gui, background='red', fg='white')
gui.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label="", menu=filemenu)

gui.mainloop()

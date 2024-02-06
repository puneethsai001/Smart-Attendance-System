from tkinter import *
from tkinter import filedialog

def resize_background(event):
    global background_photo
    global background_id
    canvas.coords(background_id, 0, 0)  
    canvas.itemconfig(background_id, image=background_photo) 


gui= Tk()

icon=PhotoImage(file='GUI/logo.png')
button_image=PhotoImage(file='GUI/Screenshot 2024-02-06 170703.png')
download_image=PhotoImage(file='GUI/Screenshot 2024-02-06 170417.png')

gui.geometry("900x900")
gui.title("Smart Attendance System")
gui.iconphoto(True,icon)
gui.config(background="#121212")


canvas = Canvas(gui, width=900, height=900, bg="#121212", highlightthickness=0)
canvas.pack(fill="both", expand=True)


background_photo = PhotoImage(file='GUI/black-background-08-vecteezy.png')
canvas.create_image(0, 0, image=background_photo, anchor='nw')

canvas.bind('<Configure>', resize_background)



label=Label(gui,
            text="Smart Attendance System",
            font=('Elianto',25,'bold'),
            fg='white',
            bg='#121212')

label.place(x=250,y=100)

def openfile():
    filepath= filedialog.askopenfilename(title='Choose Your Image!')
    print(filepath)

button=Button(gui,
              text='Choose Image!',
              font=('Comic Sans',18,'bold'),
              fg='#00FF00',
              bg='black',
              activeforeground='black',
              activebackground='white',
              image=button_image,
              compound='right',
              command=openfile)

button.place(x=330,y=200)

download=Button(gui,
              text='Download Presentees and Absentees file!',
              font=('Comic Sans',18,'bold'),
              fg='#00FF00',
              bg='black',
              activeforeground='black',
              activebackground='white',
              image=download_image,
              compound='right')

download.place(x=200,y=400)

menubar=Menu(gui,background='red',fg='white')
gui.config(menu=menubar)

filemenu=Menu(menubar)
menubar.add_cascade(label="   ",menu=filemenu)







gui.mainloop()
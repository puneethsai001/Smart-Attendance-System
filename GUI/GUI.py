from tkinter import *
from tkinter import filedialog




gui= Tk()

icon=PhotoImage(file='GUI/logo.png')
button_image=PhotoImage(file='GUI/click.png')
download_image=PhotoImage(file='GUI/download.png')

gui.geometry("900x900")
gui.title("Smart Attendance System")
gui.iconphoto(True,icon)
gui.config(background="#121212")


canvas = Canvas(gui, width=900, height=900, bg="#121212", highlightthickness=0)
canvas.pack(fill="both", expand=True)


background_photo = PhotoImage(file='GUI/background.png')
canvas.create_image(0, 0, image=background_photo, anchor='nw')





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
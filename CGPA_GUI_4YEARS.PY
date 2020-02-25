from tkinter import *
from tkinter import messagebox
def cgpa():
    try:
        cond=int(e3.get())
        if cond==1:
            root1.destroy()
            import CGPA_GUI_1
        elif cond==2:
            root1.destroy()
            import CGPA_GUI
        elif cond==3:
            root1.destroy()
            import CGPA_GUI_3
        elif cond==4:
            root1.destroy()
            import CGPA_GUI_4
        else:
            messagebox.showerror("error",'enter valid year of btech')
    except  ValueError as e:
        messagebox.showerror("error",'enter a valid year')

root1=Tk()
root1.geometry('400x400')
#root1.configure(background="blue")
Label(root1,text="enter year").grid(row=0,column=0)
e3=Entry(root1)
e3.grid(row=0,column=1)
Button(root1,text="Go",command=cgpa).grid(row=1,column=1)
root1.mainloop()

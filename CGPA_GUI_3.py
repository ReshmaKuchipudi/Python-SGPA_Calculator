from tkinter import *
from tkinter import messagebox
def find():
    a=e.get().split()
    b=e1.get().split()
    sum=0
    sum1=0
    size=len(a)
    if(size==5 and len(b)==3):
        for i in a:
            if(i=='o' or i=='O' or i=='s' or i=='S' or i=='a' or i=='A' or i=='b' or i=='B' or i=='c' or i=='C' or i=='d' or i=='D' or i=='f' or i=='F'):
                if i=='O' or i=='o':
                    sum=sum+(10*3)
                elif i=='S' or i=='s':
                    sum=sum+(9*3)
                elif i=='A' or i=='a':
                    sum=sum+(8*3)
                elif i=='B' or i=='b':
                    sum=sum+(7*3)
                elif i=='C' or i=='c':
                    sum=sum+(6*3)
                elif i=='D'or i=='d':
                    sum=sum+(5*3)
                elif i=='F'or i=='f':
                    sum=sum+(0*3)
            else:
                messagebox.showerror("Error","Enter valid grades in subjects")
                return
        for j in b:
            if(j=='o' or j=='O' or j=='s' or j=='S' or j=='a' or j=='A' or j=='b' or j=='B' or j=='c' or j=='C' or j=='d' or j=='D' or j=='f' or j=='F'):
                if j=='O'or j=='o':
                    sum1=sum1+(10*2)
                elif j=='S'or j=='s':
                     sum1=sum1+(9*2)
                elif j=='A'or j=='a':
                    sum1=sum1+(8*2)
                elif j=='B'or j=='b':
                    sum1=sum1+(7*2)
                elif j=='C'or j=='c':
                    sum1=sum1+(6*2)
                elif j=='D'or j=='d':
                    sum1=sum1+(5*2)
                elif j=='F' or j=='f':
                     sum1=sum1+(0*2)
            else:
                messagebox.showerror("Error","Enter valid grades in labs")
                return
        d=(sum+sum1)/21
        res.set(d)
    else:
        messagebox.showerror("Error","Enter 5 subjects grades and 3 labs grades")
root=Tk()
root.geometry('400x400')
root.title("CGPA")
Label(root,text="enter grade of subjects").grid(row=0,column=0)
e=Entry(root)
e.grid(row=0,column=1)
Label(root,text="enter grades of lab").grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)
Button(root,text='grade',command=find).grid(row=2,column=1)
res=DoubleVar()
res.set("")
Label(root,textvariable=res,bg='white',fg='black',padx=60).grid(row=3,column=1)
root.mainloop()


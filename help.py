from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student



class Help_center:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #first img
        img=Image.open(r"college_images\clg2.jpg")
        img=img.resize((500,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=200)


        #second img
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=200)


        #third img
        img2=Image.open(r"college_images\clg2.jpg")
        img2=img2.resize((550,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=200)


        #bg img
        img3=Image.open(r"college_images\skylab.png")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)


        #title lable
        title_lbl=Label(bg_img,text="HELP CENTER",font=("times new roman",35,"bold"),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530, height= 45)


        #Content lable
        title_lbl=Label(bg_img,text="For Any Queries Please Contact\n\n\n Phone No : 8965416693 \n\n Email Id : face@recg.com",font=("times new roman",25,"bold"),bg='white',fg='red')
        title_lbl.place(x=500,y=150,width=500, height= 345)














if __name__ == "__main__":
    root=Tk()
    obj=Help_center(root)
    root.mainloop()
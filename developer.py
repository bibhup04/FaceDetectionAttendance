from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student



class Developer_details:
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
        title_lbl=Label(bg_img,text="DEVELOPERS DETAILS",font=("times new roman",35,"bold"),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530, height= 45)


        #Content lable
        title_lbl1=Label(bg_img,text="Name: Bibhu Sunder Pattanaik\n\n Regn No : 1901209352 \n\n Phone No : 8917498418",font=("times new roman",25,"bold"),bg='white',fg='red')
        title_lbl1.place(x=130,y=90,width=470, height= 200)

        #Content lable
        title_lbl2=Label(bg_img,text="Name: Debashis Debadutta Giri\n\n Regn No : 1901209481 \n\n Phone No : 9348811347",font=("times new roman",25,"bold"),bg='white',fg='red')
        title_lbl2.place(x=930,y=90,width=470, height= 200)

        #Content lable
        title_lbl3=Label(bg_img,text="Name: Rohan Kumar Meher\n\n Regn No : 1901209483 \n\n Phone No : 7735396253",font=("times new roman",25,"bold"),bg='white',fg='red')
        title_lbl3.place(x=130,y=340,width=470, height= 200)        

        #Content lable
        title_lbl4=Label(bg_img,text="Name: Subhashree Sahu\n\n Regn No : 190410201 \n\n Phone No : 8249707699",font=("times new roman",25,"bold"),bg='white',fg='red')
        title_lbl4.place(x=930,y=340,width=470, height= 200)   
    















if __name__ == "__main__":
    root=Tk()
    obj=Developer_details(root)
    root.mainloop()
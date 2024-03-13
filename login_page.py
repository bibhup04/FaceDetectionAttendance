from tkinter import *
from tkinter import Tk
from tkinter import ttk
from PIL import Image,ImageTk
import PIL.Image
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recgonition_System
#from tkinter.tix import COLUMN

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")


        self.var_email=StringVar()
        self.var_pass=StringVar()
        
        #self.bg=ImageTk.PhotoImage(file=r"college_images\si2.png")
        #first img
        img=Image.open(r"college_images\si2.png")
        img=img.resize((1530,790))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=PIL.Image.open(r"college_images\user.png")
        img1=img1.resize((80,80))
        
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=740,y=175,width=80,height=80)
        
        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="blue",bg="white")
        get_str.place(x=95,y=100)
        
        #label
        lbl_username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="blue",bg="white")
        lbl_username.place(x=70,y=155)     
        
        self.entry_user=ttk.Entry(frame,textvariable=self.var_email,width=24,font=("times new roman",13,"bold"))
        self.entry_user.place(x=40,y=180,width=270)
        
        
        lbl_password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="blue",bg="white")
        lbl_password.place(x=70,y=225)     
        
        self.entry_password=ttk.Entry(frame,textvariable=self.var_pass,width=24,font=("times new roman",13,"bold"),show="*")
        self.entry_password.place(x=40,y=250,width=270)
        
        #iconnn
        img2=PIL.Image.open(r"college_images\user.png")
        img2=img2.resize((25,25))
        
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        
        img12=PIL.Image.open(r"college_images\psrd.png")
        img12=img12.resize((25,25))
        
        self.photoimage12=ImageTk.PhotoImage(img12)
        lblimg12=Label(image=self.photoimage12,bg="black",borderwidth=0)
        lblimg12.place(x=650,y=393,width=25,height=25)
              
        #btnssssssss
        #login btnn     
        login_btn=Button(frame,command=self.login,text="Login",font=("arial",15,"bold"),bd=3,relief=RIDGE,bg="green",fg="white",activeforeground="green",activebackground="pink")
        login_btn.place(x=50,y=300,width=240,height=35)
        
        #register btnn
        register_btn=Button(frame,command=self.rigister_window,text="New User Register",font=("arial",10,"bold"),borderwidth=0,bg="white",fg="red",activeforeground="green",activebackground="pink")
        register_btn.place(x=15,y=380,width=160)
        
        #password btnn
        #password_btn=Button(frame,text="Forget Password",font=("arial",10,"bold"),borderwidth=0,bg="white",fg="red",activeforeground="green",activebackground="pink")
        #password_btn.place(x=10,y=405,width=160)


    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.entry_user.get()=="" or self.entry_password.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                            self.var_email.get(),
                                                                                            self.var_pass.get()
                                                                                            ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and password")
                else:
                    self.main_page()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    def main_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recgonition_System(self.new_window)









    


  
        
        
if __name__ == "__main__":
    main() 
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from PIL import Image,ImageTk
import PIL.Image
from tkinter import messagebox
import mysql.connector
import os
#from tkinter.tix import COLUMN


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration page")
        self.root.geometry("1530x790+0+0")


        #==========variables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_myemail=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        #bg image
        img=Image.open(r"college_images\skylab.png")
        img=img.resize((1530,790))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)


        #left image
        img1=Image.open(r"college_images\fd.png")
        img1=img1.resize((470,550))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=50,y=100,width=470,height=550)


        #main frame
        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=750,height=550)

        register_lbl=Label(frame,text="REGISTER HERE", font=('times new roman',28,'bold'),fg='darkgreen',bg='white')
        register_lbl.place(x=20,y=20)

        #levels and entry fills
        #first_row
        first_name_label= Label(frame,text="First Name:",font=('times new roman',12,'bold'),bg='white')
        first_name_label.place(x=50,y=100)

        self.first_name_entry=ttk.Entry(frame,textvariable=self.var_fname,width=20,font=('times new roman',12,'bold'))
        self.first_name_entry.place(x=50,y=125)

        last_name_label= Label(frame,text="Last Name:",font=('times new roman',12,'bold'),bg='white')
        last_name_label.place(x=350,y=100)

        self.last_name_entry=ttk.Entry(frame,textvariable=self.var_lname,width=20,font=('times new roman',12,'bold'))
        self.last_name_entry.place(x=350,y=125)


        #second_row
        contact_no_label= Label(frame,text="Contact No:",font=('times new roman',12,'bold'),bg='white')
        contact_no_label.place(x=50,y=200)

        self.contact_no_entry=ttk.Entry(frame,textvariable=self.var_contact,width=20,font=('times new roman',12,'bold'))
        self.contact_no_entry.place(x=50,y=225)

        Email_label= Label(frame,text="Email Id:",font=('times new roman',12,'bold'),bg='white')
        Email_label.place(x=350,y=200)

        self.Email_entry=ttk.Entry(frame,textvariable=self.var_myemail,width=20,font=('times new roman',12,'bold'))
        self.Email_entry.place(x=350,y=225)


        #third_row
        security_question_label= Label(frame,text="Select Security Question:",font=('times new roman',12,'bold'),bg='white')
        security_question_label.place(x=50,y=300)

        self.security_question_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new ronam",12,'bold'),state='readonly')
        self.security_question_combo['values']=('Select','Your pet name',"Your Birth Place",'First School Name')
        self.security_question_combo.current(0)
        self.security_question_combo.place(x=50,y=325)

        security_answer_label= Label(frame,text="Security Answer:",font=('times new roman',12,'bold'),bg='white')
        security_answer_label.place(x=350,y=300)

        self.security_answer_entry=ttk.Entry(frame,textvariable=self.var_securityA,width=20,font=('times new roman',12,'bold'))
        self.security_answer_entry.place(x=350,y=325)


        #third_row
        new_password_label= Label(frame,text="New Password:",font=('times new roman',12,'bold'),bg='white')
        new_password_label.place(x=50,y=400)

        self.new_password_entry=ttk.Entry(frame,textvariable=self.var_pass,width=20,font=('times new roman',12,'bold'))
        self.new_password_entry.place(x=50,y=425)

        confirm_password_label= Label(frame,text="Confirm Password:",font=('times new roman',12,'bold'),bg='white')
        confirm_password_label.place(x=350,y=400)

        self.confirm_password_entry=ttk.Entry(frame,textvariable=self.var_confpass,width=20,font=('times new roman',12,'bold'))
        self.confirm_password_entry.place(x=350,y=425)




        #=============check button=============
        checkbtn=Checkbutton(frame,variable=self.var_check,text='I Agree all the Terms and Conditons',font=('times new roman',12,'bold'),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=475)


        #==========register icon====================
        img11=Image.open(r"college_images\register.jpg")
        img11=img11.resize((80,80))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(frame, image=self.photoimg11,cursor='hand2',command=self.register_data)
        b1.place(x=420,y=465,width=80,height=80)


        #==========login icon====================
        img12=Image.open(r"college_images\login.jpg")
        img12=img12.resize((80,80))
        self.photoimg12=ImageTk.PhotoImage(img12)

        b2=Button(frame, image=self.photoimg12,cursor='hand2')
        b2.place(x=550,y=465,width=80,height=80)



        #================functions=====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_myemail.get()=="" or self.var_pass.get()=='':
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_confpass.get()!=self.var_pass.get():
            messagebox.showerror("Error","Confirm password is not same as password",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree temrs and conditions",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                my_cursor=conn.cursor()
                #query=("select * from new_register where fname=%s")
                #value=(self.var_fname.get())
                #my_cursor.execute(query,value)
                if 5!=5:
                    messagebox.showerror("Error","User already exist,please try with another email")
                else:
                    my_cursor.execute("insert into new_register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_fname.get(),
                                                                                                                self.var_lname.get(),
                                                                                                                self.var_contact.get(),
                                                                                                                self.var_myemail.get(),
                                                                                                                self.var_securityQ.get(),
                                                                                                                self.var_securityA.get(),
                                                                                                                self.var_pass.get(),
                                                                                                                
                                                                                                            ))
                conn.commit()
                #self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Registetr successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    





if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()        
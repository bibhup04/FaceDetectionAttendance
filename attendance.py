from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime

mydata=[]
fln=str

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #===============variables================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()




        #first img
        img=Image.open(r"college_images\si2.png")
        img=img.resize((780,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=780,height=200)


        #second img
        img1=Image.open(r"college_images\skylab.png")
        img1=img1.resize((780,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=780,y=0,width=780 ,height=200)

        #bg img
        img3=Image.open(r"college_images\bg2.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)


        #title lable
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg='white',fg='darkgreen')
        title_lbl.place(x=0,y=0,width=1530, height= 45)

        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'))
        Left_frame.place(x=10,y=10,width=720,height=500)


        #left label frame img
        img_left=Image.open(r"college_images\students.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=707,height=130)

        #left inside frame

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=5,y=135,width=708,height=330)

        #label and entries

        #attendance id
        attendanceId_label= Label(left_inside_frame,text="Attendance ID:",font=('times new roman',12,'bold'),bg='white')
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=('times new roman',12,'bold'))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label= Label(left_inside_frame,text="Roll No:",font=('times new roman',12,'bold'),bg='white')
        roll_label.grid(row=0,column=2,padx=10,pady=5)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=('times new roman',12,'bold'))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name
        name_label= Label(left_inside_frame,text="Name:",font=('times new roman',12,'bold'),bg='white')
        name_label.grid(row=1,column=0,padx=10,pady=5)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=('times new roman',12,'bold'))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label= Label(left_inside_frame,text="Department:",font=('times new roman',12,'bold'),bg='white')
        dep_label.grid(row=1,column=2,padx=10,pady=5)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=('times new roman',12,'bold'))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label= Label(left_inside_frame,text="Time:",font=('times new roman',12,'bold'),bg='white')
        time_label.grid(row=2,column=0,padx=10,pady=5)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=('times new roman',12,'bold'))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label= Label(left_inside_frame,text="Date:",font=('times new roman',12,'bold'),bg='white')
        date_label.grid(row=2,column=2,padx=10,pady=5)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=('times new roman',12,'bold'))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance
        attendance_label= Label(left_inside_frame,text="Attendance:",font=('times new roman',12,'bold'),bg='white')
        attendance_label.grid(row=3,column=0,padx=10,pady=5)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=('times new roman',12,'bold'),state='readonly')
        self.atten_status['values']=('Status','Present','Absent')
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)


        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=250,width=700,height=65)


        #import csv button
        import_csv=Button(btn_frame,text='Import csv',command=self.importCsv,width=18,font=('times new roman',12,'bold'),bg='blue',fg='white')
        import_csv.grid(row=0,column=0)

        #Export csv button
        export_csv_btn=Button(btn_frame,text='Export csv',command=self.exportCsv,width=19,font=('times new roman',12,'bold'),bg='blue',fg='white')
        export_csv_btn.grid(row=0,column=1)

        #Update button
        update_btn=Button(btn_frame,text='Update',width=18,command=self.updateCsv,font=('times new roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text='Reset',width=19,command=self.reset_data,font=('times new roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)

        #=========button frame1=============
        btn_frame1=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=280,width=700,height=32)

        #take_photo button
        take_photo_btn=Button(btn_frame1,command=self.clear_data,text='Delete all data',width=78,font=('times new roman',12,'bold'),bg='red',fg='white')
        take_photo_btn.grid(row=0)





        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Class Attendance info',font=('times new roman',12,'bold'))
        Right_frame.place(x=750,y=10,width=690,height=500)

        #table frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=678,height=470)


        #=================scroll bar and table=====================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text='StudentId')
        self.AttendanceReportTable.heading('roll',text='Roll No')
        self.AttendanceReportTable.heading('name',text='Name')
        self.AttendanceReportTable.heading('department',text='Department')
        self.AttendanceReportTable.heading('time',text='Time')
        self.AttendanceReportTable.heading('date',text='Date')
        self.AttendanceReportTable.heading('attendance',text='Attendance')


        self.AttendanceReportTable['show']='headings'

        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('roll',width=100)
        self.AttendanceReportTable.column('name',width=100)
        self.AttendanceReportTable.column('department',width=100)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column('attendance',width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #self.fetch_data()


    #=============fetch data==================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # import csv function
    def importCsv(self):
        global mydata
        mydata.clear()
        global fln
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        #print(type(fln))
        p=[]
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                #print(i,'and',mydata)
                #print('---')
                #p.append([i[0],i[1],i[2]])
                #print(p)
            self.fetchData(mydata)

   
    # update csv function
    def updateCsv(self):
        global mydata
        global fln
        mydata.clear()
        now=datetime.now()
        dt=now.strftime("%d/%m/%Y")
        tim=now.strftime("%H:%M:%S")
        hou=now.strftime("%M")
       # fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        if 1==1:
            with open('attn.csv') as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    if (i[0]==self.var_atten_id):
                        mydata.append([i[0],i[1],i[2],i[3],dt,tim,self.var_atten_attendance,hou])
                    else:
                        mydata.append(i)
                self.fetchData(mydata)


    #export csv function
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data is exported to"+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #========get cursor==========
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #=========reset button================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    #==================delete all data==============
    def clear_data(self):
        try:
            f = open("attn.csv", "w")
            f.truncate()
            f.close()
            global mydata
            mydata.clear()
            self.fetchData(mydata)
            messagebox.showinfo("Data Deleted Successfully","You can take attendance again")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        
        


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
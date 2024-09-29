import pymysql
from tkinter import *
from tkinter import messagebox, simpledialog
from PollyReports import *
from reportlab.pdfgen.canvas import Canvas
import webbrowser
import os

def login_window():
    login_win = Tk()
    login_win.geometry('900x400')
    login_win.title('Login')

    def verify_login():
        username = username_entry.get()
        password = password_entry.get()

        if username=='admin' and password=='1234':
            login_win.destroy()
            crs_window()
        else:
            messagebox.showerror('ERROR','Invalid Credentials')

    Label(login_win, text="Username:", font=('Times New Romman', 12)).pack(pady=10)
    username_entry = Entry(login_win, width=30)
    username_entry.pack(pady=5)

    Label(login_win, text='Password:', font=('Times New Roman', 12)).pack(pady=10)
    password_entry = Entry(login_win, width=30, show='*')
    password_entry.pack(pady=5)

    Button(login_win, text='Login', command=verify_login, width=15).pack(pady=20)
    login_win.mainloop()

def crs_window():
    w1 = Tk()
    w1.geometry('900x400')
    w1.title('CRS')
    def newstudentwin():
        new_window = Toplevel(w1)
        new_window.title('Student Info')
        new_window.geometry('400x400')
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        sqlq = 'SELECT * from Student'
        curs.execute(sqlq)
        x = curs.fetchall()
        listboxx = Listbox(new_window, height=20, width=50)
        listboxx.pack(pady=20)
        for r in x:
            listboxx.insert(END, r)
        conn.close()

    def generate_stdreport():
        root = Tk()
        root.withdraw()
        file_name = simpledialog.askstring("Input", 'Enter file name (without .pdf):')
        if file_name:
            file_name += ".pdf"

        if os.path.exists(file_name):
            response= messagebox.askyesno("File Exists", f"The file '{file_name}' already exists. Do you want to replace it?")
            if not response:
                file_name = simpledialog.askstring("Input", "Enter a new file name (without .pdf):") + ".pdf"

        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        csor = conn.cursor()
        sq1 = "select * from student"
        csor.execute(sq1)
        x=csor.fetchall()
        rpt = Report(datasource = x,
                    detailband = Band([
                        Element((36, 0), ("Helvetica", 9),
                                key = 0),
                        Element((100, 0), ("Helvetica", 9),
                                key = 1),
                        Element((200, 0), ("Helvetica", 9),
                                key = 2),        
                        Element((250, 0), ("Helvetica", 9),
                                key = 3),
                        Element((300, 0), ("Helvetica", 9),
                                key = 4),
                        Element((330, 0), ("Helvetica", 5),
                                key = 5),
                        Element((380, 0), ("Helvetica", 9),
                                key = 6),
                        Element((430, 0), ("Helvetica", 9),
                                key = 7),        
                        Element((480, 0), ("Helvetica", 9),
                                key = 8),
                        Element((510, 0), ("Helvetica", 9),
                                key = 9),            
                    ]))
        # Header and Footer
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 20),
                text = "Students' Data"),
            Element((36, 26), ("Helvetica", 9),
                text = "RollNo"),
            Element((100, 26), ("Helvetica", 9),
                text = "StdName"),
            Element((200, 26), ("Helvetica", 9),
                text = "FName"),
            Element((250, 26), ("Helvetica", 9),
                text = "Gender"),    
            Element((300, 26), ("Helvetica", 9),
                text = "BG"),
            Element((330, 26), ("Helvetica", 9),
                text = "CellNo"),
            Element((380, 26), ("Helvetica", 9),
                text = "Income"),
            Element((430, 26), ("Helvetica", 9),
                text = "City"),
            Element((480, 26), ("Helvetica", 9),
                text = "DCode"),    
            Element((510, 26), ("Helvetica", 9),
                text = "Specialization"),
            Rule((36, 42), 7.5*72, thickness = 2),# line
            ])
        rpt.pagefooter = Band([
            Element((72*6, 15), ("Times-Bold", 10),
                text = "Designed by Hafsa", align = "right"),
            Element((30, 16), ("Helvetica-Bold", 10),
                sysvar = "pagenumber",
                format = lambda x: "Page %d" % x),
        ])
        canvas = Canvas(file_name)
        rpt.generate(canvas)
        canvas.save()
        webbrowser.open(file_name)
        conn.close()
        root.destroy()    

    def newcourseswin():
        new_window = Toplevel(w1)
        new_window.title('Course Info')
        new_window.geometry('400x400')
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        sqlq = 'SELECT * from Courses'
        curs.execute(sqlq)
        x = curs.fetchall()
        listboxx = Listbox(new_window, height=20, width=50)
        listboxx.pack(pady=20)
        for r in x:
            listboxx.insert(END, r)
        conn.close()

    def generate_coursereport():
        root = Tk()
        root.withdraw()
        file_name = simpledialog.askstring("Input", 'Enter file name (without .pdf):')
        if file_name:
            file_name += ".pdf"

        if os.path.exists(file_name):
            response= messagebox.askyesno("File Exists", f"The file '{file_name}' already exists. Do you want to replace it?")
            if not response:
                file_name = simpledialog.askstring("Input", "Enter a new file name (without .pdf):") + ".pdf"

        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        csor = conn.cursor()
        sq1 = "select * from courses"
        csor.execute(sq1)
        x=csor.fetchall()
        rpt = Report(datasource = x,
                    detailband = Band([
                        Element((36, 0), ("Helvetica", 9),
                                key = 0),
                        Element((90, 0), ("Helvetica", 7),
                                key = 1),
                        Element((300, 0), ("Helvetica", 9),
                                key = 2),        
                        Element((370, 0), ("Helvetica", 5),
                                key = 3),
                        Element((430, 0), ("Helvetica", 9),
                                key = 4),
                        Element((480, 0), ("Helvetica", 9),
                                key = 5),
                        Element((510, 0), ("Helvetica", 9),
                                key = 6),           
                    ]))
        # Header and Footer
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 20),
                text = "Courses' Data"),
            Element((36, 26), ("Helvetica", 9),
                text = "CCode"),
            Element((90, 26), ("Helvetica", 9),
                text = "CTitle"),
            Element((300, 26), ("Helvetica", 9),
                text = "CCH"),
            Element((370, 26), ("Helvetica", 9),
                text = "PreReq"),    
            Element((430, 26), ("Helvetica", 9),
                text = "DCode"),
            Element((480, 26), ("Helvetica", 9),
                text = "CStd"),
            Element((510, 26), ("Helvetica", 9),
                text = "Semester"),
            Rule((36, 42), 7.5*72, thickness = 2),# line
            ])
        rpt.pagefooter = Band([
            Element((72*6, 15), ("Times-Bold", 10),
                text = "Designed by Hafsa", align = "right"),
            Element((30, 16), ("Helvetica-Bold", 10),
                sysvar = "pagenumber",
                format = lambda x: "Page %d" % x),
        ])
        canvas = Canvas(file_name)
        rpt.generate(canvas)
        canvas.save()
        webbrowser.open(file_name)
        conn.close()
        root.destroy() 

    def newtermwin():
        new_window = Toplevel(w1)
        new_window.title('Term Info')
        new_window.geometry('400x400')
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        sqlq = 'SELECT * from term'
        curs.execute(sqlq)
        x = curs.fetchall()
        listboxx = Listbox(new_window, height=20, width=50)
        listboxx.pack(pady=20)
        for r in x:
            listboxx.insert(END, r)
        conn.close()

    def generate_termreport():
        root = Tk()
        root.withdraw()
        file_name = simpledialog.askstring("Input", 'Enter file name (without .pdf):')
        if file_name:
            file_name += ".pdf"

        if os.path.exists(file_name):
            response= messagebox.askyesno("File Exists", f"The file '{file_name}' already exists. Do you want to replace it?")
            if not response:
                file_name = simpledialog.askstring("Input", "Enter a new file name (without .pdf):") + ".pdf"

        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        csor = conn.cursor()
        sq1 = "select * from term"
        csor.execute(sq1)
        x=csor.fetchall()
        rpt = Report(datasource = x,
                    detailband = Band([
                        Element((36, 0), ("Helvetica", 9),
                                key = 0),
                        Element((86, 0), ("Helvetica", 9),
                                key = 1),
                        Element((150, 0), ("Helvetica", 9),
                                key = 2),        
                        Element((200, 0), ("Helvetica", 9),
                                key = 3),
                        Element((300, 0), ("Helvetica", 9),
                                key = 4),           
                    ]))
        # Header and Footer
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 20),
                text = "Term Data"),
            Element((36, 26), ("Helvetica", 9),
                text = "TCode"),
            Element((86, 26), ("Helvetica", 9),
                text = "TTitle"),
            Element((150, 26), ("Helvetica", 9),
                text = "TStd"),
            Element((200, 26), ("Helvetica", 9),
                text = "StartDate"),    
            Element((300, 26), ("Helvetica", 9),
                text = "EndDate"),
            Rule((36, 42), 7.5*72, thickness = 2),# line
            ])
        rpt.pagefooter = Band([
            Element((72*6, 15), ("Times-Bold", 10),
                text = "Designed by Hafsa", align = "right"),
            Element((30, 16), ("Helvetica-Bold", 10),
                sysvar = "pagenumber",
                format = lambda x: "Page %d" % x),
        ])
        canvas = Canvas(file_name)
        rpt.generate(canvas)
        canvas.save()
        webbrowser.open(file_name)
        conn.close()
        root.destroy()

    def newdegreewin():
        new_window = Toplevel(w1)
        new_window.title('Degree Info')
        new_window.geometry('400x400')
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        sqlq = 'SELECT * from Degree'
        curs.execute(sqlq)
        x = curs.fetchall()
        listboxx = Listbox(new_window, height=20, width=50)
        listboxx.pack(pady=20)
        for r in x:
            listboxx.insert(END, r)
        conn.close()

    def generate_degreereport():
        root = Tk()
        root.withdraw()
        file_name = simpledialog.askstring("Input", 'Enter file name (without .pdf):')
        if file_name:
            file_name += ".pdf"

        if os.path.exists(file_name):
            response= messagebox.askyesno("File Exists", f"The file '{file_name}' already exists. Do you want to replace it?")
            if not response:
                file_name = simpledialog.askstring("Input", "Enter a new file name (without .pdf):") + ".pdf"

        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        csor = conn.cursor()
        sq1 = "select * from degree"
        csor.execute(sq1)
        x=csor.fetchall()
        rpt = Report(datasource = x,
                    detailband = Band([
                        Element((36, 0), ("Helvetica", 9),
                                key = 0),
                        Element((86, 0), ("Helvetica", 9),
                                key = 1),
                        Element((310, 0), ("Helvetica", 9),
                                key = 2),        
                        Element((360, 0), ("Helvetica", 9),
                                key = 3),
                        Element((410, 0), ("Helvetica", 9),
                                key = 4),      
                        Element((460, 0), ("Helvetica", 9),
                                key = 5),             
                    ]))
        # Header and Footer
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 20),
                text = "Degree Data"),
            Element((36, 26), ("Helvetica", 9),
                text = "DCode"),
            Element((86, 26), ("Helvetica", 9),
                text = "DTitle"),
            Element((310, 26), ("Helvetica", 9),
                text = "DCH"),
            Element((360, 26), ("Helvetica", 9),
                text = "NoSem"),    
            Element((410, 26), ("Helvetica", 9),
                text = "ReqCGPA"),
            Element((460, 26), ("Helvetica", 9),
                text = "NoSubjects"),
            Rule((36, 42), 7.5*72, thickness = 2),# line
            ])
        rpt.pagefooter = Band([
            Element((72*6, 15), ("Times-Bold", 10),
                text = "Designed by Hafsa", align = "right"),
            Element((30, 16), ("Helvetica-Bold", 10),
                sysvar = "pagenumber",
                format = lambda x: "Page %d" % x),
        ])
        canvas = Canvas(file_name)
        rpt.generate(canvas)
        canvas.save()
        webbrowser.open(file_name)
        conn.close()
        root.destroy()

    # creating main menu
    mm = Menu(w1)
    w1.config(menu=mm)

    studentd = Menu(mm)
    mm.add_cascade(label='Student', menu=studentd)
    studentd.add_command(label='Student Info', command=newstudentwin)
    studentd.add_command(label='Generate Students Info', command=generate_stdreport)
    studentd.add_command(label='Exit', command=w1.quit)

    coursed = Menu(mm)
    mm.add_cascade(label='Course', menu=coursed)
    coursed.add_command(label='Courses Info', command=newcourseswin)
    coursed.add_command(label='Generate Courses Info', command=generate_coursereport)
    coursed.add_command(label='Exit', command=w1.quit)

    termd = Menu(mm)
    mm.add_cascade(label='Term', menu=termd)
    termd.add_command(label='Term Info', command=newtermwin)
    termd.add_command(label='Generate Term Info', command=generate_termreport)
    termd.add_command(label='Exit', command=w1.quit)

    degreed = Menu(mm)
    mm.add_cascade(label='Degree', menu=degreed)
    degreed.add_command(label='Degree Info', command=newdegreewin)
    degreed.add_command(label='Generate Degree Info', command=generate_degreereport)
    degreed.add_command(label='Exit', command=w1.quit)

    Label(w1, text='Grading System', bg='Grey', fg='White', font=('Times New Roman', 25), width=40).place(x=400,y=0)

    Label(w1,text='Roll no.:', bg='gray',fg='black',font=('Times New Roman Bold',10),width=15).place(x=300,y=150)
    rollno = StringVar()
    ent1 = Entry(w1,textvariable=rollno, width=40)
    ent1.place(x=430, y=150)

    Label(w1, text='Course Code:', bg='gray', fg='black', font=('Times New Roman Bold', 10), width=15).place(x=300,y=180)
    ccode = StringVar()
    ent2 = Entry(w1, textvariable=ccode, width=40)
    ent2.place(x=430, y=180)

    Label(w1, text='Term Code:', bg='Grey', fg='Black', font=('Times New Roman Bold', 10), width=15).place(x=300,y=210)
    tcode = StringVar()
    ent3 = Entry(w1, textvariable=tcode, width=40)
    ent3.place(x=430,y=210)

    Label(w1, text='Obtained Marks:', bg='Grey', fg='Black', font=('Times New Roman Bold', 10), width=15).place(x=300,y=240)
    om = StringVar()
    ent4 = Entry(w1, textvariable=om, width=40)
    ent4.place(x=430, y=240)

    Label(w1, text='Grade:', bg='Grey', fg='Black', font=('Times New Roman Bold', 10), width=15).place(x=300,y=270)
    grade = StringVar()
    ent5 = Entry(w1, textvariable=grade, width=40)
    ent5.place(x=430, y=270)

    list1 = Listbox(w1, height= 35, width= 55)
    list1.place(x=850, y=130)

    def connandshow():
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        sqlq = "select * from crs"
        curs.execute(sqlq)
        x = curs.fetchall()
        list1.delete(0, END)
        for r in x:
            list1.insert(END, r)

    def insertdata():
        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        curs = conn.cursor()
        RollNo = rollno.get()
        CCode = ccode.get()
        TCode = tcode.get()
        OM = om.get()
        Grade = grade.get()

        # student check query
        student_check = "SELECT * from student WHERE RollNo = %s"
        course_check = "SELECT * from courses WHERE CCode = %s"
        term_check = "SELECT * from term WHERE TCode = %s"

        curs.execute(student_check, (RollNo))
        student_exist = curs.fetchone()

        curs.execute(course_check,(CCode))
        course_exist = curs.fetchone()

        curs.execute(term_check,(TCode))
        term_exist = curs.fetchone()

        if student_exist and course_exist and term_exist:
            sqlq = "INSERT INTO crs (RegNo, CCode, TCode, OM, Grade) VALUES (%s, %s, %s, %s, %s)"
            curs.execute(sqlq, (RollNo, CCode, TCode, OM, Grade))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", 'Record inserted successfully!')

        else:
            if not student_exist:
                messagebox.showerror("Error", f"Student with roll number {RollNo} does not exist!")
            elif not course_exist:
                messagebox.showerror("Error", f"Course with course code {CCode} does not exist")
            elif not term_exist:
                messagebox.showerror("Error", f"Term with term code {TCode} does not exist")

    def deleteData():
        conn = pymysql.connect(host='localhost', user='root', password = '', db = 'crs')
        curs = conn.cursor()
        RollNo = rollno.get()
        CCode = ccode.get()
        TCode = tcode.get()
        OM = om.get()
        Grade = grade.get()

        # student check query
        student_check = "SELECT * from student WHERE RollNo = %s"
        course_check = "SELECT * from courses WHERE CCode = %s"
        term_check = "SELECT * from term WHERE TCode = %s"
        om_check = "SELECT * from crs WHERE OM = %s"
        grade_check = "SELECT * from crs WHERE Grade = %s"

        curs.execute(student_check, (RollNo))
        student_exist = curs.fetchone()

        curs.execute(course_check,(CCode))
        course_exist = curs.fetchone()

        curs.execute(term_check,(TCode))
        term_exist = curs.fetchone()

        curs.execute(om_check,(OM))
        om_exist = curs.fetchone()

        curs.execute(grade_check,(Grade))
        grade_exist = curs.fetchone()

        if student_exist and course_exist and term_exist and om_exist and grade_exist:
            sqlq = "DELETE FROM crs WHERE RegNo = %s and CCode = %s and TCode = %s and OM = %s and Grade = %s"
            curs.execute(sqlq, (RollNo, CCode, TCode, OM, Grade))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", 'Record deleted successfully!')

        else:
            messagebox.showerror("Error", f"No such data exist!")

    def updateData():
        conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'crs')
        curs = conn.cursor()
        RollNo = rollno.get()
        CCode = ccode.get()
        TCode = tcode.get()
        Grade = grade.get()
        OM = om.get()

        # student check query
        student_check = "SELECT * from student WHERE RollNo = %s"
        course_check = "SELECT * from courses WHERE CCode = %s"
        term_check = "SELECT * from term WHERE TCode = %s"

        curs.execute(student_check, (RollNo,))
        student_exist = curs.fetchone()

        curs.execute(course_check,(CCode,))
        course_exist = curs.fetchone()

        curs.execute(term_check,(TCode,))
        term_exist = curs.fetchone()

        if student_exist and course_exist and term_exist:
            sqlq = "UPDATE crs SET OM = %s, Grade = %s WHERE RegNo = %s and CCode = %s and TCode = %s"
            curs.execute(sqlq, (OM, Grade, RollNo, CCode, TCode))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", 'Record updated successfully!')

        else:
            messagebox.showerror("Error", f"No record found!") 
            conn.close()


    def searchData():
        conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'crs')
        curs = conn.cursor()
        sqlq = 'SELECT * from crs where RegNo = %s and CCode = %s and TCode = %s and OM = %s and Grade = %s'
        curs.execute(sqlq, (rollno.get(), ccode.get(), tcode.get(), om.get(), grade.get()))
        a = curs.fetchall()
        list1.delete(0,END)
        if a:
            for r in a:
                list1.insert(END, r)
        else:
            messagebox.showerror("Error", f'No record found!')

    def selectdata(evt):
        if list1.curselection():  # Check if any item is selected
            index = list1.curselection()[0]
            global sr 
            sr = list1.get(index)
            ent1.delete(0,END)
            ent1.insert(END, sr[0])
            ent2.delete(0,END)
            ent2.insert(END, sr[1])
            ent3.delete(0,END)
            ent3.insert(END, sr[2])
            ent4.delete(0,END)
            ent4.insert(END, sr[3])
            ent5.delete(0,END)
            ent5.insert(END, sr[4])

    def generate_report():
        root = Tk()
        root.withdraw()
        file_name = simpledialog.askstring("Input", 'Enter file name (without .pdf):')
        if file_name:
            file_name += ".pdf"

        if os.path.exists(file_name):
            response= messagebox.askyesno("File Exists", f"The file '{file_name}' already exists. Do you want to replace it?")
            if not response:
                file_name = simpledialog.askstring("Input", "Enter a new file name (without .pdf):") + ".pdf"

        conn = pymysql.connect(host='localhost', user='root', password='', db='crs')
        csor = conn.cursor()
        sq1 = "select * from crs"
        csor.execute(sq1)
        x=csor.fetchall()
        rpt = Report(datasource = x,
                    detailband = Band([
                        Element((36, 0), ("Helvetica", 12),
                                key = 0),
                        Element((150, 0), ("Helvetica", 12),
                                key = 1),
                        Element((250, 0), ("Helvetica", 12),
                                key = 2),        
                        Element((350, 0), ("Helvetica", 12),
                                key = 3),
                        Element((450, 0), ("Helvetica", 12),
                                key = 4),
                    ]))
        # Header and Footer
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 20),
                text = "Student's Grade Data"),
            Element((36, 26), ("Helvetica", 12),
                text = "RegNo"),
            Element((150, 26), ("Helvetica", 12),
                text = "CCode"),
            Element((250, 26), ("Helvetica", 12),
                text = "TCode"),
            Element((350, 26), ("Helvetica", 12),
                text = "OM"),    
            Element((450, 26), ("Helvetica", 12),
                text = "Grade"),
            Rule((36, 42), 7.5*72, thickness = 2),# line
            ])
        rpt.pagefooter = Band([
            Element((72*6, 15), ("Times-Bold", 10),
                text = "Designed by Hafsa", align = "right"),
            Element((30, 16), ("Helvetica-Bold", 10),
                sysvar = "pagenumber",
                format = lambda x: "Page %d" % x),
        ])
        canvas = Canvas(file_name)
        rpt.generate(canvas)
        canvas.save()
        webbrowser.open(file_name)
        root.destroy()

    list1.bind('<<ListboxSelect>>', selectdata)

    bt1 = Button(w1, text='Get Text', width=15, command=connandshow) 
    bt1.place(x=300,y=400)

    bt2 = Button(w1, text='Add Record', width=15, command= insertdata)
    bt2.place(x=300, y=430)

    bt3 = Button(w1, text='Delete Record', width=15, command=deleteData)
    bt3.place(x=420, y=400)

    bt4 = Button(w1,text='Update data', width=15, command=updateData)
    bt4.place(x=420, y=430)

    bt5 = Button(w1, text='Search Data', width=15, command=searchData)
    bt5.place(x=540, y=400)

    bt6 = Button(w1, text='Exit', width=15, command=w1.destroy)
    bt6.place(x=540, y=430)

    bt7 = Button(w1, text='Generate Report', width=15, command=generate_report)
    bt7.place(x=660, y=400)

    w1.mainloop()

login_window()
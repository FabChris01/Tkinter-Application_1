from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import ttk
import sqlite3


def add_to_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute("insert into book (name, author) values (?,?)",
                  (e_bname.get(), e_bauth.get()))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def get_from_db():

    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute('select * from book')
        data = c.fetchall()
        # for i in data:
        #     print(i)
        return data
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def del_from_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute('delete from book')
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def reset():
    MessageBox.showwarning("Warning", "Data Will be RESET!")
    del_from_db()


def payment():
    pass


def detail_view():
    top = Toplevel()
    top.title('Detail View')
    top.geometry('800x400')
    data = get_from_db()

    tv = ttk.Treeview(top)
    tv['columns'] = ('NAME', 'AUTHOR')

    tv.column("#0", width=0)
    tv.column("NAME", anchor=W, width=400)
    tv.column("AUTHOR", anchor=W, width=400)

    tv.heading("#0")
    tv.heading("NAME", text="NAME", anchor=W)
    tv.heading("AUTHOR", text='AUTHOR', anchor=CENTER)

    for i, row in enumerate(data):
        tv.insert(parent='', index='end', iid=i, values=(row[1], row[2]))

    tv.pack()

    paymentBtn = Button(top, text="PAYMENT", font=(
        "bold", 10), bg="white", command=payment)
    paymentBtn.place(x=200, y=300)
    exitBtn = Button(top, text="RESET", font=(
        "bold", 10), bg="white", command=top.destroy)
    exitBtn.place(x=400, y=300)


def submit():
    name = e_bname.get()
    auth = e_bauth.get()

    if(name == "" or auth == ""):
        MessageBox.showinfo("Message", "All Fields are Required")
    else:
        MessageBox.showinfo("Message", "Successfully Registered!!")
        # InputData gets sent to database
        add_to_db()
        # data = get_from_db()
        detail_view()


def continue_window():
    top = Toplevel()
    top.title('Book Bank')
    top.geometry("600x300")
    head = Label(top, text='GIVE BOOK DETAILS', font=('bold', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    b_name = Label(top, text='BOOK NAME', font=('bold', 15))
    b_name.place(relx=0.1, rely=0.4, anchor=W)
    global e_bname
    e_bname = Entry(top)
    e_bname.place(relx=0.9, rely=0.4, anchor=E)
    e_bname.config(width=30)

    b_auth = Label(top, text='BOOK AUTHOR', font=('bold', 15))
    b_auth.place(relx=0.1, rely=0.6, anchor=W)
    global e_bauth
    e_bauth = Entry(top)
    e_bauth.place(relx=0.9, rely=0.6, anchor=E)
    e_bauth.config(width=30)

    bname = Button(top, text="SUBMIT", font=(
        "bold", 10), bg="white", command=submit)
    bname.place(relx=0.2, rely=0.8, anchor=W)
    bname.config(height=1, width=10)

    bview = Button(top, text='VIEW', font=('bold', 10),
                   bg='white', command=detail_view)
    bview.place(relx=0.5, rely=0.8, anchor=CENTER)
    bname.config(height=1, width=10)

    bauth = Button(top, text="RESET", font=(
        "bold", 10), bg="white", command=reset)
    bauth.place(relx=0.8, rely=0.8, anchor=E)
    bauth.config(height=1, width=10)


def cancel():
    root.destroy()
    exit()


# ================================= MAIN =================================
root = Tk()
root.geometry("600x300")
root.title("Book Bank")

id = Label(root, text='WELCOME TO THE BOOK BANK MANAGEMENT SYSTEM',
           font=('bold', 15))
id.place(relx=0.5, rely=0.2, anchor=CENTER)

a = Button(root, text="DO YOU WANT TO CONTINUE", font=(
    "bold", 10), bg="white", command=continue_window)
a.place(relx=0.5, rely=0.4, anchor=CENTER)
a.config(height=1, width=30)


b = Button(root, text="CANCEL", font=("bold", 10), bg="white", command=cancel)
b.place(relx=0.5, rely=0.6, anchor=CENTER)
b.config(height=1, width=10)


mainloop()

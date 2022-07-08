import sqlite3
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox


class parkingDatabaseClass:
    # date = dt.datetime.now()
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Parking Management System -- Developed By Shruti")
        self.root.config(bg='#F5F5F5')
        self.root.focus_force()

        self.search_by = StringVar()
        self.search_text = StringVar()

        self.vehicle_type = StringVar()
        self.time_period = StringVar()

        self.vehicle_number = StringVar()
        self.owners_name = StringVar()

        self.value = int

        # function for display current time
        def my_time():
            date = strftime('%H:%M:%S %d %B')
            value_date.config(text=date)
            value_date.after(1000, my_time)

        self.contact_num = StringVar()  # "serial_no","type","reg_num","name","contact","checkIn","checkOut","fare"
        self.check_in = StringVar()  # dt.datetime.now() # '%H:%M'
        self.check_out = StringVar()

        # upper frame
        searchFrame = LabelFrame(self.root, text="Search Vehicle", font=("Times New Roman", 19, "bold"), bd=2,
                                 relief=RIDGE, bg="#F5F5F5")
        searchFrame.place(x=500, y=20, width=700, height=110)

        # Select option - Four Wheeler - two wheeler
        option_search = ttk.Combobox(searchFrame, textvariable=self.search_by,
                                     values=("Select", "reg_num", "name", "contact"), state="readonly", justify=CENTER,
                                     font=("times new roman", 17))
        option_search.place(x=10, y=15, width=200, height=50)
        option_search.current(0)

        # text and button in upper frame
        Entry(searchFrame, textvariable=self.search_text, font=("times new roman", 17),
              bg="#E1F5FE").place(x=220, y=15, height=50, width=270)
        Button(searchFrame, text="Search", command=self.search, font=("times new roman", 18),
               bg="green", fg="white", cursor="hand2").place(x=500, y=13, width=190, height=50)

        # display title main title
        Label(self.root, text="Vehicle Details", font=("times new roman", 22), bg="#1A237E", fg="white").place(
            x=2, y=140, width=1532, height=35)
        Label(self.root, font=("times", 18), fg="dark red", bg="#F5F5F5",
              text="                    Four Wheeler -> ₹50             Two Wheeler -> ₹25 \n                    "
                   "Four Wheeler -> ₹100            Two Wheeler -> ₹50 "
              ).place(x=480, y=180, width=800, height=70)
        Label(self.root, text="Parking Charges: (12-hours) \n                           (24-hours)",
              font=("times", 18),
              bg="#F5F5F5", fg="black").place(x=380, y=180, height=70)

        ''' First Column '''
        # -------------------------DATETIME----------------------------------------------------------------------------------------------------------------
        Label(self.root, text="Date-Time", font=("times new roman", 19), bg="#F5F5F5").place(x=80, y=100)
        # date label at upper left
        # format_date= f"{self.date:%A %B %d %Y}"
        value_date = Label(root, font=("times new roman", 18), fg="black", bg="#F5F5F5")
        value_date.place(x=200, y=100, width=180)
        my_time()
        # -------------------------DATETIME----------------------------------------------------------------------------------------------------------------

        # inside parameters i.e., type,name ,numbe,phn number,checkin time,chckout time, fare
        Label(self.root, text="Time Period", font=("times new roman", 19), bg="#F5F5F5").place(
            x=70, y=270)
        Label(self.root, text="Vehicle Type", font=("times new roman", 19), bg="#F5F5F5").place(
            x=70, y=370)
        Label(self.root, text="Vehicle Number", font=("times new roman", 19), bg="#F5F5F5").place(
            x=70, y=470)

        # text box for first column

        # text-variable=self.time_period,
        value_time_period = ttk.Combobox(self.root, textvariable=self.time_period,
                                         values=("Select", "12-hours", "24-hours"), state="readonly", justify=CENTER,
                                         font=("times new roman", 19))
        value_time_period.place(x=260, y=270, width=180)
        value_time_period.current(0)

        # vehicle type
        value_vehicle_type = ttk.Combobox(self.root, textvariable=self.vehicle_type,
                                          values=("Select", "Four Wheeler", "Two Wheeler"), state="readonly",
                                          justify=CENTER, font=("times new roman", 19))
        value_vehicle_type.place(x=260, y=370, width=180)
        value_vehicle_type.current(0)

        Entry(self.root, textvariable=self.vehicle_number, font=("times new roman", 17),
              bg="#E1F5FE").place(x=260, y=475, width=180)
        '''--------------End of First Column-------------'''

        '''Second Column'''
        # inside parameters i.e., type,name ,numbe,phn number,checkin time,chckout time, fare
        Label(self.root, text="Owner's Name", font=("times new roman", 19), bg="#F5F5F5").place(
            x=580, y=270)
        Label(self.root, text="Contact No.", font=("times new roman", 19), bg="#F5F5F5").place(
            x=580, y=370)
        Label(self.root, text="Check In", font=("times new roman", 19), bg="#F5F5F5").place(x=580,
                                                                                            y=470)

        # value_date.config(text =format_date)
        Entry(self.root, textvariable=self.owners_name, font=("times new roman", 17),
              bg="#E1F5FE").place(x=750, y=275, width=180)
        Entry(self.root, textvariable=self.contact_num, font=("times new roman", 17),
              bg="#E1F5FE").place(x=750, y=370, width=180)
        Entry(self.root, textvariable=self.check_in, font=("times new roman", 17), bg="#E1F5FE").place(
            x=750, y=470, width=180)
        '''------------------End of Second Column----------------'''

        '''Third Column Button '''
        Label(self.root, text="Check Out", font=("times new roman", 19), bg="#F5F5F5").place(x=1060,
                                                                                             y=270)
        Label(self.root, text="Total Fare", font=("times new roman", 19), bg="#F5F5F5").place(x=1060,
                                                                                              y=400)

        Entry(self.root, textvariable=self.check_out, font=("times new roman", 17),
              bg="#E1F5FE").place(x=1200, y=270, width=180)
        # display fare function being used here
        Button(self.root, text="Calculate", command=self.display_fare, font=("times new roman", 15)).place(
            x=1300, y=435, width=100, height=50)

        '''-------------------End of Third Column--------------------'''

        '''BUTTONS'''
        Button(self.root, text="Save", command=self.add, font=("times new roman", 22), bg="#4CAF50",
               fg="white",
               cursor="hand2").place(x=310, y=530, width=200, height=50)
        Button(self.root, text="Update", command=self.update, font=("times new roman", 22),
               bg="#0277BD", fg="white",
               cursor="hand2").place(x=610, y=530, width=200, height=50)
        Button(self.root, text="Delete", command=self.delete, font=("times new roman", 22),
               bg="#d50000", fg="white",
               cursor="hand2").place(x=910, y=530, width=200, height=50)
        Button(self.root, text="Clear", command=self.clear, font=("times", 22), bg="#F1C40F", fg="white",
               cursor="hand2").place(x=1210, y=530, width=200, height=50)

        '''--------------------End Of Buttons------------------------------'''

        '''bottom table'''
        table_frame = Frame(self.root, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=608, relwidth=1, height=200)

        scrollx = Scrollbar(table_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(table_frame, orient=VERTICAL)

        self.DataTable = ttk.Treeview(table_frame, columns=(
            "serial_no", "date", "time_period", "type", "reg_num", "name", "contact", "checkIn", "checkOut"),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.DataTable.xview)
        scrolly.config(command=self.DataTable.yview)
        self.DataTable.heading("serial_no", text="Serial No.")
        self.DataTable.heading("date", text="Date")
        self.DataTable.heading("time_period", text="Time Period")
        self.DataTable.heading("type", text="Vehicle Type")
        self.DataTable.heading("reg_num", text="Vehicle Number")
        self.DataTable.heading("name", text="Owner's Name")
        self.DataTable.heading("contact", text="Contact No.")
        self.DataTable.heading("checkIn", text="Check In Time")
        self.DataTable.heading("checkOut", text="Check Out Time")

        self.DataTable["show"] = "headings"

        self.DataTable.column("serial_no", width=90, anchor=CENTER)
        self.DataTable.column("date", width=100)
        self.DataTable.column("time_period", width=100)
        self.DataTable.column("type", width=100)
        self.DataTable.column("reg_num", width=100)
        self.DataTable.column("name", width=100)
        self.DataTable.column("contact", width=100)
        self.DataTable.column("checkIn", width=100)
        self.DataTable.column("checkOut", width=100)

        self.DataTable.pack(fill=BOTH, expand=1)

        self.DataTable.bind("<ButtonRelease-1>", self.show_data)
        self.show()

    # --------------------------------------------------------------------------------------------------------------------------------------

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.vehicle_number.get() == "":
                messagebox.showerror("Error", "Vehicle number must be required!", parent=self.root)
            else:
                cur.execute("Select * from parking where reg_num = ?", (self.vehicle_number.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Vehicle Number is already exist!", parent=self.root)
                else:
                    cur.execute("Insert into parking (time_period,type,reg_num,name,contact,checkIn,checkOut)"
                                "values(?,?,?,?,?,?,?) ",
                                (
                                    self.time_period.get(),
                                    self.vehicle_type.get(),
                                    self.vehicle_number.get(),
                                    self.owners_name.get(),
                                    self.contact_num.get(),
                                    self.check_in.get(),
                                    self.check_out.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Details Added Successfully!", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    # Display the data in tree view
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * From parking")
            rows = cur.fetchall()
            self.DataTable.delete(*self.DataTable.get_children())
            for row in rows:
                self.DataTable.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    # show display the data in respected entry
    def show_data(self, ev):
        f = self.DataTable.focus()
        content = (self.DataTable.item(f))
        row = content['values']
        self.time_period.set(row[2])
        self.vehicle_type.set(row[3])
        self.vehicle_number.set(row[4])
        self.owners_name.set(row[5])
        self.contact_num.set(row[6])
        self.check_in.set(row[7])
        self.check_out.set(row[8])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.vehicle_number.get() == "":
                messagebox.showerror("Error", "Vehicle number must be required!", parent=self.root)
            else:
                cur.execute("Select * from parking where reg_num = ?", (self.vehicle_number.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid vehicle number", parent=self.root)
                else:
                    cur.execute("Update  parking set time_period =?, type=?,name=?,contact=?,checkIn=?,checkOut=?"
                                " where reg_num=?",
                                (
                                    self.time_period.get(),
                                    self.vehicle_type.get(),
                                    self.owners_name.get(),
                                    self.contact_num.get(),
                                    self.check_in.get(),
                                    self.check_out.get(),
                                    self.vehicle_number.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Details Updated Successfully!", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.vehicle_number.get() == "":
                messagebox.showerror("Error", "Vehicle number must be required!", parent=self.root)
            else:

                cur.execute("Select * from parking where reg_num = ?", (self.vehicle_number.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invaild vehicle number", parent=self.root)
                else:
                    conformation = messagebox.askyesno("Confirm", "Do you really want to delete?")
                    if conformation is True:
                        cur.execute("Delete from parking where reg_num=?", (self.vehicle_number.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Vehicle details deleted successfully")
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def clear(self):
        self.time_period.set("Select")
        self.vehicle_type.set("Select")
        self.vehicle_number.set("")
        self.owners_name.set("")
        self.contact_num.set("")
        self.check_in.set("")
        self.check_out.set("")
        self.clear_fare()
        self.search_text.set("")
        self.search_by.set("Select")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.search_by.get() == "Select":
                messagebox.showerror("Error", "Choose the proper option!", parent=self.root)
            elif self.search_text.get() == "":
                messagebox.showerror("Error", "Enter the input in the field", parent=self.root)
            else:
                cur.execute(
                    "Select * From parking where " + self.search_by.get() + " Like '%" + self.search_text.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.DataTable.delete(*self.DataTable.get_children())
                    for row in rows:
                        self.DataTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def display_fare(self):
        # messagebox.showerror("Error", "Provide the  value")
        new_var = self.vehicle_type.get()
        if new_var == "Two Wheeler":
            if self.time_period.get() == "12-hours":
                self.value = "30"
            else:
                self.value = "50"
        else:
            if self.time_period.get() == "12-hours":
                self.value = "50"
            else:
                self.value = "100"
        Label(self.root, text=self.value, font=("times new roman", 20), bg="#F5F5F5").place(x=1200, y=405, width=180)

        return self.value

    def clear_fare(self):
        self.value = ""
        Label(self.root, text=self.value, font=("times new roman", 20), bg="#F5F5F5").place(x=1200, y=405, width=180)


def database():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE if not EXISTS Parking (serial_no integer primary key autoincrement,'
                'dates date DEFAULT CURRENT_DATE, '
                'time_period varchar(10), type text Not Null,reg_num varchar(14) not null unique,name varchar(20),'
                'contact varchar(11),checkIn text not null,checkOut text)')
    con.commit()

database()
if __name__ == "__main__":
    root = Tk()
    obj = parkingDatabaseClass(root)
    root.mainloop()

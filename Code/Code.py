import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
import tkinter.font as font
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="poon1112",
    port="3306",
    database="CarRental2019"
)

my_cursor = mydb.cursor()


def customer_info():
    Name = input1.get()
    Phone = input2.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        cusinfo = Tk()
        cusinfo.title('CUSTOMER')
        data = "INSERT INTO customer(Name, Phone) Values (%s, %s)"
        value = (Name, Phone)
        my_cursor.execute(data, value)
        my_cursor.execute('SELECT * FROM CUSTOMER')
        CUSTOMER = my_cursor.fetchall()

        result = ttk.Treeview(cusinfo, selectmode='browse')
        result.grid(row=1, column=1, padx=10, pady=10, ipadx=110, ipady=270)
        result["columns"] = ("1", "2", "3")
        result['show'] = 'headings'
        result.column("1", width=10)
        result.column("2", width=50)
        result.column("3", width=50)
        result.heading("1", text="CustID")
        result.heading("2", text="Name")
        result.heading("3", text="Phone")
        count = 0
        for cus in CUSTOMER:
            count += 1
            result.insert("", 'end', iid=cus[0], values=(cus[0], cus[1], cus[2]))
        print("Row(s) returned: ", count)
        messagebox.showinfo("Status", "New Customer Added!\n" + str(count) + " row(s) Returned.")
        mydb.commit()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def vehicle_info():
    VehicleID = vehicle1.get()
    Description = vehicle2.get()
    Year = vehicle3.get()
    Type = vehicle4.get()
    Category = vehicle5.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        vehinfo = Tk()
        vehinfo.title('VEHICLE')
        data = "INSERT INTO vehicle(VehicleID, Description, Year,Type,Category) Values (%s, %s, %s, %s,%s)"
        value = (VehicleID, Description, Year, Type, Category)
        my_cursor.execute(data, value)
        #my_cursor.execute('SELECT * FROM VEHICLE')
        VEHICLE = my_cursor.fetchall()
        result = ttk.Treeview(vehinfo, selectmode='browse')
        result.grid(row=1, column=1, padx=10, pady=10, ipadx=150, ipady=270)
        result["columns"] = ("1", "2", "3", "4", "5")
        result['show'] = 'headings'
        result.column("1", width=100)
        result.column("2", width=100)
        result.column("3", width=3)
        result.column("4", width=3)
        result.column("5", width=3)
        result.heading("1", text="VehicleID")
        result.heading("2", text="Description")
        result.heading("3", text="Year")
        result.heading("4", text="Type")
        result.heading("5", text="Category")
        count = 0
        for veh in VEHICLE:
            count += 1
            result.insert("", 'end', iid=veh[0], values=(veh[0], veh[1], veh[2], veh[3], veh[4]))
        print("Row(s) returned: ", count)
        messagebox.showinfo("Status", "New Vehicle Added!\n" + str(count) + " row(s) Returned.")
        mydb.commit()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def search_vehicle_info():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()


    try:
        search = Tk()
        search.title('Availability')
        search.geometry("300x180")
        data = "select distinct VehicleID From RENTAL as R1 where ((StartDate NOT BETWEEN %s AND %s ) " \
               "AND (ReturnDate NOT BETWEEN %s AND %s)  and RentalType = %s)"
        value = (search3.get(), search4.get(), search3.get(), search4.get(), search1.get())
        my_cursor.execute(data, value)
        fetch = my_cursor.fetchall()
        print(search3.get())
        print("Total row(s) of vechicle:  ", my_cursor.rowcount)
        messagebox.showinfo("Status", str(my_cursor.rowcount) + " Car(s) Available !\nFrom " + search3.get() + " - "
                            + search4.get())
        result = ttk.Treeview(search, selectmode='browse')
        result.grid(row=1, column=1, padx=10, pady=10, ipadx=40, ipady=50)
        result["columns"] = "1"
        result['show'] = 'headings'
        result.column("1")
        result.heading("1", text="VehicleID")
        for veh in fetch:
            result.insert("", 'end', iid=veh[0], values=(veh[0]))
        mydb.commit()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def add_Information():
    CustID = rental1.get()
    VehicleID = rental2.get()
    StartDate = rental3.get()
    OrderDate = rental4.get()
    RentalType = rental5.get()
    Qty = rental6.get()
    ReturnDate = rental7.get()
    TotalAmount = rental8.get()
    PaymentDate = rental9.get()
    Returned = rental10.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        data = "INSERT INTO Rental (CustID,VehicleID,StartDate,OrderDate,RentalType,Qty,ReturnDate,TotalAmount,PaymentDate, Returned) Values (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        value = (
        CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount, PaymentDate, Returned)
        my_cursor.execute(data, value)
        mydb.commit()
        messagebox.showinfo("Status", "New reservation added !")

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def Retrive_info():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        myretrive = Tk()
        myretrive.title("Retrieve")
        data = """SELECT Rental.CustID, Name, TotalAmount FROM rental,  customer WHERE Rental.CustID=Customer.CustID AND Rental.CustID=%s AND Name=%s AND ReturnDate=%s AND VehicleID= %s"""
        value = (return1.get(), return2.get(), return3.get(), return4.get())
        my_cursor.execute(data, value)
        fetch = my_cursor.fetchall()
        result = ttk.Treeview(myretrive, selectmode='browse')
        result.grid(row=1, column=1, padx=10, pady=10, ipadx=110, ipady=20)
        result["columns"] = ("1", "2", "3")
        result['show'] = 'headings'
        result.column("1", width=10)
        result.column("2", width=50)
        result.column("3", width=50)
        result.heading("1", text="CustID")
        result.heading("2", text="Name")
        result.heading("3", text="$ Balance Due")
        for rent in fetch:
            result.insert("", 'end', iid=rent[0], values=(rent[0], rent[1], rent[2]))
        mydb.commit()


    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def Update_info():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        data = """UPDATE RENTAL, CUSTOMER  SET Returned='1', TotalAmount=0  WHERE Rental.CustID=Customer.CustID AND Rental.CustID=%s AND Name=%s AND ReturnDate=%s AND VehicleID= %s"""
        value = (return1.get(), return2.get(), return3.get(), return4.get())
        my_cursor.execute(data, value)
        messagebox.showinfo("Status", "Updated !\nNo $ Balance Due")
        mydb.commit()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def new_customer():
    global input1
    global input2
    newcustomer = Tk()
    newcustomer.title("New Customer")
    newcustomer.geometry("300x130")
    newcustomer.resizable(0, 0)
    Label(newcustomer, text="Name").place(x=10, y=10)
    Label(newcustomer, text="Phone").place(x=10, y=40)
    input1 = Entry(newcustomer)
    input1.place(x=60, y=10)
    input2 = Entry(newcustomer)
    input2.place(x=60, y=40)
    add_button = Button(newcustomer, text="Add", bg='#3498DB', fg='#FDFEFE', borderless=1, command=customer_info)
    add_button.place(x=90, y=85)


def new_vehicle():
    global vehicle1
    global vehicle2
    global vehicle3
    global vehicle4
    global vehicle5
    newvehicle = Tk()
    newvehicle.title("New Vehicle")
    newvehicle.geometry("350x230")
    newvehicle.resizable(0, 0)
    Label(newvehicle, text="VehicleID").place(x=10, y=10)
    Label(newvehicle, text="Description").place(x=10, y=47)
    Label(newvehicle, text="Year").place(x=10, y=82)
    Label(newvehicle, text="Type").place(x=10, y=120)
    Label(newvehicle, text="Category").place(x=10, y=155)

    vehicle1 = Entry(newvehicle)
    vehicle1.place(x=100, y=10)
    vehicle2 = Entry(newvehicle)
    vehicle2.place(x=100, y=47)
    vehicle3 = Entry(newvehicle)
    vehicle3.place(x=100, y=82)
    vehicle4 = Entry(newvehicle)
    vehicle4.place(x=100, y=120)
    vehicle5 = Entry(newvehicle)
    vehicle5.place(x=100, y=155)

    add_button = Button(newvehicle, text="Add", bg='#3498DB', fg='#FDFEFE', borderless=1, command=vehicle_info)
    add_button.place(x=115, y=193)


def search_info():
    global rental1
    global rental2
    global rental3
    global rental4
    global rental5
    global rental6
    global rental7
    global rental8
    global rental9
    global rental10

    global search1
    global search2
    global search3
    global search4

    reninfo = Tk()
    reninfo.title("Rental Information")
    reninfo.resizable(0, 0)
    reninfo.geometry("480x530")

    Label(reninfo, text="--------------- Search Available Vehicles --------------").place(x=15, y=10)
    Label(reninfo, text="Type").place(x=15, y=40)
    Label(reninfo, text="Category").place(x=15, y=70)
    Label(reninfo, text="Start Date(YYYY-MM-DD)").place(x=15, y=100)
    Label(reninfo, text="Return Date(YYYY-MM-DD)").place(x=15, y=130)

    search1 = Entry(reninfo)
    search1.place(x=55, y=40, width=308)
    search2 = Entry(reninfo)
    search2.place(x=75, y=70, width=288)
    search3 = Entry(reninfo)
    search3.place(x=177, y=100, width=186)
    search4 = Entry(reninfo)
    search4.place(x=187, y=130, width=178)
    Button(reninfo, text="Search", bg='#F5B041', fg='#1C2833', borderless=1,
           command=search_vehicle_info, height=115, width=90).place(x=370, y=42)

    Label(reninfo, text="---------------- Add Rental Information ----------------").place(x=15, y=180)
    Label(reninfo, text="CustID").place(x=15, y=210)
    Label(reninfo, text="VehicleID").place(x=15, y=240)
    Label(reninfo, text="StartDate").place(x=15, y=270)
    Label(reninfo, text="OrderDate").place(x=15, y=300)
    Label(reninfo, text="RentalType").place(x=15, y=330)
    Label(reninfo, text="Qty").place(x=15, y=360)
    Label(reninfo, text="ReturnDate").place(x=15, y=390)
    Label(reninfo, text="TotalAmount").place(x=15, y=420)
    Label(reninfo, text="PaymentDate").place(x=15, y=450)
    Label(reninfo, text="Returned").place(x=15, y=480)

    rental1 = Entry(reninfo)
    rental1.place(x=63, y=210, width=301)
    rental2 = Entry(reninfo)
    rental2.place(x=78, y=240, width=286)
    rental3 = Entry(reninfo)
    rental3.place(x=78, y=270, width=286)
    rental4 = Entry(reninfo)
    rental4.place(x=85, y=300, width=279)
    rental5 = Entry(reninfo)
    rental5.place(x=90, y=330, width=274)
    rental6 = Entry(reninfo)
    rental6.place(x=45, y=360, width=319)
    rental7 = Entry(reninfo)
    rental7.place(x=90, y=390, width=275)
    rental8 = Entry(reninfo)
    rental8.place(x=98, y=420, width=267)
    rental9 = Entry(reninfo)
    rental9.place(x=102, y=450, width=263)
    rental10 = Entry(reninfo)
    rental10.place(x=78, y=480, width=286)
    Button(reninfo, text="Add", bg='#F5B041', fg='#1C2833', borderless=1,
           command=add_Information, height=295, width=90).place(x=370, y=211)


def return_car():
    global return1
    global return2
    global return3
    global return4

    myreturn = Tk()
    myreturn.title("Retrieve & Update")
    myreturn.geometry("320x200")
    myreturn.resizable(0, 0)
    Label(myreturn, text="CustID").place(x=15, y=10)
    Label(myreturn, text="Name").place(x=15, y=40)
    Label(myreturn, text="Returned Date").place(x=15, y=70)
    Label(myreturn, text="VehicleID").place(x=15, y=100)

    return1 = Entry(myreturn)
    return1.place(x=70, y=10)
    return2 = Entry(myreturn)
    return2.place(x=70, y=40)
    return3 = Entry(myreturn)
    return3.place(x=110, y=70)
    return4 = Entry(myreturn)
    return4.place(x=80, y=100)

    Button(myreturn, text="Retrive", command=Retrive_info, bg='#F5B041', fg='#1C2833', borderless=1,
           height=40, width=90).place(x=40, y=140)
    Button(myreturn, text="Update", command=Update_info, bg='#F5B041', fg='#1C2833', borderless=1,
           height=40, width=90).place(x=170, y=140)


def ID():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        myID = Tk()
        myID.title("Customer Information")
        myID.geometry("300x100")
        data = "SELECT CustID, Name FROM CUSTOMER WHERE Customer.CustID='%s' " %view1.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        for record in fetch:
            print_id = "Customer ID: " + str(record[0]) + "\n"
        for record in fetch:
            print_name = "Name: " + str(record[1]) + "\n"
        Label(myID, text=print_id).place(x=15, y=5)
        Label(myID, text=print_name).place(x=15, y=30)

        data2 = "SELECT  FORMAT( SUM(TotalAMount ),2) FROM customer, rental WHERE Rental.CustID= Customer.CustID AND customer.Name='%s' " % view1.get()
        my_cursor.execute(data2)
        balance = my_cursor.fetchall()
        for record in balance:
            print_ba = "Balance Due: $" + str(record[0]) + "\n"
        Label(myID, text=print_ba).place(x=15, y=55)
        mydb.commit()
        view1.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def Name():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        myID = Tk()
        myID.title("Customer Information")
        data = "SELECT  Rental.CustID, Name , FORMAT( SUM(TotalAMount ),2) FROM customer, rental WHERE Rental.CustID= Customer.CustID AND PaymentDate IS NULL AND customer.Name='%s' " % view2.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print_record = ''
        for record in fetch:
            print_record += "Customer ID: " + str(record[0]) + "\n" + "Name: " + str(
                record[1]) + "\n" + "Balance Due: $" + str(record[2])

        result = Label(myID, text=print_record).place(x=20)
        mydb.commit()
        view2.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def part_Name():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        myID = Tk()
        myID.title("Customer Information")
        data = "SELECT  Rental.CustID, Name , FORMAT( SUM(TotalAMount ),2) FROM customer, Rental WHERE Rental.CustID= Customer.CustID AND PaymentDate IS NULL AND customer.Name LIKE '%%%s%%' " % view3.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print_record = ''
        for record in fetch:
            print_record += "\nCustomer ID: " + str(record[0]) + "\n" + "Name: " + str(
                record[1]) + "\n" + " Balance Due: $" + str(record[2])

        result = Label(myID, text=print_record).place(x=20)
        mydb.commit()
        view3.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def without_filter():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        myID = Tk()
        myID.title("Customer Information")
        data = "SELECT  customer.CustID, Name , FORMAT( SUM(TotalAMount ),2) FROM customer, Rental WHERE PaymentDate IS NULL AND Rental.CustID=customer.CustID GROUP BY TotalAMount ORDER BY TotalAmount ASC"
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print("Total rows without filter: ", my_cursor.rowcount)
        print_record = ''
        for record in fetch:
            print_record += "Customer ID: " + str(record[0]) + "\n" + "Name: " + str(
                record[1]) + "\n" + "Balance Due: $" + str(record[2])

        Label(myID, text=print_record).place(x=15)
        mydb.commit()
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def VIN():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        my_vehicle = Tk()
        my_vehicle.title("Vehicle Information")
        my_vehicle.geometry("300x100")
        data = "SELECT  Rental.VehicleID, Description, FORMAT( ((AVG(TotalAMount))/7),2) FROM Vehicle, Rental WHERE Rental.VehicleID = Vehicle.VehicleID AND PaymentDate IS NULL AND Rental.VehicleID='%s' " % v1.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        for record in fetch:
            print_VIN = "VIN: " + str(record[0]) + "\n"
        for record in fetch:
            print_des = "Description: " + str(record[1]) + "\n"
        for record in fetch:
            print_ba = "The average DAILY price: $" + str(record[2])

        Label(my_vehicle, text=print_VIN).place(x=15, y=5)
        Label(my_vehicle, text=print_des).place(x=15, y=35)
        Label(my_vehicle, text=print_ba).place(x=15, y=65)
        mydb.commit()
        v1.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def Description():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        my_vehicle = Tk()
        my_vehicle.title("Vehicle Information")
        my_vehicle.geometry("300x100")
        data = "SELECT  Rental.VehicleID, Description, FORMAT( ((AVG(TotalAMount))/7),2) FROM Vehicle, Rental WHERE Rental.VehicleID= Vehicle.VehicleID AND PaymentDate IS NULL AND vehicle.Description='%s' " % v2.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print_record = ''
        for record in fetch:
            print_record += "\nVIN: " + str(record[0]) + "\n" + "Description: " + str(
                record[1]) + "\n" + "The average DAILY price: $" + str(record[2]) + "\n"

        Label(my_vehicle, text=print_record).place(x=15)
        mydb.commit()
        v2.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def part_Description():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        my_vehicle = Tk()
        my_vehicle.title("Vehicle Information")
        my_vehicle.geometry("300x100")
        data = "SELECT  Rental.VehicleID, Description, FORMAT( ((AVG(TotalAMount))/7),2) FROM Vehicle, Rental WHERE Rental.VehicleID = Vehicle.VehicleID AND PaymentDate IS NULL AND Vehicle.Description LIKE '%%%s%%' " % v3.get()
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print("Total rows: ", my_cursor.rowcount)
        print_record = ''
        for record in fetch:
            print_record += "\nVIN: " + str(record[0]) + "\n" + "Description: " + str(
                record[1]) + "\n" + "The average DAILY price: $" + str(record[2]) + "\n"

        Label(my_vehicle, text=print_record).place(x=15)
        mydb.commit()
        v3.delete(0, 'end')
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def vehicle_without():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="poon1112",
        port="3306",
        database="CarRental2019"
    )

    my_cursor = mydb.cursor()

    try:
        my_vehicle = Tk()
        my_vehicle.title("Vehicle Information")
        my_vehicle.geometry("250x350")
        data = "SELECT  Rental.VehicleID, Description, FORMAT( ((AVG(TotalAMount))/7),2) FROM Vehicle, Rental WHERE Rental.VehicleID = Vehicle.VehicleID GROUP BY Description"
        my_cursor.execute(data)
        fetch = my_cursor.fetchall()
        print("Total rows: ", my_cursor.rowcount)
        print_record = ''
        for record in fetch:
            print_record += "\nVIN: " + str(record[0]) + "\n" + "Description: " + str(
                record[1]) + "\n" + "The average DAILY price: $" + str(record[2]) + "\n"

        Label(my_vehicle, text=print_record).place(x=15)
        mydb.commit()
        mydb.close()

    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def view_customer():
    global view1
    global view2
    global view3

    myview = Tk()
    myview.title("Customer Information")
    myview.geometry("500x200")
    myview.resizable(0, 0)

    Label(myview, text="Customer ID").place(x=20, y=10)
    view1 = Entry(myview)
    view1.place(x=130, y=10)

    Label(myview, text="Customer Name").place(x=20, y=50)
    view2 = Entry(myview)
    view2.place(x=130, y=50)

    Label(myview, text="Part Name").place(x=20, y=90)
    view3 = Entry(myview)
    view3.place(x=130, y=90)

    Button(myview, text="Search by ID", command=ID, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=330, y=10)
    Button(myview, text="Search by Name", command=Name, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=330, y=50)
    Button(myview, text="Search by Part", command=part_Name, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=330, y=90)
    Button(myview, text="Search without filter", command=without_filter, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=140, y=140)


def view_vehicle():
    global v1
    global v2
    global v3

    view = Tk()
    view.title("Vehicle Information")
    view.geometry("590x200")
    view.resizable(0, 0)

    Label(view, text="VIN").place(x=20, y=10)
    v1 = Entry(view)
    v1.place(x=60, y=10, width=270)

    Label(view, text="Description").place(x=20, y=50)
    v2 = Entry(view)
    v2.place(x=100, y=50, width=230)

    Label(view, text="Part of Description").place(x=20, y=90)
    v3 = Entry(view)
    v3.place(x=140, y=90)

    Button(view, text="Search by VIN", command=VIN, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=340, y=10)
    Button(view, text="Search by Description", command=Description, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=340, y=50)
    Button(view, text="Search by Part Description", command=part_Description, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=340, y=90)
    Button(view, text="Search without filter", command=vehicle_without, bg='#E74C3C',
           fg='#FDEFEF', borderless=1).place(x=160, y=140)


root = Tk()
root.title("CarRental 2019")
root.geometry("470x210")
root.resizable(0, 0)
root.configure(bg="#D5D8DC")

myFont = font.Font(weight="bold", size=14)
add_customer = Button(root, text="Add Customer", bg='#3498DB', fg='#1C2833', borderless=1, command=new_customer)
add_customer['font'] = myFont
add_customer.grid(row=0, column=0, pady=10, padx=10, ipadx=40, ipady=10)

add_vehicle = Button(root, text="Add Vehicle", bg='#3498DB', fg='#1C2833', borderless=1, command=new_vehicle)
add_vehicle['font'] = myFont
add_vehicle.grid(row=0, column=1, ipadx=40, ipady=10)

rental_info = Button(root, text="Rental Information", bg='#F5B041', fg='#1C2833', borderless=1, command=search_info)
rental_info['font'] = myFont
rental_info.grid(row=2, column=0, ipadx=28, padx=10, ipady=10)

update_info = Button(root, text="Retrieve & Update Info", bg='#F5B041', fg='#1C2833', borderless=1, command=return_car)
update_info['font'] = myFont
update_info.grid(row=2, column=1, ipadx=8, ipady=10, pady=10)

search_cus = Button(root, text="Search Customer", bg='#E74C3C', fg='#1C2833', borderless=1, command=view_customer)
search_cus['font'] = myFont
search_cus.grid(row=3, column=0, ipadx=30, ipady=10, pady=10)

search_veh = Button(root, text="Search Vehicle", bg='#E74C3C', fg='#1C2833', borderless=1, command=view_vehicle)
search_veh['font'] = myFont
search_veh.grid(row=3, column=1, ipadx=30, ipady=10)

mydb.commit()
mydb.close()
root.mainloop()

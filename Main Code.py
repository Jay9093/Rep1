#Importing modules
import mysql.connector as mys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from tkinter import ttk
import re
import random
import datetime

#Regular expression for email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#MAIN PAGE
#Specifying conditions
root = Tk()
root.geometry("1000x640")
root.title("Dollar Domaine")
root.resizable( True, True)
root['bg']='White'
screenwidth = root.winfo_screenwidth(); screenheight = root.winfo_screenheight()

#Function to exit main page/window
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you wish to exit?", parent=root)
    if sure == True:
        root.destroy()

#Protocol to be followed before exiting (as defined in Exit function)
root.protocol("WM_DELETE_WINDOW", Exit)

#Background image setting 
mainimage = Image.open("bg1.png")
siz = mainimage.resize((1000, 640), Image.ANTIALIAS)
mainimage1 = ImageTk.PhotoImage(siz)

#Creating a label for bg image
l1 = Label(image = mainimage1)
l1.pack()


#Retrieving data from mysql - Employee table under Admin_Supermarket database
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'Admin_Supermarket')
mycursor = mycon.cursor()
mycursor.execute("select * from employee")
mydata = mycursor.fetchall()

#Retrieving data from Stock table under Supermarket Database
mycon2 = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'Supermarket')
mycursor2 = mycon2.cursor()
mycursor2.execute("select * from Stock")
mydata2 = mycursor2.fetchall()

#Retrieving data from Customer table under Supermarket Database
mycursor3 = mycon2.cursor()
mycursor3.execute("Select * from Customer")
mydata3 = mycursor3.fetchall()

#Creating employee button
button1 = Button(root,background="White",foreground="White",activebackground="White",relief="sunken",borderwidth="0")
button1.place(relx=0.2, rely=0.7, width=152, height=110)
img2 = PhotoImage(file="Em.png")
button1.configure(image=img2)

#Creating admin button
button2 = Button(root,background="White", relief="sunken",foreground="White",borderwidth="0",activebackground="White")
button2.place(relx=0.2, rely=0.4, width=152, height=110)
img3 = PhotoImage(file="adm.png")
button2.configure(image=img3)

##########################################################################################################################################################################################

#EMPLOYEE PAGE
#On clicking employee button (Function defined as follows)
def emp():
    cart1 = []
    root.withdraw()
    root2 = Tk()
    root2.geometry("1000x640")
    root2.title("Dollar Domaine_EMPLOYEE")
    root2.resizable(0,0)
    #Frame created to place widgets
    frame1=Frame(root2,background="#005555") #Dark green 
    frame1.place(relwidth=1,relheight=1)

    #Title text - Employee Login
    l = Label(frame1, text = "EMPLOYEE LOGIN", bg = "#005555", fg = "#00F0C0")
    l.configure(font =("Display", 30))
    l.place(relx=0.32,rely=0.189)
    l2 = Label(frame1, text = "Please enter your Employee ID and Password.", bg = "#005555", fg = "White") 
    l2.configure(font =("Glide", 15))
    l2.place(relx = 0.29, rely = 0.288)

    #Collecting employee ID and Password to login
    user2id=Label(frame1,text="Employee ID",font=("Dreamwood", 15))
    user2id.place(relx=0.34,rely=0.419)
    i=Entry(frame1,font=("Lato",12))
    i.place(relx=0.47,rely=0.422)

    password2=Label(frame1,text="Password",font=("Dreamwood", 15))
    password2.place(relx=0.365,rely=0.519)
    s=Entry(frame1, show = "*", font=("Lato",12))
    s.place(relx=0.47,rely=0.522)

    #Function executed once logged in
    def emlogin():
        frame1.destroy()
        frame8=Frame(root2,background="#004444") 
        frame8.place(relwidth=1,relheight=1)
        #Title text
        text = Label(frame8, text = "Select any of the following : ", bg = "#004444", fg = "White")
        text.configure(font =("Andalus", 25))
        text.place(relx=0.312,rely=0.189)

        #Logout
        def logout():
            root2.withdraw()
            root.deiconify()
        log = Button(frame8,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
        log.place(relx=0.02,rely=0.02)
        log.configure(command=logout)
        
        #On clicking stock, the following options are displayed
        def stock():
            frame8.destroy()
            frame9 = Frame(root2, background = "#003333")
            frame9.place(relwidth=1,relheight=1)
            St=Label(frame9, text="Inventory Data - Tools",fg = "White", bg ="#003333", font=("Comic Sans",25))
            St.place(relx=0.345,rely=0.14)

            #Logout
            def logout():
                    root2.withdraw()
                    root.deiconify()
            log = Button(frame9,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame9,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame9.destroy(),emlogin()])
                
            #On clicking 'Add new item'
            def addstock():
                frame9.destroy()
                frame12 = Frame(root2, background = "#003333")
                frame12.place(relwidth=1,relheight=1)

                #BACK
                back = Button(frame12,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame12.destroy(),stock()])

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame12,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                add1=Label(frame12,text="Inventory Data",bg="#003333",fg="White")
                add1.config(font=("Display",30))
                add1.place(relx=0.37,rely=0.05)
                add2=Label(frame12,text="-- ADD NEW ITEM --",bg="#003333",fg="#E1FFB2")
                add2.config(font=("Lato", 18))
                add2.place(relx=0.39,rely=0.155)
                add3=Label(frame12,text="Enter The Details Of The Item ",bg="#003333",fg="#E1FFB2")
                add3.config(font=("Lato",16))
                add3.place(relx=0.355,rely=0.2295)

                #Getting details of the item to be added
                
                nnc=Label(frame12,text="Name_Category", width = 20, height = 1)
                nnc.config(font=("Dreamwood"))
                nnc.place(relx=0.25,rely=0.340)
                nnc1=Entry(frame12,font=("Lato",14))
                nnc1.place(relx=0.5,rely=0.340)

                bnd=Label(frame12,text="Brand", width = 20, height = 1)
                bnd.config(font=("Dreamwood"))
                bnd.place(relx=0.25,rely=0.460)
                bnd1=Entry(frame12,font=("Lato",14))
                bnd1.place(relx=0.5,rely=0.460)

                qty=Label(frame12,text="Quantity", width = 20, height = 1)
                qty.config(font=("Dreamwood"))
                qty.place(relx=0.25,rely=0.580)
                qty1=Entry(frame12,font=("Lato",14))
                qty1.place(relx=0.5,rely=0.580)

                pri=Label(frame12,text="Price", width = 20, height = 1)
                pri.config(font=("Dreamwood"))
                pri.place(relx=0.25,rely=0.71)
                pri1=Entry(frame12,font=("Lato",14))
                pri1.place(relx=0.5,rely=0.71)

                
                #Adding an item into the database
                def itemadd():
                    Name = nnc1.get()
                    Brand = bnd1.get()
                    Quan = qty1.get()
                    Price = pri1.get()
                    Quant = int(Quan)
                    Pi = float(Price)
                    try:
                        query = "insert into stock (Name_Category, Brand, Quantity, Price) values ('{0}', '{1}', {2}, {3})".format(Name, Brand, Quant, Pi)
                        mycursor2.execute(query)
                        mycon2.commit()
                        d3=Label(frame12, text="Updated Stock!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        d3.place(relx=0.58,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        d3.destroy()
                    except mys.Error as err:
                        print("Oops! Something went wrong: {}".format(err))

                #Checking done before adding item
                def checkadd():
                    Name = nnc1.get()
                    Brand = bnd1.get()
                    Quan = qty1.get()
                    Price = pri1.get()
                    if (Quan.isdigit()==True) and (Price.isdigit()==True):
                        itemadd()
                    else:
                        d2=Label(frame12, text="Please enter valid details.",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        d2.place(relx=0.58,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        d2.destroy()

                #Submitting item details to be added
                adD=Button(frame12, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Add",font="Andalus",relief = "raised",height=1,width=10)
                adD.place(relx=0.43,rely=0.85)
                adD.configure(command=checkadd)

            #On clicking 'Modify or Update details'
            def modstock():
                frame9.destroy()
                frame15 = Frame(root2, background = "#003333")
                frame15.place(relwidth=1,relheight=1)

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame15,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame15,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame15.destroy(),stock()])

                #Getting details
                add12=Label(frame15,text="Inventory Data",bg="#003333",fg="White")
                add12.config(font=("display",30))
                add12.place(relx=0.37,rely=0.05)
                add13=Label(frame15,text="-- Update an Item --",bg="#003333",fg="#E1FFB2")
                add13.config(font=("Lato",20))
                add13.place(relx=0.375,rely=0.155)
                add14=Label(frame15,text="Enter the details of the item to be updated",bg="#003333",fg="#E1FFB2")
                add14.config(font=("Lato",16))
                add14.place(relx=0.3,rely=0.235)

                nnc2=Label(frame15,text="ID",width=20,height=1)
                nnc2.config(font=("Dreamwood"))
                nnc2.place(relx=0.25,rely=0.34)
                nnc3=Entry(frame15,font=("Lato"))
                nnc3.place(relx=0.5,rely=0.340)

                nnc=Label(frame15,text="Name_Category",width=20,height=1)
                nnc.config(font=("Dreamwood"))
                nnc.place(relx=0.25,rely=0.43)
                nnc1=Entry(frame15,font=("Lato"))
                nnc1.place(relx=0.5,rely=0.435)

                bnd=Label(frame15,text="Brand",width=20,height=1)
                bnd.config(font=("Dreamwood"))
                bnd.place(relx=0.25,rely=0.52)
                bnd1=Entry(frame15,font=("Lato"))
                bnd1.place(relx=0.5,rely=0.52)

                qty=Label(frame15,text="Quantity",width=20,height=1)
                qty.config(font=("Dreamwood"))
                qty.place(relx=0.25,rely=0.61)
                qty1=Entry(frame15,font=("Lato"))
                qty1.place(relx=0.5,rely=0.61)

                pri=Label(frame15,text="Price",width=20,height=1)
                pri.config(font=("Dreamwood"))
                pri.place(relx=0.25,rely=0.7)
                pri1=Entry(frame15,font=("Lato"))
                pri1.place(relx=0.5,rely=0.7)

                #Updating details
                def upditem():
                    IId = nnc3.get()
                    Nam = nnc1.get()
                    Brnd = bnd1.get()
                    Qt = qty1.get()
                    Price = pri1.get()
                    try:
                        query = "Update stock set Name_Category = '"+Nam+"',Brand = '"+Brnd+"',Quantity = "+Qt+",Price = "+Price+" where Product_ID = "+IId
                        mycursor2.execute(query)
                        mycon2.commit()
                        d3=Label(frame15, text="Updated Stock!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        d3.place(relx=0.58,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        d3.destroy()
                    except mys.Error as err:
                        print("Oops! Something went wrong: {}".format(err))
                        
                #Checking done with details before updating
                def upditemchk():
                    IId = nnc3.get()
                    Nam = nnc1.get()
                    Brnd = bnd1.get()
                    Qt = qty1.get()
                    Price = pri1.get()
                    if IId.isdigit()!=True:
                        di2=Label(frame15, text="Enter a valid ID!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        di2.place(relx=0.58,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        di2.destroy()
                    else:
                        id1 = int(IId)
                        for row in mydata2:
                            if row[0]==id1:
                                if (Qt.isdigit()==True) and (Price.isdigit()==True):
                                    upditem()
                                    break
                                else:
                                     did2=Label(frame15, text="Please enter valid details.",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                                     did2.place(relx=0.58,rely=0.852)
                                     root2.update()
                                     time.sleep(2)
                                     did2.destroy()
                                     break
                        else:
                            did3=Label(frame15, text="Invalid ID, does not exist!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                            did3.place(relx=0.58,rely=0.852)
                            root2.update()
                            time.sleep(2)
                            did3.destroy()
                           
                #Button to submit
                add15=Button(frame15, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Update",font="Display",relief = "raised",height=1,width=10)
                add15.place(relx=0.43,rely=0.85)
                add15.configure(command=upditemchk)

            #On clicking 'Search or View details'
            def searchstock():
                frame9.destroy()
                frame14 = Frame(root2, background = "#003333")
                frame14.place(relwidth=1,relheight=1)

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame14,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame14,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame14.destroy(),stock()])

                #Getting details
                vrs=Label(frame14,text="Inventory Data",bg="#003333",fg="White")
                vrs.config(font=("display",30))
                vrs.place(relx=0.37,rely=0.05)
                vrs2=Label(frame14,text="-- Search and View --",bg="#003333",fg="#E1FFB2")
                vrs2.config(font=("Dreamwood",20))
                vrs2.place(relx=0.369,rely=0.155)
                vrs3=Label(frame14,text="Enter product ID to search item",bg="#003333",fg="#E1FFB2")
                vrs3.config(font=("Dreamwood",16))
                vrs3.place(relx=0.348,rely=0.2295)

                id3=Label(frame14,text="ID",width=10,height=1)
                id3.config(font=("Dreamwood"))
                id3.place(relx=0.348,rely=0.34)
                id5=Entry(frame14,font=("Lato",10))
                id5.place(relx=0.482,rely=0.345,relheight=0.035)

                #Searching to get details through id
                def searching1():
                    Idd = id5.get()
                    if Idd.isdigit():
                        Id = int(Idd)

                        flag = False
                        for row in mydata2:
                            if(Id==row[0]):
                                flag = True
                                break
                        if flag == True:
                            tree = ttk.Treeview(root2, height = 1)
                            tree["columns"] = ("one", "two", "three", "Four", "Five")
                            tree.column("one", width=100)
                            tree.column("two", width=250)
                            tree.column("three", width=150)
                            tree.column("Four", width=100)
                            tree.column("Five", width =100)
                            tree.heading("#0", anchor='w')
                            tree.column("#0", width=0)   
                            tree.heading("one", text="ID")
                            tree.heading("two", text="NAME_CATEGORY")
                            tree.heading("three", text="BRAND")
                            tree.heading("Four", text="QUANTITY")
                            tree.heading("Five", text="PRICE")
         
                            tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4]))
                            tree.place(relx=0.15, rely=0.5)
                            root2.update()
                            time.sleep(5)
                            tree.destroy()
                        elif flag == False:
                            er=Label(frame14, text="Product ID entered does not exist.",fg="#4A8FE3", bg ="#003333", font=("Dosis",16))
                            er.place(relx=0.348,rely=0.52)
                            root2.update()
                            time.sleep(2)
                            er.destroy()
                            
                    else:
                        erre=Label(frame14, text="Invalid entry. Try again!",fg="#4A8FE3", bg ="#003333", font=("Dosis",16))
                        erre.place(relx=0.348,rely=0.52)
                        root2.update()
                        time.sleep(2)
                        erre.destroy()
                   
                #Search button
                search=Button(frame14, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Search",font="Display",relief = "raised",height=1,width=10)
                search.place(relx=0.7,rely=0.337)
                search.configure(command=searching1)

                #TO VIEW STOCK DATA FROM MYSQL TABLE - TREEVIEW USED
                tree = ttk.Treeview(root2)
                tree["columns"] = ("one", "two", "three", "Four", "Five")
                tree.column("one", width=100)
                tree.column("two", width=250)
                tree.column("three", width=150)
                tree.column("Four", width=100)
                tree.column("Five", width =100)
                tree.heading("#0", anchor='w')
                tree.column("#0", width=0)   
                tree.heading("one", text="ID")
                tree.heading("two", text="NAME_CATEGORY")
                tree.heading("three", text="BRAND")
                tree.heading("Four", text="QUANTITY")
                tree.heading("Five", text="PRICE")

                cpt = 0 #Counter representing ID 
                for row in mydata2: #For row in stock table 
                   tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4]))
                   cpt += 1 # increment the ID
                   
                tree.place(relx=0.15, rely=0.62)


            #Deleting an item
            def delitem():
                frame9.destroy()
                frame13 = Frame(root2, background = "#003333")
                frame13.place(relwidth=1,relheight=1)

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame13,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame13,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame13.destroy(),stock()])
                
                #Getting ID to delete corresponding Item
                dele=Label(frame13,text="Inventory Data",bg="#003333",fg="White")
                dele.config(font=("Display",30))
                dele.place(relx=0.37,rely=0.05)
                dele1=Label(frame13,text="-- ITEM DELETION --",bg="#003333",fg="#E1FFB2")
                dele1.config(font=("Lato",18))
                dele1.place(relx=0.39,rely=0.155)
                dele2=Label(frame13,text="Enter Product ID to delete item",bg="#003333",fg="#E1FFB2")
                dele2.config(font=("Dreamwood",16))
                dele2.place(relx=0.348,rely=0.2295)

                id3a=Label(frame13,text="ID",width=10,height=1)
                id3a.config(font=("Dreamwood"))
                id3a.place(relx=0.348,rely=0.34)
                id4a=Entry(frame13,font=("Lato",10))
                id4a.place(relx=0.482,rely=0.345,relheight=0.035)

                #Deleting the item
                def delstock():
                    Iditem = id4a.get()
                    Idit = int(Iditem)
                    for row in mydata2:
                        if row[0]==Idit:
                            query="DELETE FROM STOCK WHERE Product_ID = {0}".format(Idit)
                            try:
                                mycursor2.execute(query)
                                mycon2.commit()
                                do=Label(frame13, text="Product details of the Item with the given ID deleted.",fg="#2DDBD7", bg ="#003333", font=("Arvo",16))
                                do.place(relx=0.244,rely=0.75)
                                root2.update()
                                time.sleep(2)
                                do.destroy()
                                break
                            except mys.Error as err:
                                print("Oops! Something went wrong: {}".format(err))
                    else:
                        er2=Label(frame13, text="Product ID entered does not exist.",fg="red", bg ="#003333", font=("Dosis",16))
                        er2.place(relx=0.339,rely=0.75)
                        root2.update()
                        time.sleep(2)
                        er2.destroy()
                    
                    
                #Checking done before deletion
                def checkitemdel():
                    IdItem = id4a.get()
                    if IdItem.isdigit():
                        delstock()
                    else:
                        eron1=Label(frame13, text="Please enter a valid Product ID.",fg="#2DDBD7", bg ="#003333", font=("Dosis",16))
                        eron1.place(relx=0.346,rely=0.75)
                        root2.update()
                        time.sleep(2)
                        eron1.destroy()
                    
                #Button to submit ID or Name entered
                delh=Button(frame13, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Delete",font="Display",relief = "raised",height=1,width=10)
                delh.place(relx=0.44,rely=0.43)
                delh.configure(command=checkitemdel)
                            
            #Button to add new item
            bu1 = Button(frame9,bg = "#00C3C3", activebackground = "#00C3C3", text = "Add New Item", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            bu1.place(relx=0.34,rely=0.29)
            bu1.configure(command=addstock)

            #Button to modify or update item details
            bu2 = Button(frame9,bg = "#00C3C3", activebackground = "#00C3C3", text = "Modify or Update Details", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            bu2.place(relx=0.34,rely=0.44)
            bu2.configure(command=modstock)

            #Button to search/view item details
            bu3 = Button(frame9,bg = "#00C3C3", activebackground = "#00C3C3", text = "Search or View Details", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            bu3.place(relx=0.34,rely=0.59)
            bu3.configure(command=searchstock)

            #Button to delete item
            bu4 = Button(frame9,bg = "#00C3C3", activebackground = "#00C3C3", text = "Delete Item", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            bu4.place(relx=0.34,rely=0.74)
            bu4.configure(command=delitem)

            #Stock quantity low warning generated
            def warn():
                for j in mydata2:
                    if j[3]<3:
                        messagebox.showwarning("Stock Warning", "Item "+j[1]+" Quantity low"+"\n"+"Visit stock now!",parent=root2)
            warn()
                     
        #On clicking customer, the following options are displayed
        def customer():
            frame8.destroy()
            frame10 = Frame(root2, background = "#003333")
            frame10.place(relwidth=1,relheight=1)
            St=Label(frame10, text="Customer Data - Tools",fg = "White", bg ="#003333", font=("Comic Sans",25))
            St.place(relx=0.345,rely=0.14)

            #Logout
            def logout():
                    root2.withdraw()
                    root.deiconify()
            log = Button(frame10,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame10,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame10.destroy(),emlogin()])

            #Executed on clicking 'Add new customer'
            def addcust():
                frame10.destroy()
                frame16 = Frame(root2, background = "#003333")
                frame16.place(relwidth=1,relheight=1)
        
                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame16,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame16,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame16.destroy(),customer()])
                
                #Getting customer details to be added
                add4=Label(frame16,text="Customer Data",bg="#003333",fg="White")
                add4.config(font=("Display",30))
                add4.place(relx=0.37,rely=0.05)
                add5=Label(frame16,text="-- CUSTOMER REGISTRATION --",bg="#003333",fg="#E1FFB2")
                add5.config(font=("Lato",17))
                add5.place(relx=0.34,rely=0.155)
                add6=Label(frame16,text="Enter The Details Of New customer",bg="#003333",fg="#E1FFB2")
                add6.config(font=("Lato",16))
                add6.place(relx=0.34,rely=0.2295)

                id5=Label(frame16,text="ID", width = 10, height = 1)
                id5.config(font=("Dreamwood"))
                id5.place(relx=0.1,rely=0.335)
                id6=Entry(frame16,font=("Lato"), width = 20)
                id6.place(relx=0.22,rely=0.335)

                name3=Label(frame16,text="Name", width = 10, height = 1)
                name3.config(font=("Dreamwood"))
                name3.place(relx=0.1,rely=0.48)
                name4=Entry(frame16,font=("Lato"), width = 20)
                name4.place(relx=0.22,rely=0.480)

                ph2=Label(frame16,text="Phone",width = 10, height = 1)
                ph2.config(font=("Dreamwood"))
                ph2.place(relx=0.53,rely=0.335)
                ph3=Entry(frame16,font=("Lato"), width = 20)
                ph3.place(relx=0.65,rely=0.335)

                address=Label(frame16,text="Address", width = 10, height = 1)
                address.config(font=("Dreamwood"))
                address.place(relx=0.53,rely=0.48)
                address1=Entry(frame16,font=("Lato"), width = 20)
                address1.place(relx=0.65,rely=0.480)

                hys=Label(frame16,text="Half Yearly Sales",width = 20, height = 1)
                hys.config(font=("Dreamwood"))
                hys.place(relx=0.1,rely=0.63)
                hys1=Entry(frame16,font=("Lato"), width = 11)
                hys1.place(relx=0.329,rely=0.63)

                #Adding customer details into database
                def custadd():
                    Cid = id6.get()
                    Name = name4.get()
                    Phone = ph3.get()
                    Address = address1.get()
                    Hys = hys1.get()
                    Halfys = int(Hys)
                    #Hys > 20k, Membership level 1, Discount 3%
                    #Hys >22k, Membership level 2, Discount 5%
                    #Hys >24k, Membership level 3, Discount 8%
                    #Hys > 28k, Membership level 4, Discount 10%
                    #Hys > 30k, Membership level 5, Discount 12%
                    Mem = 0   
                    Dis = 0
                    if Halfys >= 20000:
                        Mem = 1
                        Dis = 3
                    if Halfys >= 22000:
                        Mem = 2
                        Dis = 5
                    if Halfys >= 24000:
                        Mem = 3
                        Dis = 8
                    if Halfys >= 28000:
                        Mem = 4
                        Dis = 10
                    if Halfys >= 30000:
                        Mem = 5
                        Dis = 12
                           
                    for row in mydata3:
                        if row[0]!=Cid:
                            try:
                                query = "insert into customer values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}' )".format(Cid, Name, Phone, Address, Halfys, Mem, Dis)
                                mycursor3.execute(query)
                                mycon2.commit()
                                d=Label(frame16, text="Updated Customers!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                                d.place(relx=0.68,rely=0.852)
                                root2.update()
                                time.sleep(2)
                                d.destroy()
                                break
                            except:
                                mycon2.rollback()
                    else:
                        d22=Label(frame16, text="Try Update instead? ID exists.",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        d22.place(relx=0.68,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        d22.destroy()     

                #Checking if details entered are fit to be added
                def checkcustadd():
                    Cid = id6.get()
                    Name = name4.get()
                    Phone = ph3.get()
                    Address = address1.get()
                    Hys = hys1.get()
                    flag = False
                    if (Name.isalpha()) and (len(Phone)==10):
                            if (Hys.isdigit()):
                                flag = True
                    if flag == True:
                        custadd()
                    else:
                        e22=Label(frame16, text="Invalid entries. Try again.",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        e22.place(relx=0.68,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        e22.destroy()
                #Button to submit details
                add7=Button(frame16, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Add",font="Andalus",relief = "raised",height=1,width=10)
                add7.place(relx=0.65,rely=0.62)
                add7.configure(command=checkcustadd)

            #Executed on clicking 'Modify or Update details'
            def modcust():
                frame10.destroy()
                frame18 = Frame(root2, background = "#003333")
                frame18.place(relwidth=1,relheight=1)

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame18,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame18,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame18.destroy(),customer()])
                
                add8=Label(frame18,text="Customer Data",bg="#003333",fg="White")
                add8.config(font=("display",30))
                add8.place(relx=0.365,rely=0.05)
                add9=Label(frame18,text=" MODIFYING DETAILS ",bg="#003333",fg="#E1FFB2")
                add9.config(font=("Lato",18))
                add9.place(relx=0.373,rely=0.155)
                add10=Label(frame18,text="Enter Updated Customer Details",bg="#003333",fg="#E1FFB2")
                add10.config(font=("Lato",16))
                add10.place(relx=0.347,rely=0.2295)

                id9=Label(frame18,text="ID",width = 10, height = 1)
                id9.config(font=("Dreamwood"))
                id9.place(relx=0.1,rely=0.335)
                id10=Entry(frame18,font=("Lato"), width=20)
                id10.place(relx=0.22,rely=0.335)

                name5=Label(frame18,text="Name",width = 10, height = 1)
                name5.config(font=("Dreamwood"))
                name5.place(relx=0.1,rely=0.47)
                name6=Entry(frame18,font=("Lato"), width=20)
                name6.place(relx=0.22,rely=0.47)

                ph4=Label(frame18,text="Phone",width = 10, height = 1)
                ph4.config(font=("Dreamwood"))
                ph4.place(relx=0.53,rely=0.335)
                ph5=Entry(frame18,font=("Lato"), width=20)
                ph5.place(relx=0.65,rely=0.335)

                address2=Label(frame18,text="Address",width = 10, height = 1)
                address2.config(font=("Dreamwood"))
                address2.place(relx=0.53,rely=0.470)
                address3=Entry(frame18,font=("Lato"), width=20)
                address3.place(relx=0.65,rely=0.470)

                #Modifying details
                def updcust2():
                    Cid = id10.get()
                    Name = name6.get()
                    Phone = ph5.get()
                    Address = address3.get()
                    for row in mydata3:
                        if row[0]==Cid:
                            try:
                                query = "update customer set Customer_Name = '{0}', Phone_Number = '{1}', Address = '{2}' where Customer_ID = '{3}'".format(Name, Phone, Address, Cid) 
                                mycursor3.execute(query)
                                mycon2.commit()
                                d=Label(frame18, text="Updated Customer data!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                                d.place(relx=0.68,rely=0.852)
                                root2.update()
                                time.sleep(3)
                                d.destroy()
                                break
                            except:
                                mycon2.rollback()
                    else:
                        d22=Label(frame18, text="ID does not exist. Try again.",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        d22.place(relx=0.68,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        d22.destroy()     

                #Checking details entered
                def updcust1():
                    Cid = id10.get()
                    Name = name6.get()
                    Phone = ph5.get()
                    Address = address3.get()
                    if (Name.isalpha()) and (len(Phone)==10):
                        updcust2()
                    else:
                        e22=Label(frame18, text="Incorrect details. Try again. ",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        e22.place(relx=0.68,rely=0.852)
                        root2.update()
                        time.sleep(2)
                        e22.destroy()

                #Button to modify customer details
                add11=Button(frame18, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Submit",font="Andalus",relief = "raised",height=1,width=10)
                add11.place(relx=0.44,rely=0.71)
                add11.configure(command=updcust1)

            #Executed on clicking 'Search or view details'
            def searchdelcust():
                frame10.destroy()
                frame17 = Frame(root2, background = "#003333")
                frame17.place(relwidth=1,relheight=1)

                #Logout
                def logout():
                    root2.withdraw()
                    root.deiconify()
                log = Button(frame17,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
                log.place(relx=0.02,rely=0.02)
                log.configure(command=logout)

                #BACK
                back = Button(frame17,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[frame17.destroy(),customer()])

                #Getting details
                vsd=Label(frame17,text="Customer Data",bg="#003333",fg="White")
                vsd.config(font=("Display",30))
                vsd.place(relx=0.37,rely=0.05)
                vsd1=Label(frame17,text="-- VIEW, SEARCH, DELETE --",bg="#003333",fg="#E1FFB2")
                vsd1.config(font=("Lato",16))
                vsd1.place(relx=0.368,rely=0.155)

                id5=Label(frame17,text="ID", width = 10, height = 1)
                id5.config(font=("Dreamwood"))
                id5.place(relx=0.12,rely=0.339)
                id6=Entry(frame17,font=("Lato"), width = 20)
                id6.place(relx=0.24,rely=0.339)

                #Deleting the customer's details
                def delcust2():
                    IDC = id6.get()
                    flag = False
                    for row in mydata3:
                        if IDC == row[0]:
                            flag = True
                            #MYSQL QUERY TO DELETE
                            q1="DELETE FROM CUSTOMER WHERE Customer_ID = '{0}'".format(IDC)
                            try:
                                mycursor3.execute(q1)
                                mycon2.commit()
                                donee=Label(frame17, text="Customer data deleted.",fg="#4A8FE3", bg ="#003333", font=("Arvo",15))
                                donee.place(relx=0.12,rely=0.5)
                                root2.update()
                                time.sleep(2)
                                donee.destroy()
                                break
                            except:
                                mycon2.rollback()
                    if flag!=True:
                        erom=Label(frame17, text="Customer ID entered does not exist.",fg="#2DDBD7", bg ="#003333", font=("Dosis",16))
                        erom.place(relx=0.12,rely=0.5)
                        root2.update()
                        time.sleep(2)
                        erom.destroy()
                #Executed to delete customer
                def delcust():
                    IDC = id6.get()
                    if IDC.isalnum():
                        delcust2()
                    else:
                        ero1=Label(frame17, text="Please enter a valid Customer ID.",fg="#4A8FE3", bg ="#003333", font=("Dosis",18))
                        ero1.place(relx=0.12,rely=0.5)
                        root2.update()
                        time.sleep(3)
                        ero1.destroy()

                #Executed to search customer details
                def searchcust():
                    IDC2 = id6.get()
                    flag = False
                    for row in mydata3:
                        if (IDC2==row[0]):
                            flag = True
                            break
                    if flag == True:
                        tree = ttk.Treeview(root2, height = 1)
                        tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
                        tree.column("one", width=100)
                        tree.column("two", width=150)
                        tree.column("three", width=100)
                        tree.column("Four", width=200)
                        tree.column("Five", width =150)
                        tree.column("Six", width =120)
                        tree.column("Seven", width =120)
                        
                        tree.heading("#0", anchor='w')
                        tree.column("#0", width=0)   
                        tree.heading("one", text="ID")
                        tree.heading("two", text="NAME")
                        tree.heading("three", text="PHONE")
                        tree.heading("Four", text="ADDRESS")
                        tree.heading("Five", text="HALF YEARLY SALES")
                        tree.heading("Six", text="MEMBERSHIP LEVEL")
                        tree.heading("Seven", text="DISCOUNT %")

                        tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                        tree.place(relx=0.025, rely=0.48)
                        root2.update()
                        time.sleep(4)
                        tree.destroy()
                    else:
                        done1=Label(frame17, text="Invalid ID. Does not exist. Try again!",fg="#2DDBD7", bg ="#003333", font=("Arvo",15))
                        done1.place(relx=0.341,rely=0.5)
                        root2.update()
                        time.sleep(2)
                        done1.destroy()

                #Delete button
                delete1=Button(frame17, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Delete",font="Display",relief = "raised",height=1,width=10)
                delete1.place(relx=0.2,rely=0.85)
                delete1.configure(command=delcust)

                #Search button
                search1=Button(frame17, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Search",font="Display",relief = "raised",height=1,width=10)
                search1.place(relx=0.65,rely=0.85)
                search1.configure(command=searchcust)

                #TO VIEW CUSTOMER DETAILS
                tree = ttk.Treeview(root2, height = 5)
                tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
                tree.column("one", width=100)
                tree.column("two", width=150)
                tree.column("three", width=100)
                tree.column("Four", width=200)
                tree.column("Five", width =150)
                tree.column("Six", width =120)
                tree.column("Seven", width =120)
                
                tree.heading("#0", anchor='w')
                tree.column("#0", width=0)   
                tree.heading("one", text="ID")
                tree.heading("two", text="NAME")
                tree.heading("three", text="PHONE")
                tree.heading("Four", text="ADDRESS")
                tree.heading("Five", text="HALF YEARLY SALES")
                tree.heading("Six", text="MEMBERSHIP LEVEL")
                tree.heading("Seven", text="DISCOUNT %")

                cpt = 0 #Counter representing ID 
                for row in mydata3:
                   tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                   cpt += 1 # increment the ID
                   
                tree.place(relx=0.025, rely=0.62)

            #Button to add new customer
            butn1 = Button(frame10,bg = "#00C3C3", activebackground = "#00C3C3", text = "Add New Customer", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            butn1.place(relx=0.34,rely=0.29)
            butn1.configure(command=addcust)

            #Button to modify customer details
            butn2 = Button(frame10,bg = "#00C3C3", activebackground = "#00C3C3", text = "Modify or Update Details", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            butn2.place(relx=0.34,rely=0.44)
            butn2.configure(command=modcust)

            #Button to search/view customer details
            butn3 = Button(frame10,bg = "#00C3C3", activebackground = "#00C3C3", text = "Search or View Details", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            butn3.place(relx=0.34,rely=0.59)
            butn3.configure(command=searchdelcust)

            #Button to delete customer details
            butn4 = Button(frame10,bg = "#00C3C3", activebackground = "#00C3C3", text = "Delete Customer", font="Cairo 20 bold", relief = "raised", height = 1, width = 20)
            butn4.place(relx=0.34,rely=0.74)
            butn4.configure(command=searchdelcust)

        #After checking if the customer has been registered
        def billing():
            frame8.destroy()
            frame11 = Frame(root2, background = "#003333")
            frame11.place(relwidth=1,relheight=1)
            f = Label(frame11, text = "WELCOME TO BILLING!", bg = "#003333", fg = "White")
            f.configure(font =("Baskerville", 25))
            f.place(relx=0.321,rely=0.06)
             
            #Logout
            def logout():
                root2.withdraw()
                root.deiconify()
            log = Button(frame11,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame11,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame11.destroy(), emlogin()])

            #To get ID and Phone number of the customer
            C1D = Label(frame11,text="Customer ID",font=("Dreamwood", 15))
            C1D.place(relx=0.1,rely=0.2491)
            C1 = Entry(frame11, font=("Lato",12), width=20)
            C1.place(relx=0.224,rely=0.251)

            C2D = Label(frame11,text="Phone no",font=("Dreamwood", 15))
            C2D.place(relx=0.59,rely=0.249)
            C2 = Entry(frame11, font=("Lato",12), width=20)
            C2.place(relx=0.687,rely=0.25)

            #On clicking continue, continues to items
            def billcont2():
                frame11.destroy()
                framebill = Frame(root2, background = "#003333")
                framebill.place(relwidth=1,relheight=1)
                l = Label(framebill, text = "BILLING", bg = "#003333", fg = "White")
                l.configure(font =("Display", 30))
                l.place(relx=0.408,rely=0.0789)
                list1 = []
                for row in mydata2:
                    Name = row[1]
                    list1.append(Name)
                options_list = list1

                #BACK
                back = Button(framebill,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                back.place(relx=0.8985,rely=0.02)
                back.configure(command=lambda:[framebill.destroy(),billing()])

                value_inside = StringVar(framebill)
                value_inside.set("Name_Category")
                question_menu = OptionMenu(framebill, value_inside, *options_list)
                question_menu.place(relx=0.1, rely = 0.2)

                Qua=Label(framebill,text="Quantity",font=("Dreamwood", 15))
                Qua.place(relx=0.6,rely=0.2)
                Qua1=Entry(framebill,font=("Lato",12))
                Qua1.place(relx=0.7,rely=0.2)

                #Updating stock quantity according to purchase
                def billupdate():
                    today = datetime.datetime.now() 
                    total = 0
                    htotal = 0
                    rtotal = 0
                    Quan2 = Qua1.get()
                    if Quan2.isdigit():
                        Quan = int(Quan2)
                    else:
                        messagebox.showwarning("Quantity Warning", "Enter valid quantity!",parent=root2)
                    for a in range(len(cart1)):
                        for row in mydata2:
                            if cart1[a][0]==row[0]:
                                quan3 = row[3] - cart1[a][3]
                                query = "Update stock set Quantity = "+str(quan3)+" where Product_ID = "+str(cart1[a][0])
                                mycursor2.execute(query)
                                mycon2.commit()
                        #To determine amount = price * quantity
                        pitem = cart1[a][3]*cart1[a][4]
                        total = total + pitem
                        
                    yo=messagebox.askyesno("Discount Confirmation","Avail your discount?")
                    if yo:
                        for k in mydata3:
                            if HEYID == k[0]:
                                discount = k[6]      
                            rtotal=total
                        rprice = total*discount/100 #determining discounted amount
                        total = total - rprice
                    else:
                        rtotal = total
                        
                    for rw in mydata3:
                        if HEYID == rw[0]:
                            htotal = htotal + rw[4]
                    htotal = htotal + total
                    query = "Update customer set Half_Yearly_Sales = "+str(htotal)+" where Customer_ID = "+HEYID
                    mycursor3.execute(query)
                    mycon2.commit()

                    cusnem = namm
                    #FRAME FOR THE BILL
                    framebill.destroy()
                    framebill2 = Frame(root2, background = "#003333")
                    framebill2.place(relwidth=1,relheight=1)

                    #To print item details and final bill

                    tree = ttk.Treeview(root2, height = len(cart1))
                    tree["columns"] = ("one", "two", "three", "Four", "Five", "Six")
                    tree.column("one", width=100)
                    tree.column("two", width=250)
                    tree.column("three", width=150)
                    tree.column("Four", width=100)
                    tree.column("Five", width =100)
                    tree.column("Six", width =100)
                    tree.heading("#0", anchor='w')
                    tree.column("#0", width=0)   
                    tree.heading("one", text="ID")
                    tree.heading("two", text="NAME_CATEGORY")
                    tree.heading("three", text="BRAND")
                    tree.heading("Four", text="QUANTITY")
                    tree.heading("Five", text="PRICE")
                    tree.heading("Six", text="AMOUNT")
                    

                    for i in range(len(cart1)):
                        tree.insert('', 'end',values=[cart1[i][0], cart1[i][1], cart1[i][2], cart1[i][3], cart1[i][4], cart1[i][3]*cart1[i][4]])
                    tree.place(relx=0.1, rely=0.29)

                    label=Label(framebill2,text="DOLLAR DOMAINE",bg="#003333", fg = "#84F3F3")
                    label.config(font=("Courier",18))
                    label.place(relx=0.72,rely=0.05)
                    label1=Label(framebill2,text="-- Your neighbourhood market --\n 284, Adams Street, Mylapore\n Phone: 8693017974",bg="#003333", fg="White")
                    label1.config(font=("Courier",10))
                    label1.place(relx=0.69,rely=0.1)

                    #BACK
                    back = Button(framebill2,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
                    back.place(relx=0.02,rely=0.02)
                    back.configure(command=lambda:[framebill2.destroy(),billing()])

                    #RANDOMLY GENERATED BILL NUMBER
                    num=random.randint(1000,9999)
                    invoice="DDR"+str(num)
                    tots=Label(framebill2, text="INVOICE NUMBER: "+invoice,fg="White", bg ="#003333", font=("Courier",16))
                    tots.place(relx =0.07,rely=0.1)
                    
                    tot=Label(framebill2, text="Date & Time: "+str(today),fg="White", bg ="#003333", font=("Courier",16))
                    tot.place(relx =0.07,rely=0.15)

                    tote=Label(framebill2, text="Customer name: "+cusnem,fg="White", bg ="#003333", font=("Courier",16))
                    tote.place(relx =0.07,rely=0.2)
                    
                    tott=Label(framebill2, text="TOTAL AMT: "+str(rtotal),fg="White", bg ="#003333", font=("Courier",16))
                    tott.place(relx=0.1,rely=0.799)

                    tot1=Label(framebill2, text="(DISCOUNTED) AMOUNT: "+str(total),fg="White", bg ="#003333", font=("Courier",16))
                    tot1.place(relx=0.1,rely=0.86)

                    amtpaid=Label(framebill2,text="AMOUNT RECEIVED: ",font=("Courier", 15), bg = "#003333", fg = "White")
                    amtpaid.place(relx=0.682,rely=0.799)
                    amtpay=Entry(framebill2,font=("Lato",12))
                    amtpay.place(relx=0.69,rely=0.86)

                    def yes(): 
                        amt1 = amtpay.get()
                        change = 0
                        if amt1.isdigit():
                            change = int(amt1) - total
                            to=Label(framebill2, text="AMOUNT TO BE RETURNED: "+str(change),fg="White", bg ="#003333", font=("Courier",16))
                            to.place(relx=0.1,rely=0.916)
                        else:
                            toerr=Label(framebill2, text="Enter valid amount in rupees!",fg="Red", bg ="#003333", font=("Lato",12))
                            toerr.place(relx=0.69,rely=0.916)
                            root.update()
                            time.sleep(2)
                            toerr.destroy()
                    #Submitting amount received to calculate change
                    sub=Button(framebill2, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Submit",font="Courier",relief = "raised")
                    sub.place(relx=0.899,rely=0.92)
                    sub.configure(command=yes)

                    #TO GO TO NEW BILL
                    subb=Button(framebill2, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "New bill",font="Courier",relief = "raised")
                    subb.place(relx=0.771,rely=0.212)
                    subb.configure(command=lambda:[framebill2.destroy(),billing()])
                    
                #Function defined to display details of selected item
                def subill():
                    #Proceed button
                    sub2=Button(framebill, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Proceed",font="Courier",relief = "raised",height=1,width=10)
                    sub2.place(relx=0.6,rely=0.85)
                    sub2.configure(command=billupdate)
                    
                    op=messagebox.askyesno("Bill Confirmation","Are you sure that you want to add this item to the cart?")
                    if op:
                        Nm = value_inside.get()
                        Quan2 = Qua1.get()
                        Quan = int(Quan2)
                        for row in mydata2:
                            if Nm == row[1]:
                                cquan = row[3]
                                Q = str(cquan)
                        if Quan > cquan:
                            messagebox.showwarning("Quantity Warning", "Item quantity available - "+Q+". Enter valid quantity",parent=root2)
                        else:
                            for row in mydata2:
                                if Nm == row[1]:
                                    row1 = list(row)
                                    row1[3] = Quan
                                    cart1.append(row1)
                                
                            tree = ttk.Treeview(root2, height = len(cart1))
                            tree["columns"] = ("one", "two", "three", "Four", "Five")
                            tree.column("one", width=100)
                            tree.column("two", width=250)
                            tree.column("three", width=150)
                            tree.column("Four", width=100)
                            tree.column("Five", width =100)
                            tree.heading("#0", anchor='w')
                            tree.column("#0", width=0)   
                            tree.heading("one", text="ID")
                            tree.heading("two", text="NAME_CATEGORY")
                            tree.heading("three", text="BRAND")
                            tree.heading("Four", text="QUANTITY")
                            tree.heading("Five", text="PRICE")

                            for i in range(len(cart1)):
                                tree.insert('', 'end',values=[cart1[i][0], cart1[i][1], cart1[i][2], cart1[i][3], cart1[i][4]])
                            tree.place(relx=0.15, rely=0.3)


                #Submit button
                sub=Button(framebill, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Add to Cart",font="Courier",relief = "raised",height=1,width=16)
                sub.place(relx=0.2,rely=0.85)
                sub.configure(command=subill)
 
            #On clicking submit, to print membership level and discount
            def disc():
                Id = C1.get()
                global HEYID
                HEYID = Id
                Ph = C2.get()
                i = True
                for row in mydata3:
                    if (row[0]== Id) and (row[2]==Ph):
                        global namm
                        namm = row[1]
                        x = row[5]
                        y = row[6]
                        i = False

                if i == False:
                    Show = Label(frame11,text="Membership level",font=("Dreamwood", 15))
                    Show.place(relx=0.1,rely=0.45)
                    Show1 = Label(frame11,text= x, font=("Lato",15), width=10, bg = "#B9FE9B")
                    Show1.place(relx=0.2762,rely=0.45)
                    Show2 = Label(frame11,text="Discount %",font=("Dreamwood", 15))
                    Show2.place(relx=0.59,rely=0.45)
                    Show3 = Label(frame11,text=y, font=("Lato",15), width=10, bg = "#b9fe9b")
                    Show3.place(relx=0.71,rely=0.45)

                    #Continue button
                    cont=Button(frame11, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Continue",font="Courier",relief = "raised",height=1,width=10)
                    cont.place(relx=0.65,rely=0.85)
                    cont.configure(command=billcont2)
                else:
                    er1=Label(frame11, text="Enter valid details!",fg="#C8FFCD", bg ="#005555", font=("Garamond",18))
                    er1.place(relx=0.359,rely=0.62)
                    root2.update()
                    time.sleep(2)
                    er1.destroy()  

            #Submit button
            sub=Button(frame11, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Submit",font="Courier",relief = "raised",height=1,width=10)
            sub.place(relx=0.2,rely=0.85)
            sub.configure(command=disc)


        #On clicking billing, the following checing is done 
        def bilcheck():
            text1 = Label(frame8, text = "Has the customer been registered?", bg = "#004444", fg = "White")
            text1.configure(font =("Garamond", 20))
            text1.place(relx=0.31,rely=0.689)

            #Button 'Yes' to proceed to billing
            b1 = Button(frame8, bg = "#F4FF77", activebackground = "#F4FF77", text ="Yes", font="Andalus 15", height = 1, width = 8) 
            b1.place(relx=0.36,rely=0.82)
            b1.configure(command=billing) 

            #Button 'No' to register customer first before moving to billing
            b2 = Button(frame8, bg = "#F4FF77", activebackground = "#F4FF77", text ="No", font="Andalus 15", height = 1, width = 8)
            b2.place(relx=0.522,rely=0.82)
            #Redirection to Customer data tools
            b2.configure(command=customer)

        #Stock Button
        inv = Button(frame8, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "    Stock    ", font="Andalus 18", relief = "raised")
        inv.place(relx=0.42,rely=0.56)
        inv.configure(command=stock)
        
        #Customer Button
        cus = Button(frame8, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "Customers", font="Andalus 18", relief = "raised")
        cus.place(relx=0.42,rely=0.32)
        cus.configure(command=customer)
        
        #Billing Button
        bil = Button(frame8, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "    Billing   ", font="Andalus 18", relief = "raised")
        bil.place(relx=0.42,rely=0.44)
        bil.configure(command=bilcheck)

    #Security check for logging in
    def emcheck():
        Id = i.get()
        Psd = s.get()
        flag = False
        for row in mydata:
            if row[0] == Id:
                flag = True
                if row[4] == Psd:
                    done1=Label(frame1, text="Login successful!",fg="#C8FFCD", bg ="#005555", font=("Garamond",18))
                    done1.place(relx=0.426,rely=0.77)
                    root2.update()
                    time.sleep(1)
                    done1.destroy()
                    emlogin()
                else:
                    erpas=Label(frame1, text="Incorrect Password. Please try again!",fg="#C8FFCD", bg ="#005555", font=("Garamond",18))
                    erpas.place(relx=0.328,rely=0.77)
                    root2.update()
                    time.sleep(2)
                    erpas.destroy()
        if flag!= True:
            erlog=Label(frame1, text="Incorrect ID. Please try again!",fg="#C8FFCD", bg ="#005555", font=("Garamond",18))
            erlog.place(relx=0.358,rely=0.77)
            root2.update()
            time.sleep(2)
            erlog.destroy()
                

    #To exit the window (Exit button)
    def exitt2():
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root2)
        if sure == True:
            root2.destroy()
            root.destroy()

    root2.protocol("WM_DELETE_WINDOW", exitt2)
    #Login button
    log2 = Button(frame1, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "Login", font="Andalus 15", relief = "flat", height = 1, width = 10)
    log2.place(relx=0.45,rely=0.65)
    log2.configure(command=emcheck)

#Command of Employee button
button1.configure(command=emp)


##################################################################################################################################################################
#ADMIN PAGE
#On clicking admin button (Function as defined below)
def adm():
    root.withdraw() #Main page disappears
    root3 = Tk()
    root3.geometry("1000x640")
    root3.title("Dollar Domaine_ADMIN")
    root3.resizable(0,0)
    #Frame created to place widgets
    frame2=Frame(root3,background="#010057") #Dark blue
    frame2.place(relwidth=1,relheight=1)

    #Title text - Login page
    l = Label(frame2, text = "ADMIN LOGIN", bg = "#010057", fg = "White")
    l.configure(font =("Display", 30))
    l.place(relx=0.37,rely=0.189)
    l2 = Label(frame2, text = "Please enter your Username (ID) and Password. ", bg = "#010057", fg = "#A2D0FA") #Lighter blue shade
    l2.configure(font =("Glide", 15))
    l2.place(relx = 0.29, rely = 0.288)

    #Username and Password - ADMIN, 7063
    userid=Label(frame2,text="Username",font=("Dreamwood", 15))
    userid.place(relx=0.36,rely=0.419)
    e=Entry(frame2,font=("Lato",12))
    e.place(relx=0.47,rely=0.422)

    password=Label(frame2,text="Password",font=("Dreamwood", 15))
    password.place(relx=0.36,rely=0.519)
    p=Entry(frame2, show = "*", font=("Lato",12))
    p.place(relx=0.47,rely=0.522)
    
    #Login button
    log = Button(frame2, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "Login", font="Andalus 15", relief = "flat", height = 1, width = 10)
    log.place(relx=0.45,rely=0.65)
        
    #Opening page showing employee data and actions (Login successful)
    def logadm():
        frame2.destroy()
        frame3 = Frame(root3,background = "#02006C")
        frame3.place(relwidth=1,relheight=1)
        Det=Label(frame3, text="Employee Data - Tools",fg = "White", bg ="#02006C", font=("Comic Sans",25))
        Det.place(relx=0.345,rely=0.14)

        #Logout
        def logout():
                root3.withdraw()
                root.deiconify()
        log = Button(frame3,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
        log.place(relx=0.02,rely=0.02)
        log.configure(command=logout)

        #Executed on clicking 'Add New Employee'
        def addd():
            frame3.destroy()
            frame4 = Frame(root3,background = "#010048")
            frame4.place(relwidth=1,relheight=1)

            #Logout
            def logout():
                root3.withdraw()
                root.deiconify()
            log = Button(frame4,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame4,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame4.destroy(),logadm()])
                
            Add = Label(frame4, text="EMPLOYEE DATA",bg ="#010048",fg = "White", font=("DISPLAY",25))
            Add.place(relx=0.359,rely=0.111)
            Add2 = Label(frame4, text = "- Add new employee details -", bg = "#010048", fg = "#45FFEA")
            Add2.configure(font =("Glide", 15))
            Add2.place(relx = 0.369, rely = 0.199)

            #To get ID of the new employee
            EmpID = Label(frame4,text="Employee ID",font=("Dreamwood", 15))
            EmpID.place(relx=0.1,rely=0.34)
            E1 = Entry(frame4, font=("Lato",12), width=21)
            E1.place(relx=0.224,rely=0.345)

            #To get Name of the new employee
            EmpName = Label(frame4,text="Name",font=("Dreamwood", 15))
            EmpName.place(relx=0.1,rely=0.488)
            E2 = Entry(frame4, font=("Lato",12), width=28)
            E2.place(relx=0.162,rely=0.49)

            #To get Phone number of the new employee
            EmpNo = Label(frame4,text="Ph. Number",font=("Dreamwood", 15))
            EmpNo.place(relx=0.1,rely=0.64)
            E3 = Entry(frame4, font=("Lato",12), width=22)
            E3.place(relx=0.214,rely=0.643)

            #To get the Salary of the new employee
            EmpSal = Label(frame4,text="Salary (Rs)",font=("Dreamwood", 15))
            EmpSal.place(relx=0.588,rely=0.338)
            E7 = Entry(frame4, font=("Lato",12))
            E7.place(relx=0.699,rely=0.34)

            #To get Email ID of the new employee
            EmpEmail = Label(frame4,text="Email ID",font=("Dreamwood", 15))
            EmpEmail.place(relx=0.588,rely=0.489)
            E4 = Entry(frame4, font=("Lato",12), width=23)
            E4.place(relx=0.674,rely=0.492)

            #To get the password
            EmpPsw = Label(frame4,text="Password",font=("Dreamwood", 15))
            EmpPsw.place(relx=0.588,rely=0.639)
            E5 = Entry(frame4, font=("Lato",12), width=21)
            E5.place(relx=0.687,rely=0.642)

            #To get the Home Address of the employee
            EmpAd = Label(frame4,text="Address",font=("Dreamwood", 15))
            EmpAd.place(relx=0.1,rely=0.79)
            E6 = Entry(frame4, font=("Lato",12), width = 35)
            E6.place(relx=0.184,rely=0.793)

            #Button to submit details entered
            De = Button(frame4, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "Submit", font="Courier 15 bold", relief = "raised", height = 1, width = 10)
            De.place(relx=0.699,rely=0.821)

            #Adding new employee details into employee table
            def adsub():
                idEm = E1.get()
                Nam = E2.get()
                Ph = E3.get()
                Mail = E4.get()
                Pasd = E5.get()
                Ads = E6.get()
                Sal = E7.get()
                salys = int(Sal)
                for row in mydata:
                    if row[0]!=idEm:
                        try:
                            query = "insert into employee values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6} )".format(idEm, Nam, Ph, Mail, Pasd, Ads, salys)
                            mycursor.execute(query)
                            mycon.commit()
                            d=Label(frame4, text="Updated Employee!",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                            d.place(relx=0.68,rely=0.92)
                            root3.update()
                            time.sleep(2)
                            d.destroy()
                            break
                        except:
                            mycon.rollback()
                else:
                    d22=Label(frame4, text="Try Update instead? ID exists.",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                    d22.place(relx=0.68,rely=0.92)
                    root3.update()
                    time.sleep(2)
                    d22.destroy()     

            #Checking if details entered are okay to be added
            def subch():
                idEm = E1.get()
                Nam = E2.get()
                Ph = E3.get()
                Mail = E4.get()
                Pasd = E5.get()
                Ads = E6.get()
                Sal = E7.get()
                flag = False
                if (Nam.isalpha())and (len(Ph)==10):
                    if (re.fullmatch(regex, Mail)):
                        if Sal.isdigit():
                           adsub()
                        else:
                            doo=Label(frame4, text="Incorrect salary",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                            doo.place(relx=0.244,rely=0.89)
                            root3.update()
                            time.sleep(2)
                            doo.destroy()
                    else:
                        doo2=Label(frame4, text="Incorrect Mail ID",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                        doo2.place(relx=0.244,rely=0.89)
                        root3.update()
                        time.sleep(2)
                        doo2.destroy()
                else:
                    doo3=Label(frame4, text="Please enter valid details only.",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                    doo3.place(relx=0.244,rely=0.852)
                    root3.update()
                    time.sleep(2)
                    doo3.destroy()
                        
            #Command of submit button
            De.configure(command=subch)

        #Executed on clicking 'Modify or Update Details'
        def modemp():
            frame3.destroy()
            frame6 = Frame(root3,background = "#010048")
            frame6.place(relwidth=1,relheight=1)

            #Logout
            def logout():
                root3.withdraw()
                root.deiconify()
            log = Button(frame6,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame6,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame6.destroy(),logadm()])
            
            up1=Label(frame6,text="EMPLOYEE DATA",bg="#010048",fg="White")
            up1.config(font=("display",25))
            up1.place(relx=0.37,rely=0.05)
            up2=Label(frame6,text="-- Updating Employee Details --",bg="#010048",fg="#45FFEA")
            up2.config(font=("Glide",15))
            up2.place(relx=0.37, rely=0.155)
            up3=Label(frame6,text="Enter the employee details to be updated",bg="#010048",fg="#45FFEA")
            up3.config(font=("Lato",16))
            up3.place(relx=0.32,rely=0.235)

            #Getting details to update 
            n=Label(frame6,text="ID",width=20,height=1)
            n.config(font=("Dreamwood"))
            n.place(relx=0.27,rely=0.34)
            nn=Entry(frame6,font=("Lato"))
            nn.place(relx=0.525,rely=0.340)

            n1=Label(frame6,text="Address",width=20,height=1)
            n1.config(font=("Dreamwood"))
            n1.place(relx=0.27,rely=0.435)
            nn1=Entry(frame6,font=("Lato"))
            nn1.place(relx=0.525,rely=0.435)

            bn=Label(frame6,text="Phone Number",width=20,height=1)
            bn.config(font=("Dreamwood"))
            bn.place(relx=0.27,rely=0.52)
            bn1=Entry(frame6,font=("Lato"))
            bn1.place(relx=0.525,rely=0.52)

            qt=Label(frame6,text="Email",width=20,height=1)
            qt.config(font=("Dreamwood"))
            qt.place(relx=0.27,rely=0.61)
            qt1=Entry(frame6,font=("Lato"))
            qt1.place(relx=0.525,rely=0.61)

            pr2=Label(frame6,text="Password",width=20,height=1)
            pr2.config(font=("Dreamwood"))
            pr2.place(relx=0.27,rely=0.7)
            pr3=Entry(frame6,font=("Lato"))
            pr3.place(relx=0.525,rely=0.7)

            pr4=Label(frame6,text="Salary",width=20,height=1)
            pr4.config(font=("Dreamwood"))
            pr4.place(relx=0.27,rely=0.79)
            pr5=Entry(frame6,font=("Lato"))
            pr5.place(relx=0.525,rely=0.79)

            #Into the database
            def modupdate():
                Id = nn.get()
                Address = nn1.get()
                Phon = bn1.get()
                Email = qt1.get()
                Pas = pr3.get()
                Sala = pr5.get()
                for row in mydata:
                    if (row[0]==Id):
                        try:
                            query = "Update employee set Emp_Address = '"+Address+"',Emp_Phone_Number = '"+Phon+"',Emp_Email = '"+Email+"',Emp_Password = '"+Pas+"',Salary = "+Sala+" where Employee_ID = '{0}'".format(Id)
                            mycursor.execute(query)
                            mycon.commit()
                            d3=Label(frame6, text="Updated Employee!",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                            d3.place(relx=0.58,rely=0.852)
                            root3.update()
                            time.sleep(2)
                            d3.destroy()
                            break
                        except mys.Error as err:
                                print("Oops! Something went wrong: {}".format(err))
                else:
                    d22=Label(frame6, text="Try Add instead? ID does not exist.",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                    d22.place(relx=0.68,rely=0.92)
                    root3.update()
                    time.sleep(2)
                    d22.destroy()
                       

            #Updating details
            def updatemod():
                Id = nn.get()
                Address = nn1.get()
                Phon = bn1.get()
                Email = qt1.get()
                Pas = pr3.get()
                Sala = pr5.get()
                if (len(Phon)==10):
                    if (re.fullmatch(regex, Email)):
                        if Sala.isdigit():
                            modupdate()
                        else:
                            doo=Label(frame6, text="Incorrect salary",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                            doo.place(relx=0.65,rely=0.918)
                            root3.update()
                            time.sleep(2)
                            doo.destroy()
                    else:
                        doo2=Label(frame6, text="Incorrect Mail ID",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                        doo2.place(relx=0.65,rely=0.918)
                        root3.update()
                        time.sleep(2)
                        doo2.destroy()
                else:
                    doo3=Label(frame6, text="Please enter valid details only.",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                    doo3.place(relx=0.65,rely=0.918)
                    root3.update()
                    time.sleep(2)
                    doo3.destroy()

            
            #Update button
            upd=Button(frame6, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Update",font="Display",relief = "raised",height=1,width=10)
            upd.place(relx=0.45,rely=0.88)
            #Command of update button
            upd.configure(command=updatemod)

        #Executed on clicking 'Search or View Details'
        def empview():
            frame3.destroy()
            frame7 = Frame(root3,background = "#010048")
            frame7.place(relwidth=1,relheight=1)

            #LOGOUT
            def logout():
                root3.withdraw()
                root.deiconify()
            log = Button(frame7,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame7,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame7.destroy(),logadm()])

            up = Label(frame7, text="EMPLOYEE DATA",bg ="#010048",fg = "White", font=("DISPLAY",25))
            up.place(relx=0.363,rely=0.07)
            up2 = Label(frame7, text = "- Search & View -", bg = "#010048", fg = "#45FFEA")
            up2.configure(font =("Glide", 15))
            up2.place(relx = 0.422, rely = 0.17)
            vrs3=Label(frame7,text="Enter employee ID or Name to be searched",bg="#010048",fg="#45FFEA")
            vrs3.config(font=("Dreamwood",16))
            vrs3.place(relx=0.30,rely=0.2295)

            id3=Label(frame7,text="ID",width=10,height=1)
            id3.config(font=("Dreamwood"))
            id3.place(relx=0.348,rely=0.34)
            id4=Entry(frame7,font=("Lato",10))
            id4.place(relx=0.482,rely=0.345,relheight=0.035)

            #Checking done with ID to search details
            def searcheck():
                Id = id4.get()
                flag = False
                for row in mydata:
                    if (row[0]==Id):
                        flag = True
                        break
                if flag == True:
                    tree = ttk.Treeview(root3, height = 1)
                    tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
                    tree.column("one", width=100)
                    tree.column("two", width=100)
                    tree.column("three", width=100)
                    tree.column("Four", width=150)
                    tree.column("Five", width =100)
                    tree.column("Six", width =200)
                    tree.column("Seven", width =100)
                        
                    tree.heading("#0", anchor='w')
                    tree.column("#0", width=0)   
                    tree.heading("one", text="ID")
                    tree.heading("two", text="NAME")
                    tree.heading("three", text="PHONE")
                    tree.heading("Four", text="EMAIL")
                    tree.heading("Five", text="PASSWORD")
                    tree.heading("Six", text="ADDRESS")
                    tree.heading("Seven", text="SALARY")

                    tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                    tree.place(relx=0.079, rely=0.54)
                    root3.update()
                    time.sleep(4)
                    tree.destroy()
                else:
                    done=Label(frame7, text="Invalid ID. Does not exist. Try again!",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                    done.place(relx=0.341,rely=0.65)
                    root3.update()
                    time.sleep(2)
                    done.destroy()
            
            #Search button
            search=Button(frame7, bg ="#4A8FE3", activebackground ="#4A8FE3",text = "Search",font="Andalus",relief = "raised",height=1,width=10)
            search.place(relx=0.44,rely=0.43)
            search.configure(command=searcheck)

            #TO VIEW DETAILS
            tree = ttk.Treeview(root3, height = 5)
            tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
            tree.column("one", width=100)
            tree.column("two", width=100)
            tree.column("three", width=100)
            tree.column("Four", width=150)
            tree.column("Five", width =100)
            tree.column("Six", width =200)
            tree.column("Seven", width =100)
                
            tree.heading("#0", anchor='w')
            tree.column("#0", width=0)   
            tree.heading("one", text="ID")
            tree.heading("two", text="NAME")
            tree.heading("three", text="PHONE")
            tree.heading("Four", text="EMAIL")
            tree.heading("Five", text="PASSWORD")
            tree.heading("Six", text="ADDRESS")
            tree.heading("Seven", text="SALARY")

            cpt = 0 #Counter representing ID 
            for row in mydata:
                tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                cpt += 1 # increment the ID
                
            tree.place(relx=0.079, rely=0.74)

        #Executed on clicking 'Delete an Employee'
        def delemp():
            frame3.destroy()
            frame5 = Frame(root3,background = "#010048")
            frame5.place(relwidth=1,relheight=1)

            #Logout
            def logout():
                root3.withdraw()
                root.deiconify()
            log = Button(frame5,bg = "Black",fg = "White", activebackground = "Blue", text = "Logout", font="Chiller 22", relief = "groove")
            log.place(relx=0.02,rely=0.02)
            log.configure(command=logout)

            #BACK
            back = Button(frame5,bg = "Black",fg = "White", activebackground = "Blue", text = "Back", font="Chiller 22", relief = "groove")
            back.place(relx=0.8985,rely=0.02)
            back.configure(command=lambda:[frame5.destroy(),logadm()])
                
            Del = Label(frame5, text="EMPLOYEE DATA",bg ="#010048",fg = "White", font=("DISPLAY",25))
            Del.place(relx=0.359,rely=0.111)
            Del2 = Label(frame5, text = "Enter ID of the employee to delete details", bg = "#010048", fg = "#45FFEA")
            Del2.configure(font =("Glide", 15))
            Del2.place(relx = 0.312, rely = 0.199)

            #To get employee ID
            Empid = Label(frame5,text="Enter ID",font=("Dreamwood", 15))
            Empid.place(relx=0.36,rely=0.416)
            ED = Entry(frame5, font=("Lato",12))
            ED.place(relx=0.45,rely=0.419)

            #Button to submit
            Sub1 = Button(frame5, bg = "#4A8FE3", activebackground = "#4A8FE3", text = "Submit", font="Courier 15 bold", relief = "raised", height = 1, width = 10)
            Sub1.place(relx=0.43,rely=0.55)

            #Deleting an employee's details from employee table once ID is checked
            def delemp():
                IDE = ED.get()
                for row in mydata:
                    if IDE == row[0]:
                        
                        #MYSQL QUERY TO DELETE
                        q1="DELETE FROM EMPLOYEE WHERE Employee_ID = '{0}'".format(IDE)
                        try:
                            mycursor.execute(q1)
                            mycon.commit()
                            done=Label(frame5, text="Employee details of the employee with the given ID deleted.",fg="#2DDBD7", bg ="#010048", font=("Arvo",15))
                            done.place(relx=0.244,rely=0.75)
                            root3.update()
                            time.sleep(2)
                            done.destroy()
                            break
                        except:
                            mycon.rollback()
                        
                else:
                    ero2=Label(frame5, text="Employee ID entered does not exist.",fg="#2DDBD7", bg ="#010048", font=("Dosis",18))
                    ero2.place(relx=0.312,rely=0.75)
                    root3.update()
                    time.sleep(2)
                    ero2.destroy()
                    

            #Checks ID entered (Function executed on clicking submit)
            def delcheck():
                IDE = ED.get()
                if IDE.isalnum():
                    delemp()
                else:
                    ero1=Label(frame5, text="Please enter a valid Employee ID.",fg="#2DDBD7", bg ="#010048", font=("Dosis",18))
                    ero1.place(relx=0.312,rely=0.75)
                    root3.update()
                    time.sleep(3)
                    ero1.destroy()
                
            #Command of the submit button
            Sub1.configure(command=delcheck)

        #Button to add new employee
        b1 = Button(frame3,bg = "#2CBFFA", activebackground = "#2CBFFA", text = "Add New Employee", font="Geneva 20 bold", relief = "raised", height = 1, width = 20)
        b1.place(relx=0.34,rely=0.29)
        b1.configure(command=addd)

        #Button to modify employee details
        b2 = Button(frame3,bg = "#2CBFFA", activebackground = "#2CBFFA", text = "Modify or Update Details", font="Geneva 20 bold", relief = "raised", height = 1, width = 20)
        b2.place(relx=0.34,rely=0.44)
        b2.configure(command=modemp)

        #Button to search/view employee details
        b3 = Button(frame3,bg = "#2CBFFA", activebackground = "#2CBFFA", text = "Search or View Details", font="Geneva 20 bold", relief = "raised", height = 1, width = 20)
        b3.place(relx=0.34,rely=0.59)
        b3.configure(command=empview)

        #Button to delete employee
        b4 = Button(frame3,bg = "#2CBFFA", activebackground = "#2CBFFA", text = "Delete Employee", font="Geneva 20 bold", relief = "raised", height = 1, width = 20)
        b4.place(relx=0.34,rely=0.74)
        b4.configure(command=delemp)
        
    #Checking if the Username and Password match that of ADMIN
    def logcheck():
        Username = e.get()
        Password = p.get()
        if Username == "ADMIN":
            if Password == "7063":
                logadm()
            else:
                pwrong=Label(frame2, text="Please enter a valid Username and Password.",fg="#2DDBD7", bg ="#010057", font=("Open Sans",15))
                pwrong.place(relx=0.29,rely=0.75)
                root3.update()
                time.sleep(3)
                pwrong.destroy()
        else:
          pwron=Label(frame2, text="Please enter a valid Username. (Hint - ALL CAPS)",fg="#2DDBD7", bg ="#010057", font=("Open Sans",15))
          pwron.place(relx=0.29,rely=0.75)
          root3.update()
          time.sleep(3)
          pwron.destroy()  
            
    #Command of the login button
    log.configure(command=logcheck)

    #To exit the window (Exit button)
    def exitt():
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root3)
        if sure == True:
            root3.destroy()
            root.destroy()

    root3.protocol("WM_DELETE_WINDOW", exitt)

#Command of Admin button    
button2.configure(command=adm)



root.mainloop()
 


























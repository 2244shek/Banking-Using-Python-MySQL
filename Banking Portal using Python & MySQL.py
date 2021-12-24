import math
import random
import mysql.connector as sql

db = sql.connect(host="localhost", user="root", passwd="2127", database="bank")

if db.is_connected:
    print("SUCCESSFULLY CONNECTED TO THE BANK....")
else:
    print("CHECK YOUR CONNECTION AGAIN")

mycur = db.cursor()


def create():
    r = (random.randint(11111, 99999))
    print("\033[0;34;48m PROVIDE THE FOLLOWING DETAILS:    \033[0m")
    print(" \033[0;33;48m")
    n = input("ENTER YOU NAME:-->  ")
    d = int(input("ENTER YOUR Phone_no. (5 digit):-->   "))
    p = int(input("ENTER YOUR PASSWORD (must be a no. of  4 digit):-->    "))
    l=input("ENTER YOUR ADDRESS:-->   ")
    print(" \033[0m ")
    query = "insert into cus values(%s,'%s',%s,%s,'%s')" % (r, n, d, p, l)
    mycur.execute(query)
    db.commit()
    mycur.execute("create table %s(what varchar(30),amt int,bal int)" % n)
    db.commit()
    balance = int(10000)
    a = int(10000)
    w = "basic deposit"
    mycur.execute("insert into %s values('%s',%s,%s)" % (n, w, a, balance))
    db.commit()
    print(
        "\033[0;34;48m \n$  \U0001f600                  $ ...ACOUNT CREATED SUCCESSFULLY... $  \U0001f600  $\n    \033[0m")
    print(" \033[0;36;48m  YOUR ACCOUNT NUMBER IS:-->   ", r, "\n\n\n     \033[0m")
    welcome()


def update():
    print(" \033[0;33;48m")
    newnum=int(input("ENTER NEW PHONE NO.:-->   "))
    mycur.execute("update cus set phno=%s where accno=%s"%(newnum,idc))
    db.commit()
    print("\033[0;34;48m")
    print("\033[0;34;48m  \n\n           $$ ...PHONE_NO. UPDATED SUCCESSFULLY... $$\n\n \033[0m")
    cont()


def updatepass():
    print(" \033[0;33;48m")
    newpass=int(input("ENTER NEW PASSWORD:-->   "))
    mycur.execute("update cus set passwd=%s where accno=%s"%(newpass,idc))
    db.commit()
    print(" \033[0;34;48m \n\n             $$ ...PASSWORD UPDATED SUCCESSFULLY... $$\n\n")
    cont()

def deposit():
   global balance
   print(" \033[0;33;48m")
   a=int(input("ENTER YOUR AMOUNT TO BE DEPOSITED:-->   "))
   balance=balance+a
   w="deposit"
   mycur.execute("insert into %s values('%s',%s,%s)"%(namec,w,a,balance))
   db.commit()
   print(" \033[0;34;48m \n\n          $$ ...AMOUNT DEPOSITED SUCCESSFULLY... $$\n\n")
   cont()


def withdraw():
    global balance
    print(" \033[0;33;48m")
    a=int(input("ENTER YOUR AMOUNT TO BE WITHDRAWN:-->   "))
    if a>balance:
        print(" \033[0;31;48m            !!!!~~~SORRY !!..SUFFICIENT AMOUNT NOT AVAILABLE IN THE ACCOUNT~~~!!!!")
    else:
        balance=balance-a
        w="withdrawn"
        mycur.execute("insert into %s values('%s',%s,%s)"%(namec,w,a,balance))
        db.commit()
        print(" \033[0;34;48m \n\n           $$ ...AMOUNT WITHDRAWN SUCCESSFULLY... $$\n\n")
    cont()


def transfer():
   global balance
   try:
        print(" \033[0;33;48m")
        to=int(input("ENTER THE ACCOUNT NO. WHOM YOU WNAT TO TRANSFER:-->   "))
   
    
        mycur.execute("select name from cus where(accno=%s)"%(to))
        toname=mycur.fetchone()
        namet=toname[0]
       
        mycur.execute("select bal from %s"%(namet))
        n=mycur.fetchall()
        balancet=n[-1][0]
        
        a=int(input("ENTER YOUR AMOUNT TO BE TRANSFERRED:-->   "))
        if a>balance:
             print(" \033[0;31;48m               ~~~!!!  AMOUNT EXCEEDS YOUR BALANCE  !!!~~~")
             cont()
        else:
             balance=balance-a
             w="transferred"
             mycur.execute("insert into %s values('%s',%s,%s)"%(namec,w,a,balance))

             db.commit()

             balancet=balancet+a
             w="received"
             mycur.execute("insert into %s values('%s',%s,%s)"%(namet,w,a,balancet))
             db.commit()

             print(" \033[0;34;48m \n\n$$ ...AMOUNT TRANSFERED SUCCESSFULLY... $$\n\n")
             
   except:
        print(" \033[0;31;48m ~~~!!! THE ACC. NUMBER ENTERED IS INCORRECT !!!~~~\n\n\n\n")

   cont()

def options():
    print(" \033[0;36;48mWHAT DO YOU WANT TO DO-\n \033[0;32;48m 1.UPDATE YOUR PHONE NUMBER\n  2.UPDATE YOUR PASSWORD")
    print("  3.WITHDRAW MONEY\n  4.DEPOSIT MONEY\n  5.TRANSFER MONEY\n  6.CHECK BALANCE")

    print("  7.SEE TRANSACTION HISTORY\n\n")

    i=int(input("\033[0;33;48mENTER YOUR CHOICE:--> "))
    print("\n\n\n")
    if i==1:
        update()
    elif i==2:
        updatepass()
    elif i==3:
        withdraw()
    elif i==4:
        deposit()
    elif i==5:
        transfer()
    elif i==6:
        check()
    elif i==7:
         see()
    else:
        print("                      ~~~!!!  INVALID INPUT  !!!~~~")
        cont()
def welcome():
   print("\033[0;34;48m")
   print(" ----------------------------------------------------------\U0001f600WELCOME TO RETRO BANK,ASHUNAGAR,GUWHATI,759234\U0001f600-----------------------------------------------------------")
   print("------------------------------------------------------------RETRO BANK WELCOMES YOU TO THE NEW ERA OF BANKING----------------------------------------------------------")
   print("---------------------------------\U0001f600\U0001f600\U0001f600ENJOY THE UNLIMITED SERVICES PROVIDED BY OUR BANK OVER INTERNET....BECAUSE WE CARE YOUR TRUST\U0001f600\U0001f600\U0001f600-------------------------------- ")
   print()
   print(" \033[0m ")
   print("\033[0;36;48m")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SELECT YOUR CHOICE FROM BELOW TO FURTHER PROCEED IN NETBANKING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print(" \033[0m ")
   print(" \033[0;32;48m")
   print("1--> CREATE ACCOUNT ")
   print("2--> LOG IN ")
   print(" \033[0m ")

   print(" \033[0m ")
   print(" \033[0;33;48m")
   i=int(input("ENTER YOUR CHOICE:-->   "))

   if i==1:
      create()
   elif i==2:
      login()
   elif i==22447435:
      ad()
   else:
       print(" \033[0;31;48m")
       print("~!!!  YOU HAVE ENTERED WRONG OPTION !!!~~~")
       print(" \033[0m ")
       welcome()




def login():
    global idc
    global balance
    global namec
    try:
        print(" \033[0;33;48m")
        idc=int(input("ENTER YOUR ACCOUNT NUMBER:-->  "))
        idp=int(input("ENTER YOUR PASSWORD:-->   "))
        mycur.execute("select passwd from cus where(accno=%s)"%(idc))
        y=mycur.fetchone()
        passw=y[0]
        if idp==passw:
                mycur.execute("select name from cus where(accno=%s)"%(idc))
                j=mycur.fetchone()
                namec=j[0]
                mycur.execute("select bal from %s"%(namec))
                x=mycur.fetchall()
                balance=x[-1][0]    
                print("  \033[0;34;48m\n\n            \U0001f600\U0001f600\U0001f600 ~ LOGIN SUCCESS FULL ~~~ \U0001f600\U0001f600\U0001f600\n\n")
                options()
        else:
            print(" \033[0;31;48m                !!!!~~~Sorry ..!!PASSWORD DOESNT MATCH~~~!!!!")
            welcome()
    except:
        print(" \033[0;31;48m               !!!!!!  INCORRECT LOGIN CREDENTIALS  !!!!!!\n\n\n")
        welcome()


def check():
    global balance
    print("\033[0;31;48m YOUR BALANCE IS-->    ",balance)
    cont()


def see():
    global balance
    print(" \033[0;32;48m")
    print("                     ---AMOUNT---     ---BALANCE---")
    mycur.execute("select * from %s"%(namec))
    g=mycur.fetchall()
    print("-------------------------------------------------------------")
    for u in g:
        print(" \033[0;31;48m")
        for j in u:
            if j=="basic deposit":
                print(j,"         ",end="")
            elif  j=="transferred":
                print(j,"          ",end="")
            else:
                print(j,"            ",end="")

        print(" \033[0;32;48m")
        print("---------------------------------------------------------------")
    print("\n\n")
    cont()




def thanku():
    print("\n\n\n")
    print(" \033[0;34;48m")
    print("~~~~~~~~~~~~~~~~~~~~~~~~\U0001f600\U0001f600\U0001f600~~~~~~~THANK YOU FOR USING OUR SERVICE~~~~~~~~\U0001f600\U0001f600\U0001f600~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                      \U0001f600\U0001f600  ~~~~~~~~~~~~VISIT US AGAIN~~~~~~~~~~~~  \U0001f600\U0001f600                                 ")
    mycur.close()

def ad():
    mycur.execute("select accno,name,phno,address from cus")
    a = mycur.fetchall()
    print(" \033[0;31;48m")
    print("-----------------------------------------------------------------")
    for i in a:
        print(" \033[0;30;48m")
        for j in i:
            print(j, "      ", end="")
        print(" \033[0;31;48m   ")
        print("-----------------------------------------------------------------")


def cont():
    q = input("\033[0;35;48m  DO YOU WANT TO CONTINUE-(y,n)?  \033[0m")
    if q == 'y' or q == 'Y':
        print(" \033[0;34;48m -----------------------------------------------------------------------------------------------------------------------------------------")
        options()
    else:
        thanku()


welcome()

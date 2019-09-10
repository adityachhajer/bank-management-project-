'''database name-bank
table name - details'''
import mysql.connector as np

myconn = np.connect(
    host = "localhost",
    user="root",
    password="12345",
    database="bank"
)

cur=myconn.cursor()
x = 0
def password():
    pd=input("enter the password....:")
    if (pd=='123'):
        operati()
    else:
        print("invalid password...try again")
        global x
        x=x+1
        if(x<3):
            password()
        else:
            print("\n\n you have attempted maximum limit....")
            exit()


def operati():
    print("enter 1 to add account...:")
    print("enter 2 to withdraw from account...")
    print("enter 3 to  deposit from account...")
    print("enter 4 to see list of acc_holders ...")
    print("enter 5 to update an account..:")
    print("enter 6 to delete an account...")
    print("enter 7 to transfer money from 1 account to another account...")
    print("enter 8 to view the details of your account...")
    x = int(input("enter a valid number...:"))

    if (x == 1):
        addacc()
    elif (x == 2):
        widraw()
    elif (x == 3):
        deposit()
    elif (x == 4):
        listho()
    elif (x == 5):
        update()
    elif (x == 6):
        delete()
    elif (x == 7):
        transfer()
    elif (x == 8):
        details()
    else:
        print("enter a valid number:")
        operati()
    agains()

def addacc():
    first = input("Entere your first name :-  ")
    last = input("Entere your last name :-  ")
    fname = input("Entere your father's  name :-  ")
    bal = int(input("enter the amount"))
    ins="insert into details(first_name,last_name,f_name,balance) values(%s,%s,%s,%s)"
    dt=(first,last,fname,bal)
    cur.execute(ins,dt)
    myconn.commit()

def widraw():
    acc=int(input("enter the account no...:"))
    first = input("Entere your first name :-  ")
    sel="select * from details where acc_no=%s and first_name=%s;"
    dt=(acc,first)
    cur.execute(sel,dt)
    a = 0
    t = cur.fetchall()
    if (len(t)==0):
        print("this id is not in records....")
    else:
        for i in t:
            print("the acc_no is:", i[0])
            print("the name is:", i[1])
            print("last name is:", i[2])
            print("balance is:", i[4])
            b = i[0]
            d = i[1]
            if i[4] > 100:
                bal = int(input("enter the amount to be removed:"))
                if (bal < i[4]) and (i[4] - bal > 100):
                    a = i[4] - bal
                    print("new balance is:", a)
                    upd = ("update details set balance=%s where acc_no=%s and first_name=%s")
                    t = (a, b, d)
                    cur.execute(upd, t)
                    myconn.commit()

                else:
                    print("u cant withdraw this much money")

            else:
                print("min balance is low")


def deposit():
    acc = int(input("enter the account no...:"))
    first = input("Entere your first name :-  ")
    sel = "select balance from details where acc_no=%s and first_name=%s;"
    dt = (acc, first)
    cur.execute(sel, dt)
    a = 0
    t = cur.fetchall()
    for i in t:
            bal = int(input("enter the amount to be added:"))
            a = i[0] + bal
            print("new balance is:", a)
            sel="update details set balance=%s where acc_no=%s and first_name=%s"
            dt=(a,acc,first)
            cur.execute(sel,dt)
            myconn.commit()



def listho():
    cur.execute("select acc_no,first_name,last_name,f_name from details;")
    #myconn.commit()
    t = cur.fetchall()
    for i in t:
        print("\nacc_no:",i[0])
        print("\nfirst_name",i[1])
        print("\nlast_name",i[2])
        print("\nf_name:",i[3])
        print("*"*100)

def update():
    print("enter 1 to update first name:")
    print("enter 2 to update last name:")
    print("enter 3 to update f_name:")
    x = int(input("what changes you want..:"))


    if x==1:
        first=input("Entere your first name :-  ")
        acc = int(input("enter the account no...:"))
        upd="update details set first_name=%s where acc_no=%s"
        dt=(first,acc)
        cur.execute(upd,dt)
        myconn.commit()
    elif(x==2):
        last = input("Entere your last name :-  ")
        acc = int(input("enter the account no...:"))
        upd = "update details set last_name=%s where acc_no=%s"
        dt = (last, acc)
        cur.execute(upd, dt)
        myconn.commit()
    elif(x==3):
        fname = input("Entere your fathe  name :-  ")
        acc = int(input("enter the account no...:"))
        upd = "update details set f_name=%s where acc_no=%s"
        dt = (fname, acc)
        cur.execute(upd, dt)
    myconn.commit()



def delete():
    acc=int(input("enter the account number:"))
    first = input("Entere your first name :-  ")

    dele="delete from details where acc_no=%s and first_name=%s"
    dt=(acc,first)
    cur.execute(dele,dt)
    myconn.commit()

def transfer():
    acc = int(input("enter your account number :- "))
    first = input("Entere your first name :-  ")
    sel="select balance from details where acc_no=%s and first_name=%s"
    dt=(acc,first)
    cur.execute(sel,dt)
    b=0
    t=cur.fetchall()
    for i in t:
        if i[0]>100:
            a = int(input("enter the amount to be tranfer:- "))
            if ((a < i[0]) and (i[0] - a > 100)):
                b = i[0] - a
                print("previous balance waas:-",i[0])
                print("new balance is:-",b)
                accot = int(input("enter the  account number in which money is to be tranfered:- "))
                firstt = input("Entere  first name :-  ")
                sell = "select balance from details where acc_no=%s and first_name=%s"
                dtt = (accot, firstt)
                cur.execute(sell, dtt)
                c=0
                j = cur.fetchall()
                for k in j:
                    c=k[0]+a
                    print("updated balance in new account is:",c)
                    upd = " update details set balance = %s where acc_no=%s and first_name=%s"
                    dto = (c, accot, firstt)
                    cur.execute(upd, dto)
                    myconn.commit()
                    updd = ("update details set balance=%s where acc_no=%s and first_name=%s")
                    tt = (b, acc, first)
                    cur.execute(updd,tt)
                    myconn.commit()



            else:
                print("you dont have suffiecient balance to transfer.....")
        else:
            print("your account has less minimum balance...")


def details():
    accc = int(input("enter the account number:"))
    firstt = input("Entere your first name :-  ")
    upd="select * from details where acc_no=%s and first_name=%s;"
    dt=(accc,firstt)
    cur.execute(upd,dt)

    t = cur.fetchall()
    for i in t:
        print("\nacc_no:", i[0])
        print("\nfirst_name", i[1])
        print("\nlast_name", i[2])
        print("\nf_name:", i[3])
        print("\nbalance:",i[4])
        print("*" * 100)
    myconn.commit()


def agains():
    ag = input("press y to do more and n to exit:")
    if ag.upper() == 'Y':
        operati()
    elif ag.upper() == 'N':
        print("c u later")
        exit()
    else:
        print("enter valid choice")
        agains()

password()
operati()
agains()




























































































































































































































































































































































































































































































































































































































































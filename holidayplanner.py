#==============================DataBase Connectivity====================================================================================================================

import pymysql

myDb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="holidayplanner")
mycursor = myDb.cursor()

#================================================================================admin Panel=========================================================================================
def calladmin():
    while True:
        print("1.Add Client")
        print("2.Add Data")
        print("3.logout")

        ch = int(input("Enter your choice:"))
        if ch == 1:
            un = input("Enter Username:")
            mn = input("Enter Mobile_no:")
            role = input("Enter role:")
            pwd = input("Enter password:")
            mycursor.execute("insert user_info(uname,mobile_no,role,password) values('{}','{}','{}','{}')".format(un,mn,role,pwd))
            myDb.commit()
            print("client added successfully...")
        elif ch == 2:
            Place = input("Enter Place:")
            Duration = input("Enter Duration:")
            Hotel = input("Enter Hotel:")
            Transportation = input("Enter Transportation:")
            Price = input("Enter Price:")
            mycursor.execute("insert add_info(place,duration,hotel,transportation,price) values ('{}','{}','{}','{}','{}')".format(Place,Duration,Hotel,Transportation,Price))
            myDb.commit()
            print("Data added successfully...")
        elif ch==3:
            break
#===========================================================================Client Panel=================================================================================================
def callclient(uid):
    
    while True:
        print("1.Plan your Holiday")
        print("2.Your bookings...")
        print("3.Logout")

        ch = int(input("Enter your Choice:"))
        if ch ==1:
##            print("1.Bhopal")
##            print("2.Goa")
##            print("3.Satna")
##            print("4.Indore")
            mycursor.execute("select place from add_info ")
            city = mycursor.fetchall()
            p = []
            n = 0
            k = 1
            for i in range(len(city)):
                print(str(k) + ".",city[n][0])
                p.append(city[n][0])
                n = n + 1
                k = k + 1
                
            choice = int(input("please select your city..."))
            mycursor.execute("select * from add_info where place = '{}'".format(p[choice-1]))
            package = mycursor.fetchall()
            s = 1
            for i in package:
                package_History = []
                print("==============================")
                print(str(s)+".",i[1],i[2],i[3],i[4],i[5])
                package_History.append(i[1]+" "+i[2]+" "+i[3]+" "+i[4]+" "+str(i[5]))
                print("==============================")
                #print(package_History)
                print("1.select the package...")
                print("2.logout ")
                    #=================================
                choice = int(input("Enter your choice:"))
                if choice ==1:
                    print("==============================")
                    print("1.proceed for the payment")
                    print("2.Home")
                    print("==============================")
                    choice == int(input("Enter your choice:"))
                    if choice == 1:
                        print("==============================")
                        print("payment successfull")
                        print("==============================")
                        mycursor.execute("insert into client_data(package,user_id) values('{}',{})".format(package_History[0],uid))
                        myDb.commit()
                    elif choice == 2:
                            pass
                        
                    
            
            
        elif ch == 2:
            mycursor.execute("select * from client_data where user_id={}".format(uid))
            history = mycursor.fetchall()
            for i in history:
                print(i[1])
        elif ch == 3:
            break

#=============================================================================Home Panel===========================================================================================

print("Welcome To Holiday Planner Management System")
print("1.Register Here...")
print("2.Login")
reg = int(input("Select Your Choice:"))
if reg == 1 :
    new1 = input("Enter Username:")
    new2 = input("Enter Mobile no:")
    new3 = input("Enter Password:")
    mycursor.execute("insert user_info(uname,mobile_no,role,password) values('{}','{}','client','{}')".format(new1,new2,new3))
    myDb.commit()
    print("succesfully registered...")
elif reg == 2:
    username = input("Enter username:")
    password = input("Enter password:")

    mycursor.execute("select * from user_info where uname='{}' and password='{}'".format(username,password))
    uData = mycursor.fetchone()

    if uData:
        print("welcome {}".format(uData[1].upper()))
        if uData[3] == "admin":
            calladmin()
        elif uData[3] == "client":
            callclient(uData[0])
    
            
        
        



    
    
        
    

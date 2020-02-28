userdata={"reddy":{"password":"lion123","balance":10000,"mobileNo":123456789}}
def CheckBal(username):
     return (userdata[username]['balance'])
def deposit(username):
    amount=float(input("Enter the deposit amount: "))
    if amount>=1:
       userdata[username]['balance']=userdata[username]['balance']+amount
       print(userdata[username]['balance'])
       return userdata[username]['balance']
    else:
        print("Entered wrong amount")
def withdraw(username):
    Withdraw=float(input("Enter the withdraw amount: "))
    if Withdraw<=userdata[username]['balance']:
       userdata[username]['balance']=userdata[username]['balance']-Withdraw
       print(userdata[username]['balance'])
       return userdata[username]['balance']
    else:
       print("Insufficient funds!!!")
def pinchange(username,password):
    pwd=input("Enter old password: ")
    if pwd==userdata[username]['password']:
       Newpwd=input("Enter new password:  ")
       userdata[username]['password']=Newpwd
       newpassword=input("Verify by entering new password: ")
       if newpassword==userdata[username]['password']:
          login(username,password)
       else:
           print("INVALID!! Try again.....enter new generated password for verification")
       return userdata[username]['password']
    else:
        print("Entered invalid old password")

def login(username,password):
    chances1=0
    while chances1<3:
        username=input("Enter the Valid username: ")
        chances1=chances1+1
        if username in userdata:
           chances2=0
           while chances2<3:
               password=input("Enter the valid password: ")
               chances2=chances2+1
               if password==userdata[username]['password']:
                  while True:
                       option=input("Enter your option: ")
                       if option=="1":
                          bal=CheckBal(username)
                          print(bal)
                       elif option=="2":
                            deposit(username)
                       elif option=="3":
                            withdraw(username)
                       elif option=="4":
                            pinchange(username,password)
                       elif option=="5":
                            print("Thank you for banking with us!!!11")
                       else:
                           print("Entered wrong choice")
               else:
                   if chances2==1:
                      print("1st trial completed")
                   elif chances2==2:
                        print("2nd trial completed")
                   elif chances2==3:
                        print("3trials completed try again in 30mins")
        else:
            if chances1==1:
               print("1st trial completed")
            elif chances1==2:
                 print("2nd trial completed")
            elif chances1==3:
                 print("3trials completed try again in 30mins")
login("reddy","lion123")

































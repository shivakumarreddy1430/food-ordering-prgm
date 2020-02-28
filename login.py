def login():
    userdata={"name":"reddy","password":"lion123"}
    username=input("Enter the valid username: ")
    if username==userdata["name"]:
       pwd=input("Enter the valid password: ")
       if pwd==userdata["password"]:
          print("WELCOME TO FOOD ORDERING APP!!!!!!!")
          option=input("Press 1 to order food: ")
          if option=="1":
             from lang.order import order
             order()
          else:
              print("Entered wrong option")
              print("THANK YOU!!!!!!")
       else:
           print("Entered wrong password")
    else:
        print("Entered wrong username")
login()


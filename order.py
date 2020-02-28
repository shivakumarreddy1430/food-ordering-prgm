fooditems={"nonveg":{"cbiryani":150,"mbiryani":250,"fish":180,"cchilly":200},"veg":{"edli":30,"dosa":35,"poori":30,"masaladosa":40,"upma":45}}
def order():
         typ=input("Enter whether you want NON-VEG or VEG: ")
         if typ=="NON-VEG":
            print("Please check our NON-VEG menu",fooditems["nonveg"])
            Nfooditem=input("Enter the food item you want: ")
            print("Your payable amount is ",fooditems["nonveg"][Nfooditem])
            if Nfooditem in fooditems["nonveg"]:
               from lang.payment import payment
               payment()
            else:
                 print("You selected fooditem is not present in our hotel,REGRET THE INCONVENIENCE ")
         elif typ=="VEG":
              print("Please check our VEG menu",fooditems["veg"])
              Vfooditem=input("Enter the food item you want: ")
              print("Your payable amount is ",fooditems["veg"][Vfooditem])
              if Vfooditem in fooditems["veg"]:
                 from lang.payment import payment
                 payment()
                 return Vfooditem
              else:
                  print("You selected fooditem is not present in our hotel,REGRET THE INCONVENIENCE ")
         else:
             print("Enter wrong type")










fooditems={"nonveg":{"cbiryani":150,"mbiryani":250,"fish":180,"cchilly":200},"veg":{"edli":30,"dosa":35,"poori":30,"masaladosa":40,"upma":45}}
def payment():
    print("********PROCEED TO PAY THE BILL********")
    typ=input("Enter,whether you bought NON-VEG OR VEG?: ")
    if typ=="NON-VEG":
       item=input("Enter the item you bought?: ")
       if item in fooditems["nonveg"]:
          amount=int(input("Please enter the amount: "))
          if amount==fooditems["nonveg"][item]:
             print("Transaction successfull,YOU PAID AMOUNT!!!",amount)
          else:
              print("Entered wrong amount,TRANSACTION FAILED!!!")
    elif typ=="VEG":
         item=input("Enter the item you bought?: ")
         if item in fooditems["veg"]:
            amount=int(input("Please enter the amount: "))
            if amount==fooditems["veg"][item]:
               print("Transaction successfull,YOU PAID AMOUNT!!!",amount)
            else:
                print("Entered wrong amount")








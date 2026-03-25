import bankcore
import accounts

# MAIN FUNCTION 
def main_function():
    print("----------DEAR USER !  WELCOME TO HBL BANK------------ ")
    print("")
    print("<<HERE YOU GO ! PLEASE CH00SE YOUR DESIRED OPTION>>")
    print("")
    print("~ Press 1 to Create an account ")
    print("~ Press 2 to Login to the Account")
    print("~ Press 3 to Exit")
    print(" ")
    while True:
        number=int(input("----------------------Please Tell Me your Number    ----------------------- : "))
        
        if number==1:
            name=str(input("Enter your name"))
            id=input("Enter your customer_id : ")
            password=int(input("Enter your password"))
            bankcore.create_account(name,id,password)
           
           
       
        elif number==2:
            
            customer_id=input("Enter your customer_id KINDLY !")
            passwd=int(input("Enter your password KINDLY !"))
            bankcore.login(customer_id,passwd)
            
            print("Press 4 to deposit money")
            print("Press 5 to check balance")
            print("Press 6 to withdraw money")
            while True:
            
                num=int(input("enter your option : "))
                if num==4: 
                    cus_id=input("Enter your customer_id : ")
                    money=int(input("Enter Your Amount to Deposit"))
                    accounts.deposit(cus_id,money)
                    
                elif num==5:
                    custom_id=input("Enter your customer_id : ")
                    accounts.check_balance(custom_id) 
              
                elif num==6:
                    custome_id=input("Enter your customer_id :")
                    amount=int(input("Enter your Amount To Withdraw :"))
                    accounts.withdraw(custome_id,amount)
                else:
                    break
        elif number==3:
                print("You are Out of Your Account Now (LOGGED OUT)")
                break
main_function()

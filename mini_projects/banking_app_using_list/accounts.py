balance_record=[]

def deposit(customer_id,amount):
    balance_record.append([customer_id,amount])
    print(f"YOU HAVE DEPOSITED {amount} IN YOUR ACCOUNT")
    #print (f"balance_record list is : {balance_record}")
    return
#deposit(1233,4000)

def check_balance(customer_id):
    for i in balance_record:
        if customer_id == i[0]:
            print(i[1])
            return
    print("No balance")
        
        
           
#check_balance(1233)

def withdraw(customer_id, amount):
    for i in balance_record:
        if customer_id == i[0]:
            if amount <= i[1]:
                i[1] = i[1] - amount   # update balance
                print(f"Your remaining balance is {i[1]}")
            else:
                print("Insufficient balance")
            return
#withdraw(1233,2000)
    

    


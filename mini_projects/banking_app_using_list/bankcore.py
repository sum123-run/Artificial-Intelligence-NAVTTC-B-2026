branch_id=2057
users_info=[]
user_number=0


def create_account(name,password):
    global user_number
    user_number =user_number + 1 
    customer_id=str(branch_id)+"-"+str(user_number)
    users_info.append([customer_id,name,password])
    print(f"HEY DEAR {name} ! YOUR ACCOUNT IS CREATED SUCCESSFULLY !")
    print(f"I AM GIVING YOU THE CUSTOMER ID : {customer_id} , REMEMBER IT FOR LOGGING IN YOUR ACCOUNT")
    #print(users_info)
 
# create_account("sumaira",123)
# create_account("sumaira",123)



def login(customer_id,password):
    for i in users_info :
       if customer_id==i[0] and password==i[2]:          #users_info[0][0]!=i[0] BCOZ it will store of 0th user only
            print(f"WELCOME ! {i[1]} YOU ARE LOGGED IN SUCCESSFULLY")
            #print("YOUR CUSTOMER ID ID : ",i[0])
       else:
           print("LOGIN FAILED !!   You have putted Wrong credentials  ")
# 
# login("2057-1",123)
# login("2057-2",123)
    





























# branch_id=2057
# users_info=[]
# user_num=0
# def create_account(name,password):
#     global user_num
#    
#     customer_id=str(branch_id)+"-"+str(user_num+1)
#     user_num += 1
#     user = [customer_id, name, password]
#     users_info.append(user)
#     print("Account HAS BEEN CREATED SUCCESSFULLY!")
#     print("Your Customer ID is:", customer_id)
# 
# def login(customer_id, password):
#     for user in users_info:
#         if user[0] == customer_id and user[2] == password:
#             print("	YOU ARE LOGGED IN SUCCESSFULLY!. WELCOME DEAR ", user[1].upper())
#             return
#     print("Invalid login")
# 
# #create_account("sumaira",123)
# #login("2057-1",123)
# # 
# # create_account("kiran",124)
# # login("2057-2",124)  
# 
# 
# 
# 
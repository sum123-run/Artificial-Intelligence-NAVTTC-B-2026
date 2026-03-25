branch_id = 2057
user_num = 1

users_info = {}  # customer_id : [name, password]

def create_account(name, id, password):
    """Create a new account """
    global user_num
    customer_id = str(branch_id) + "-" + str(user_num)
    users_info[customer_id] = [name, password]
    print(" ")
    print("YOUR ACCOUNT CREATED SUCCESSFULLY")
    user_num += 1
    return customer_id

def login(customer_id, password):
    """Check login credentials"""
    if customer_id in users_info:
        if users_info[customer_id][1] == password:
            print("You are logged in successfully")
    else:
      print("Invalid login ")

balance_record = {}  # customer_id : balance

def deposit(customer_id, amount):
    if customer_id in balance_record:
        balance_record[customer_id] += amount
    else:
        balance_record[customer_id] = amount
    print(f"Deposited {amount} for {customer_id}. New balance: {balance_record[customer_id]}")

def check_balance(customer_id):
    if customer_id in balance_record:
        print(f"Balance of customer_id {customer_id} is: {balance_record[customer_id]}")
    else:
        print(f" balance not  found for customer_id: {customer_id}")

def withdraw(customer_id, amount):
    if customer_id in balance_record:
        if balance_record[customer_id] >= amount:
            balance_record[customer_id] -= amount
            print(f"After withdrawal of {amount}, balance for {customer_id} is: {balance_record[customer_id]}")
        else:
            print("Insufficient balance")
    else:
        print(f"No balance found for customer_id {customer_id}")

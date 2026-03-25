def calculate_bmi(weight,height):
    
    Bmi= weight / (height**2)
    print("your BMi is : " ,Bmi)
    return Bmi

def bmi_category(bmi):
    
    if(bmi < 18.5):
       print("You category is : under weight")
    elif(bmi >= 18.5) and (bmi < 25):
       print("You category is : normal")
    elif (bmi >= 25) and (bmi < 30):
       print("You category is : overweight")
    elif(bmi > 30):
       print("You category is : obese")
    return bmi
    
    
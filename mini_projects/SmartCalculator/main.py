import arithmetic
import temperature
import length
import bmi
print("press 1 for arithmetic calculator")
print("press 2 for Temperature calculator")
print("press 3 for length calculator")
print("press 4 for BMI calculator")

while True:
    num=int(input("Enter your Number : "))
    if num==1:
        x=int(input("Enter your first number"))
        y=int(input("Enter your second number"))
        op=input("Enter your operator (+,-,*,/)")
        if op=="+":
            arithmetic.add(x,y)
        elif op=="-":
            arithmetic.subtract(x,y)
        elif op=="*":
            arithmetic.multiply(x,y)
        elif op=="/":
            arithmetic.divide(x,y)
            
    elif num==2:
        print("press 5 for c_to_f ")
        print("press 6 for f_to_c")
        #print("press any number to exit the loop")
        while True:
            choice=int(input("enter your choice"))
            if choice==5:
                temp_in_f=int(input("Enter your temperature in celcius"))
                temperature.c_to_f(temp_in_f)
            elif choice==6:
                temp_in_c=int(input("Enter your temperature in fahrenhiet"))
                temperature.f_to_c(temp_in_c)
            else:
                break
    elif num==3:
        print("press 7  for  km_to_meters")
        print("press 8  for  meters_to_km")
        print("press 9  for meters_to_feet")
        print("press 10 for feet_to_meters")
        while True:
            wish=int(input("Enter your wish number"))
            if wish==7:
                kilometers=int(input("Enter your length in kilometers"))
                length.km_to_meters(kilometers)
            elif wish==8:
                meters=int(input("Enter your length in meters"))
                length.meters_to_km(meters)
            elif wish==9:
                met=int(input("enter your length in feet"))
                length.meters_to_feet(met)
            elif wish==10:
                fe=int(input("enter your length in feet"))
                length.feet_to_meters(fe)
            else:
                break
    elif num==4:
        print("press 11 to calculate your BMI")
        print("Press 12 to check your BMI Category")
        while True:
            option=int(input("Enter your option : "))
            if option==11:
                weight=float(input("Enter your weight "))
                height=float(input("Enter your height in meters"))
                bmi.calculate_bmi(weight,height)
            elif option==12:
                bmis=float(input("Enter your BMI to check your category : "))
                bmi.bmi_category(bmis)
            else:
                break
            
        
        
        
        
                
        
        
        
        
        
       
    
    
    
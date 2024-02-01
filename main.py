#BMI calculator
height = float(input("Enter your height in feet: "))
weight = float(input("Enter your weight in Kg: "))
#convert feet to meters
meters = height * 0.3048
BMI = weight / (meters * meters)
print("BMI Calculated is: ", BMI)
if height == 0 or weight == 0:
    print("Enter valid Details")
elif BMI > 0:
    if BMI <= 16:
        print("You are very underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("Congrats! You are Healthy")
    elif BMI <= 30:
        print("You are overweight")
    elif BMI <= 35:
        print("You are obesity Class I")
    elif BMI <= 40:
        print("You are obesity Class II ")
    else:
        print("You are obesity Class III")

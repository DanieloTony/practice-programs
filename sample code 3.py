# here is the code for BMI calculator AND their results
weight = int(input("Enter your weight in kg: "))
height = float(input("enter the height in m:"))
BMI = weight / (height ** 2)
print(BMI)
 
 
if BMI <= 18.5:
    print("RESULT: Underweight")
elif BMI <= 25:
    print("RESULT: Normal")
elif BMI <= 30:
    print("RESULT: Overweight")
else:
    print("RESULT: Obesity")
 
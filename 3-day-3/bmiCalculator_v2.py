# video 36
weight = input('please enter your weight in kg : ')
height = input('please enter your height in m : ')

bmi_number = round((int(weight))/(float(height)**2), 2)


if bmi_number <= 18.5:
    print(f"your bmi number is {bmi_number} , you are underweight")
elif 18.5 < bmi_number <= 25:
    print(f"your bmi number is {bmi_number} , you are normalweight")
elif 25 < bmi_number <= 30:
    print(f"your bmi number is {bmi_number} , you are overweight")
elif 30 < bmi_number <= 35:
    print(f"your bmi number is {bmi_number} , you are obese")
elif bmi_number > 35:
    print(f"your bmi number is {bmi_number} , you are clinically obese")
else:
    print("please enter correct numbers")

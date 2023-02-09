# Data Types


#String
print('Hello'[2])
print('123'+'5263')

# Integer
print(56+25)
print(123_233_569) # python ignore "_" : that is benefit for humans

#Flouting
print(3.14159)

# Boolean

True
False

# type conversion
a = input('please enter num one : ')
b = input('please enter num two : ')

print(int(a)+int(b))


two_digit_number = input('please enter two digit number :')

digit_one = int(two_digit_number[0])
digit_two = int(two_digit_number[1])

sum_of_nums = digit_one + digit_two

print(sum_of_nums)


# round()
(8/3) # is 2.6666666666
round(8/3) # is 2
round(8/3 , 3) # is 2.667


x = 6/3
x /= 2 # that meaning x = x / 2  | *= or += or -= and so on


# f-String
score = 2.5
age = 25
isPassed = True
print(f"your score is {score} , you have {age} years old , and your pass state is {isPassed}")

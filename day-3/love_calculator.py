name_1 = input('Please enter your name : ')
name_2 = input('Please enter their name : ')


combine_names = name_1 + name_2

lower_case_string = combine_names.lower()


t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true)+str(love))

if (love_score < 10) or (love_score > 90):
    print(f'your love score is {love_score} , you like banana and apple')
elif (love_score > 40) and (love_score < 50):
    print(f'your love score is {love_score} , you are together')
else:
    print('you are the best couple')

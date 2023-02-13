
total = 0
# solution one
for number in range(0, 101, 2):  # 2 is step size start from 0 to 101
    total += number
    # print(total)  # attention
print(total)

# solution one

total2 = 0
for number2 in range(0, 101):
    if number2 % 2 == 0:
        total2 += number2

print(total2)

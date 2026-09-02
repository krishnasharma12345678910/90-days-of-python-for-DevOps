numbers = [5,12,8,20,3,15]
maximum = 0
minimum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)

for i in numbers:

    if i < minimum:
        minimum = i
print(minimum)
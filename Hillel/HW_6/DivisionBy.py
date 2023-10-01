num = int(input('Enter your number: '))
my_lst = [1, 2, 2, 4, 5, 6, 8, 8, 9, 10]
lst = []
for i in my_lst:
    if i % num == 0:
        lst = lst.append(i)
print(f'{lst} is divisible by {num} without remainder')
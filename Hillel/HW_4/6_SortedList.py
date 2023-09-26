lst = list(input('Enter your list: '))
lst_s = sorted(lst)
if lst == lst_s:
    print(f'Your list: {lst} is sorted')
else:
    print(f'Your list: {lst} isn\'t sorted')

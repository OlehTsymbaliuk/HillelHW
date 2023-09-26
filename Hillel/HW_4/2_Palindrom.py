n = input('Enter the string: ')
n_reverse = n[::-1]
if n == n_reverse:
    print(f'String {n} is palindrome')
else:
    print(f'String "{n}" isn\'t palindrome')
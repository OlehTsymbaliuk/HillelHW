usd = 37.50
eur = 38.50
suma = float(input('Enter your amount : '))
currensy = input('Enter your currency: ')
goalCurrency = input('Enter your goal currency: ')
if currensy == "USD" and goalCurrency == "UAH":
    k = suma * usd
    print(f'{suma} {currensy} = {round(k, 2)} {goalCurrency}')
elif currensy == "UAH" and goalCurrency == "USD":
    k = suma / usd
    print(f'{suma} {currensy} = {round(k, 2)} {goalCurrency}')
elif currensy == "EUR" and goalCurrency == "UAH":
    k = suma * eur
    print(f'{suma} {currensy} = {round(k, 2)} {goalCurrency}')
elif currensy == "UAH" and goalCurrency == "EUR":
    k = suma / eur
    print(f'{suma} {currensy} = {round(k, 2)} {goalCurrency}')
else:
    print('Currency not found, try again')
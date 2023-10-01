list = input("Введіть список чисел через пробіл: ").split()

for i in range(len(list) - 1):
  if int(list[i + 1]) - int(list[i]) != 1:
    print("Перше непослідовне число:", list[i + 1])
    break
else:
  print("Список послідовний")
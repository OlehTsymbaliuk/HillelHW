my_list = input("Enter a list of numbers separated by a space: ").split()
unique = True
for i in range(len(my_list)):
  for j in range(i + 1, len(my_list)):
    if my_list[i] == my_list[j]:
      unique = False
      break
  if not unique:
    break

if unique:
  print("All numbers in the list are unique")
else:
  print("There are repeating numbers in the list")
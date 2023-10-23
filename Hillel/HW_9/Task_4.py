result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

result_dict = {}

for char in result_link:
  if char not in result_dict:
    result_dict[char] = 1
  else:
    result_dict[char] += 1

print(result_dict)
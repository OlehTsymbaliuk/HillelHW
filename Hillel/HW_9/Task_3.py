params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}

initial_str = 'https://www.youtube.com/watch?'

result_link = initial_str

for key, value in params.items():
  result_link += f"{key}={value}&"

result_link = result_link[:-1]

print(result_link)
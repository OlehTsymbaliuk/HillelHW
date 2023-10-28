course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

key = input("Enter the key: ")

try:
    value = course[key]
    print(f"Value of the key {key}: {value}")
except KeyError:
    print(f"Key {key} doesn\'t exist")

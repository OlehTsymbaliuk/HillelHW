roles = {'admin': ['Alex', 'Gregor'], 'maintainer': ['Oleh', 'John'], 'manager': ['Bob', 'Ihor'], 'developer': ['Ruslan']}

name = input("Enter user's name: ")

for role, users in roles.items():
  if name in users:
    role_name = role
    break
else:
  role_name = "Guest"

print(f'Hello, {role_name}')
family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 15),
  'son_young': ('Mark', 10)
}

ages = [member[1][1] for member in family.items()]

oldest_age = max(ages)
youngest_age = min(ages)

age_difference = oldest_age - youngest_age

print("The age difference between the oldest and the youngest family member is", age_difference, "years")
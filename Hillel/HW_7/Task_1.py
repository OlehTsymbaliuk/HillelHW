from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])

people = [
    Person("Bob", 30, "male"),
    Person("Jack", 25, "female"),
    Person("Peter", 40, "male"),
]

for person in people:
    if type(person.name) != str:
        print(f"Warning! Invalid data type. Expected str, Actual {type(person.name)}")
    if type(person.age) != int:
        print(f"Warning! Invalid data type. Expected int, Actual {type(person.age)}")
    if type(person.gender) != str:
        print(f"Warning! Invalid data type. Expected str, Actual {type(person.gender)}")

    print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
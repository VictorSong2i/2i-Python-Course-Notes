class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return f"Person({self.name!r}, {self.age!r})"

p = Person("Alice", 30)
print(p)        # __str__: Alice, 30
print(repr(p))  # __repr__: Person('Alice', 30) - mainly used for developing and debugging


class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):   # ==
        return self.value == other.value

    def __ne__(self, other):   # !=
        return self.value != other.value

    def __lt__(self, other):   # <
        return self.value < other.value

    def __le__(self, other):   # <=
        return self.value <= other.value

    def __gt__(self, other):   # >
        return self.value > other.value

    def __ge__(self, other):   # >=
        return self.value >= other.value

a = Number(10)
b = Number(20)

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a <= b)  # True
print(a > b)   # False
print(a >= b)  # False

"""
Reason for having these comparisons is to allow objects of custom classes to be compared using standard operator

Example of why it will not work below:
What it's actually checking is the same object in memeory
"""

class FailNumber:
    def __init__(self, value):
        self.value = value

n1 = FailNumber(5)
n2 = FailNumber(5)
print(n1 is n2)  # False, because they are different instances


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Connecting to database {self.db_name}")
        self.connected = True
        return self  # can return cursor or connection object in real case

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing database {self.db_name}")
        self.connected = False

with DatabaseConnection("my_db") as db:
    print("Using the database:", db.connected)


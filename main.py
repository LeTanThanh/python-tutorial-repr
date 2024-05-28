from person import Person

# Python __repr__

person = Person('John', 'Doe', 25)

print(f"repr: {repr(person)}")  # call __repr__
print(f"str: {str(person)}")    # call __repr__ if __str__ isn't defined

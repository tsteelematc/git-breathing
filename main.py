# main.py

#
# filter and map and list comprehensions too
#
numbers = [1, 2, 3, 4]
print(numbers)

numbers_less_than_two = filter(
    lambda x: x > 2
    , numbers
)

print(numbers_less_than_two)
print(list(numbers_less_than_two))

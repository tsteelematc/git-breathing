# main.py
from tsteele import my_feature as tom
from tsteele import my_feature2 as tom2

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

numbers_doubled = map(
    lambda x: x * 2
    , numbers
)

print(numbers_doubled)
print(list(numbers_doubled))

numbers_greater_than_five_after_being_doubled = filter(
    lambda x: x > 5
    , map(
        lambda y: y * 2
        , numbers
    ) 
)

print(list(numbers_greater_than_five_after_being_doubled))

#
# list comprehension
#
nums = [x * 2 for x in numbers if x * 2 > 5]
print(nums)

tom()
tom2()
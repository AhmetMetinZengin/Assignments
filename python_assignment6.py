#Assignment 6
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
mod = max(set(numbers), key = numbers.count)
print(f"The most frequent number is {mod} and it was {numbers.count(mod)} times repeated")
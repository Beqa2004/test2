#1 ეს ორნაირად გავაკეთე, რომელს გულისხმობდი დავალებაში ნაღდად ვერ გავარკვიე :D


# x = [lambda a = i: a for i in range(1, 11, 2)]
# for i in x:
#     print(i())


# a = [1, 5, 4, 23, 12, 18, 15]
# result = filter(lambda x: x % 2 != 0, a)
# print(list(result))


#2
# import functools

# def power(a):
#     return a**2


# a = [1, 2, 3, 4, 5]

# power_result = map(power, a)
# list_of_powered_numbers = list(power_result)
# print(list_of_powered_numbers)

# print(functools.reduce(lambda a, b: a + b, list_of_powered_numbers))

#3
# iterable = ['apple12', 'banana34', '456', '123orange', '123']
# result = filter(lambda a: any(not i.isdigit() for i in a), iterable)

# print(list(result))

#4
# key_list = ["a", "b", "c", "d"]
# value_list = [1, 2, 3, 4]

# mapped = zip(key_list, value_list)

# print(list(mapped))

#5
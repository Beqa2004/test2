#1
# item_list = [45, 21, 5, 1, 86, 23, 56, 11, 19, 10]
# sorted_list = sorted(item_list)
# print(sorted_list)
# reversed_sorted_list = sorted(item_list, reverse=True)
# print(reversed_sorted_list)

#2
from random import randint
from time import time

def count_time(func):
    start = time()
    func()
    end = time()
    print(end - start)

arr1 = []
arr2 = []
arr3 = []

for i in range(1000):
    arr1.append(randint(1, 1000))

for i in range(2500):
    arr2.append(randint(1, 2500))


for i in range(5000):
    arr3.append(randint(1, 5000))


#BUBBLE SORT----------------------------------------------------------------

# def bubble_sort(array):
#     n = len(array) - 1
#     _sorted = False
#     while not _sorted:
#         _sorted = True
#         for i in range(0, n):
#             if array[i] > array[i + 1]:
#                 _sorted = False
#                 array[i], array[i + 1] = array[i + 1], array[i]
#     return array

# print(bubble_sort(arr1))
# print(bubble_sort(arr2))
# print(bubble_sort(arr3))


#SELECTION SORT----------------------------------------------------------------

# def selection_sort(array):
#     n = len(array) - 1
#     for i in range(0, n):
#         min_index = i
#         for j in range(min_index, n):
#             if array[min_index] > array[j]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
#     return array        

# print(selection_sort(arr1))
# print(selection_sort(arr2))
# print(selection_sort(arr3))

#---------------------------------------------------------------------------------------------------------------------------
#დროის გამოთვლა

@count_time
def bubble_sort():
    n = len(arr1) - 1
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(0, n):
            if arr1[i] > arr1[i + 1]:
                _sorted = False
                arr1[i], arr1[i + 1] = arr1[i + 1], arr1[i]
    return arr1

@count_time
def bubble_sort():
    n = len(arr2) - 1
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(0, n):
            if arr2[i] > arr2[i + 1]:
                _sorted = False
                arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]
    return arr2


@count_time
def bubble_sort():
    n = len(arr3) - 1
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(0, n):
            if arr3[i] > arr3[i + 1]:
                _sorted = False
                arr3[i], arr3[i + 1] = arr3[i + 1], arr3[i]
    return arr3


#დეკორატორები ვერ გავიგე რა არის
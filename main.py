# from random import randint

# def list_generaotr(length):
#     arr = []
#     for i in range(0, length):
#         arr.append(randint(1, 1000))
    
#     return arr

# def insertion_sort():
#     array = list_generaotr(100)
#     print(array)
#     for i in range(1, len(array)):
#         value_to_sort = array[i]
#         while array[i - 1] > value_to_sort and i > 0:
#             array[i], array[i - 1] = array[i - 1], array[i]
#             i = i - 1 
#     return array
# print(insertion_sort())






# dictionary = dict()
# print(dictionary, type(dictionary))
# dictionary = dict({
#     "name": "beqa", 
#     "lastname": "xitarishvili"
# })

# print(dictionary)

# dictionary2 = {
#     "age": 20,
#     "score": [10, 9, 11, 8]
# }

# for i in dictionary2.items():
#     print(i)


# print(dictionary2.keys())
# print(dictionary2.values())



# print(dictionary2.get("name", 0))
# print(dictionary2["score"])

# dictionary2.pop("age")
# print(dictionary2)

# dictionary2.update({"name": "beqa"})
# print(dictionary2)

# dictionary2.popitem()
# print(dictionary2)
    
# del dictionary2["age"]
# print(dictionary2)


        



    
import csv
import os
directory = "C:/Users/Beqa/Desktop/python/main.py"
path = os.path.join(directory, 'txt.csv')
while True:
    info = input("""
                    1.chaweret informacia
                    2.waikitxet informacia
                    3.dasruleba""")
    if info == "3":
        print("dasrulebulia")
        break
    elif info == "2":
        with open(path) as f:
            z = csv.reader(f)
            for i in z:
                print(i)
            input("daawiret rames gasagrdzeleblad")
    elif info == "1":
        name = input("your name: ")
        age = input("your age: ")
        country = input("your country: ")
        list = [name, age, country]
        with open(path, "a") as file:
            x = csv.writer(file)
            x.writerow(list)
            print("your information has been saved succesfully")
            input("daawiret rames rom gaagrdzelot")
#1
#shell sort - იღებს რაღაც დაშორებას ორ რიცხვს შოსრის ლისტში და იგივე დაშორებით ჯგუფდება ყველა რიცხვი ერთმანეთთან.
# პროგრამა ადარებს წყიველბს სანამ ყველა რიცხვი არ დაჯგუფბდება მეტობით

#merge sort - გახლიჩავს ლისტს შუაზე სანამ ერთ-ერთი ელემენტები არ დარჩება, მერე შეაწებებს ელემენტებს ისე როგორც გაიხლიჩა ლისტი,
# შეადარებს ერთმანეთს და დაალაგებს ზრდადობის მიხედვით სანამ ლისტი თავდაპირველ მდგომარეობას არ დუბრუნდება

#heap sort - პროგრამა დაალაგებს ელემენტებს გენელოგიური ხის მსგვასად (პირველი ელემენტი შეერთებული იქნება მეორე და მესამე ელემნტთან
# მორე ელემენტი იქნება შეერთებლუ მეოთხე და მეხუთე ელემენტთან, მესამე ელემენტი შეერთებლუ იქნება მეექვსე ელემენტთან და ასე შემდეგ).
# პროგრამა შეადარებს თავში მყოფ ელემენტს სხვა დაკავშირებულ ელემენტებთან და გადაანაცვლებს ამ ხეზე თავში მყოფ ელემენტებს იქამდე სანამ ლისტი არ დასორტირდება.


#2
# from random import randint

# arr = []

# for i in range(10):
#     arr.append(randint(1, 20))

# def bubble_sort():
#     n = len(arr) - 1
#     _sorted = False
#     while not _sorted:
#         _sorted = True
#         for i in range(0, n):
#             if arr[i] > arr[i + 1]:
#                 _sorted = False
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr

# def binary_search(arr, target):
#     low = 0
#     highest = len(arr) - 1
#     print(arr)

#     while low <= highest:
#         mid = (low + highest) // 2
#         mid_value = arr[mid]
#         if mid_value == target:
#             # print(mid_value)
#             return mid_value
#         elif mid_value < target:
#             low = mid + 1
#         else:
#             highest = mid - 1
#     return -1   


# print(binary_search(arr, 10))


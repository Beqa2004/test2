#1
Dictionary = {
    "Disciplinable": "A disciplinable action is one that someone can be disciplined (= punished) for, and a disciplinable person is someone who can be disciplined",
    "Enormity ": "concrete. A breach of law or morality; a transgression, crime; in later use, a gross and monstrous offence",
    "Abrogate": "transitive. To repeal (a law, established usage, etc.); to abolish authoritatively or formally; to annul, to cancel.",
    "nonplussed": "Brought to a nonplus or standstill; at a nonplus; perplexed, confounded.",
    "abjure": "transitive. To reject or repudiate on oath (a claim or claimant); to renounce or disavow (a thing). Also occasionally intransitive."
}


# def add_to_dict(dict, key, value):
#     if key in dict:
#         print("Word is already in the dictionary")
#     else:
#         dict[key] = value
#     return Dictionary



# def search_in_dict(dict, key):
#     if key in dict:
#         return f"definition of the wrod {key}: " + dict[key]
#     else:
#         return "Word not found"
    


# while True: 
#     starting_or_exiting_program = int(input("Type 1 if you want to exit or type 2 if you want to continue: "))
#     if starting_or_exiting_program == 1:
#         print("Exiting program...")
#         break
#     elif starting_or_exiting_program == 2:
#         print(add_to_dict(Dictionary, "hello", "hi"))
#         print(search_in_dict(Dictionary, "nonplussed"))
#     else:
#         print("Invalid input")



#2
quiz_questions = {
    "What is the capital of France?": ["Berlin", "Paris", "Madrid", "Rome"],
    "How many continents are there?": [5, 6, 7, 8],
    "What is the square root of 81?": [8, 9, 10, 11],
    # Add more questions...
}


# def take_quiz(quiz_questions):
#     x = 0
#     for i in quiz_questions:
#         print(i)
#         answer = input("type your answer: ")
#         if answer == quiz_questions["What is the capital of France?"][1]:
#             print("Correct")
#             x += 1
#         elif int(answer) == quiz_questions["How many continents are there?"][2]:
#             print("Correct")
#             x += 1
#         elif int(answer) == quiz_questions["What is the square root of 81?"][1]:
#             print("Correct")
#             x += 1
#         else:
#             print("incorrect")
#     return f"your total score is: {x} out of 3" 
        


# print(take_quiz(quiz_questions))

#dictionary-ში რომ ვამატებდი კიდე კითხვებს კოდი სულ ირეოდა და ვერ მივხვდი რატომ, რაგაც ერორს მიგდებდა
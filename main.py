print("Welcome to a simple quiz!")

playing = input("Would You like to play? ")

if playing.lower() not in ["yes", "y"]:
    quit()

print("Okay! Let's play :)")

score = 0

#Done with a Tuple
questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("What does ROM stand for? ", "read only memory")
]

#loop through each question
for question, correct_answer in questions:
    answer = input(f"{question}").lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# Final Score
print(f"\nYou got {score} out of {len(questions)} questions correct!")
print(f"You scored {(score / len(questions)) * 100:.2f}%.")

# Long way 

# answer = input("What does CPU stand for? ")
# if answer.lower() == "central processing unit":
#     print('Correct!')
#     score +=1
# else:
#     print("InCorrect!")

# answer = input("What does GPU stand for? ")
# if answer.lower() == "graphics processing unit":
#     print('Correct!')
#     score +=1
# else:
#     print("InCorrect!")

# answer = input("What does RAM stand for? ")
# if answer.lower() == "random access memory":
#     print('Correct!')
#     score +=1
# else:
#     print("InCorrect!")

# answer = input("What does PSU stand for? ")
# if answer.lower() == "power supply":
#     print('Correct!')
#     score +=1
# else:
#     print("InCorrect!")

# answer = input("What does ROM stand for? ")
# if answer.lower() == "read only memory":
#     print('Correct!')
#     score +=1
# else:
#     print("InCorrect!")

# print("You got " + str(score) + " questions correct!")
# print("You got " + str((score/5) * 100) + "%.")
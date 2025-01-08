import json

with open("Work/Python/questions.json", "r") as file:
    content = file.read()

# print("content below here is a string:", "\n", content)

data = json.loads(content)

# print(type(content))
# print(type(data))

# print("content below here is a list:", "\n", data)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice
    #print(question["user_choice"], question["correct_answer"])
    if question["user_choice"] == question["correct_answer"]:
        print("dooru")
        score += 1
        result = "Correct Answer!,"
    else:
        print("yannis")
        result = "Wrong Answer!,"
    message = f"{result} Your answer is: {question['user_choice']}, " \
              f"Correct answer is: {question['correct_answer']} "
    print(message)



# for index, question in enumerate(data):


#     message = f"{result} {index + 1} - Your answer is: {question['user_choice']}, " \
#               f"Correct answer is: {question['correct_answer']} "
#     print(message)
#print(data)
print(score, "/", len(data))
# -------------------------
def start_quiz():

    selections = []
    correct_selections = 0
    question_num = 1
    nickname = ""

    nickname = input("Please enter your nickname: ")
    print("Hello "+str(nickname)+", below is the first question, good luck!")

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        selection = input("Enter (A, B, C, or D): ")
        selection = selection.upper()
        selections.append(selection)

        correct_selections += check_result(questions.get(key), selection)
        question_num += 1

    show_score(correct_selections, selections)

    
# -------------------------
def check_result(result, selection):
    choices = ['A', 'B', 'C', 'D']

    if selection not in choices:
        print("Selection is not valid")
        return 0

    elif selection == result:
        print("YOU ARE CORRECT!")
        return 1
        
    else:
        print("YOU ARE WRONG!")
        return 0

# -------------------------
def show_score(correct_selections, selections):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("results: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("selections: ", end="")
    for i in selections:
        print(i, end=" ")
    print()

    score = int((correct_selections/len(questions))*100)
    print("You achieved: "+str(score)+"%")

    # -------------------------
def restart_game():

    response = input("Would you like to try again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False 

# -------------------------


questions = {
 "1: ": "A",
 "2: ": "B",
 "3: ": "C",
 "4: ": "A"
}

options = [["A. 1", "B. 2", "C. 3", "D. 4"],
          ["A. 1", "B. 2", "C. 3", "D. 4"],
          ["A. 1", "B. 2", "C. 3", "D. 4"],
          ["A. 1", "B. 2", "C. 3", "D. 4"]]

start_quiz()

while restart_game():
    start_quiz()

print("Good luck!")

# -------------------------
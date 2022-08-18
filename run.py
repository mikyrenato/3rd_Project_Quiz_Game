# -------------------------
def start_quizz():

    selections = []
    correct_selections = 0
    question_num = 1

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

    if result == selection:
        print("YOU ARE CORRECT!")
        return 1
    else:
        print("YOU ARE WRONG!")
        return 0

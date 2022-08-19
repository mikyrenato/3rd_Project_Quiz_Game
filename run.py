nickname = ""
nickname = input("Please enter your nickname: ")
print("Hello "+str(nickname)+", below is the first question, good luck!")

# -------------------------
def start_quiz():

    selections = []
    correct_selections = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        while True:
            selection = input("Enter (A, B, C, or D): ")
            selection = selection.upper()
            if selection not in ('A', 'B', 'C', 'D'):
                print("Invalid choice, try again:")
            else:
                break

        selections.append(selection)

        correct_selections += check_result(questions.get(key), selection)
        question_num += 1

    resp = input("Would you like to reveal the answers? (yes or no): ")
    resp = resp.upper()

    if resp == "YES":
        show_score(correct_selections, selections)
    else:
        return False 
    
# -------------------------
def check_result(result, selection):

    if selection == result:
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
    print(str(nickname)+", you achieved: "+str(score)+"%")

    # -------------------------
def restart_game():

    response = input("Would you like to try again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False 

# -------------------------

def reveal_answers():

    resp = input("Would you like to reveal the answers? (yes or no): ")
    resp = resp.upper()

    if resp == "YES":
        return True
    else:
        return False 

# -------------------------


questions = {
 "1: Which player scored the fastest hat-trick in the Premier League?": "A",
 "2: Which player, with 653 games, has made the most Premier League appearances?": "B",
 "3: Three players share the record for most Premier League red cards (8). Who are they?": "C",
 "4: With 260 goals, who is the Premier League's all-time top scorer?": "D",
 "5: When was the inaugural Premier League season?": "A",
 "6: Which team won the first Premier League title?": "B",
 "7: With 202 clean sheets, which goalkeeper has the best record in the Premier League?": "C",
 "8: How many clubs competed in the inaugural Premier League season?": "D",
 "9: Which three players shared the Premier League Golden Boot in 2018-19?": "A",
 "10: The fastest goal scored in Premier League history came in 7.69 seconds. Who scored it?": "B"
}

options = [["A. Sadio Mane", "B. Cristiano Ronaldo", "C. Michael Owen", "D. Didier Drogba"],
          ["A. Wayne Rooney", "B. Gareth Barry", "C. Rio Ferdinand", "D. John Terry"],
          ["A. Nemanja Vidic, John Terry and Patrice Evra", "B. Patrick Vieira, Virgil Van Dijk and Duncan Ferguson", "C. Patrick Vieira, Richard Dunne and Duncan Ferguson", "D. Nemanja Vidic, John Terry and Richard Dunne"],
          ["A. 1", "B. 2", "C. 3", "D. Alan Shearer"],
          ["A. 1992-93", "B. 2", "C. 3", "D. 4"],
          ["A. 1", "B. Manchester United", "C. 3", "D. 4"],
          ["A. 1", "B. 2", "C. Petr Cech", "D. 4"],
          ["A. 1", "B. 2", "C. 3", "D. 22"],
          ["A. Pierre-Emerick Aubameyang, Mohamed Salah and Sadio Mane", "B. 2", "C. ", "D. 4"],
          ["A. 1", "B. Shane Long (for Southampton vs Watford in 2018-19)", "C. 3", "D. "]]

start_quiz()

while restart_game():
    start_quiz()

print("Good luck!")

# -------------------------
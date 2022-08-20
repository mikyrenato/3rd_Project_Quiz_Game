import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz_game')


print("Do you know much about football? Can you make it on the leaderboard?")
nickname = ""
nickname = input("Please enter your nickname: \n")
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
            selection = input("Enter (A, B, C, or D): \n")
            selection = selection.upper()
            if selection not in ('A', 'B', 'C', 'D'):
                print("Invalid choice, the only options are: A, B, C, or D")
            else:
                break

        selections.append(selection)

        correct_selections += check_result(questions.get(key), selection)
        question_num += 1

    resp = input("Would you like to reveal the answers together with your result % ? (yes or no): \n")
    resp = resp.upper()

    if resp == "YES":
        score = int((correct_selections/len(questions))*100)
        print(str(nickname)+", you achieved: "+str(score)+"%")
        show_score(correct_selections, selections)
        data = nickname, score
        quiz_data = [num for num in data]
        update_worksheet(quiz_data, "Leaderboard")
        leaderboard()
    else:
        score = int((correct_selections/len(questions))*100)
        print(str(nickname)+", you achieved: "+str(score)+"%")
        data = nickname, score
        quiz_data = [num for num in data]
        update_worksheet(quiz_data, "Leaderboard")
        leaderboard()
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

    print("results:    ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("selections: ", end="")
    for i in selections:
        print(i, end=" ")
    print()


# -------------------------


def restart_game():

    response = input("Would you like to try again? (yes or no): \n")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False 


# -------------------------


def update_worksheet(data, worksheet):

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


# -------------------------


def leaderboard():

    lead = SHEET.worksheet('Leaderboard')

    data = lead.get_all_values()

    size = lambda dat: dat[1]

    data.sort(key=size, reverse=True)

    print(tabulate(data[0:11], headers=['Leaderboard', 'Table']))


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
          ["A. Cristiano Ronaldo", "B. Carlos Tevez", "C. Thierry Henry", "D. Alan Shearer"],
          ["A. 1992-93", "B. 1991-1992", "C. 1989-90", "D. 1993-94"],
          ["A. Chelsea", "B. Manchester United", "C. Arsenal", "D. Liverpool"],
          ["A. Edwin Van der Sar", "B. David De Gea", "C. Petr Cech", "D. Peter Schmeichel"],
          ["A. 26", "B. 24", "C. 20", "D. 22"],
          ["A. Pierre-Emerick Aubameyang, Mohamed Salah and Sadio Mane", "B. Harry Kane, Mohamed Salah and Sadio Mane", "C. Pierre-Emerick Aubameyang, Hiung Ming Son and Sadio Mane. ", "D. Pierre-Emerick Aubameyang, Mohamed Salah and Jamie Vardy"],
          ["A. Cristiano Ronaldo", "B. Shane Long", "C. Carlos Tevez", "D. Zlatan Ibrahimovic"]]


start_quiz()


while restart_game():
    start_quiz()


print("Thank you and have a nice day! :)")


# -------------------------

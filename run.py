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
print("The quiz has 20 questions about Premier league and World Cup")
print("Each question will give you 5 points out of 100.")
print("If you still feel confident, please follow the steps below:")
nickname = ""
nickname = input("Please enter your nickname: \n")
print("Hello "+str(nickname)+", below is the first question, good luck!")

# This is the main function which will run the quiz
def start_quiz():

    selections = []
    correct_selections = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        # This is the validation in case the user is choosing an invalid answer
        while True:
            selection = input("Enter (A, B, C, or D): \n")
            selection = selection.upper()
            if selection not in ('A', 'B', 'C', 'D'):
                print("Invalid choice, the only options are A, B, C, or D")
            else:
                break

        selections.append(selection)

        correct_selections += check_result(questions.get(key), selection)
        question_num += 1
    # the user is being asked if he want to see the correct answers
    resp = input("Would you like to reveal the answers together"
                 "with your result % ? (yes or no): \n")
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

# This function is telling the user if the answer was correct/incorrect
def check_result(result, selection):

    if selection == result:
        print("YOU ARE CORRECT!")
        return 1
    else:
        print("YOU ARE WRONG!")
        return 0

# This fucntion will show the correct results and the choices
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

# This fucntion is asking the user if he wants to try again or end the game
def restart_game():
    while True:
        response = input("Would you like to try again? (yes or no): \n")
        response = response.upper()
        if response not in ('YES', 'NO'):
            print("Invalid choice, the only options are YES or NO")
        elif response == "YES":
            return True
        else:
            break

# This fucntion is updating the leaderboard worksheet
def update_worksheet(data, worksheet):

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

# Sorting from highest to lowest the top 10 results from the worksheet
def leaderboard():

    lead = SHEET.worksheet('Leaderboard')

    data = lead.get_all_values()

    size = lambda dat: float(dat[1])

    data.sort(key=size, reverse=True)

    print(tabulate(data[0:11], headers=['Leaderboard', 'Score']))

# These are the quiz questions and answers
questions = {
 "1: Which player scored the fastest hat-trick in the Premier League?": "A",
 "2: Which player, with 653 games, has made the most"
 "Premier League appearances?": "B",
 "3: Three players share the record for most Premier"
 "League red cards (8). Who are they?": "C",
 "4: With 260 goals, who is the Premier League's all-time top scorer?": "D",
 "5: When was the inaugural Premier League season?": "A",
 "6: Which team won the first Premier League title?": "B",
 "7: With 202 clean sheets, which goalkeeper has the"
 "best record in the Premier League?": "C",
 "8: How many clubs competed in the inaugural Premier League season?": "D",
 "9: Which three players shared the"
 "Premier League Golden Boot in 2018-19?": "A",
 "10: The fastest goal scored in Premier League"
 "history came in 7.69 seconds. Who scored it?": "B",
 "11: There have been two World Cup trophies."
 "What was the name of the first?": "C",
 "12: Which country won the first ever World Cup in 1930?": "D",
 "13: Which country has won the most World Cups?": "A",
 "14: Three countries have won the World Cup twice. Can you name them?": "B",
 "15: Which country has appeared in three World Cup finals,"
 "but never won the competition?": "C",
 "16: The 2026 World Cup will be hosted across three different countries."
 "Can you name them?": "D",
 "17: In which World Cup did Diego Maradona"
 "score his infamous 'Hand of God' goal?": "A",
 "18: The record number of World Cup goals is 16, scored by who?": "B",
 "19: Three people have won the World Cup as a player and as a coach."
 "Mario Zagallo, Didier Deschamps and... can you name the third?": "C",
 "20: Two English players have won the World Cup Golden Boot."
 "Who are they?": "D"
}

# These are the quiz options
options = [["A. Sadio Mane", "B. Cristiano Ronaldo",
            "C. Michael Owen", "D. Didier Drogba"],
           ["A. Wayne Rooney", "B. Gareth Barry",
            "C. Rio Ferdinand", "D. John Terry"],
           ["A. Nemanja Vidic, John Terry and Patrice Evra",
           "B. Patrick Vieira, Virgil Van Dijk and Duncan Ferguson",
            "C. Patrick Vieira, Richard Dunne and Duncan Ferguson",
            "D. Nemanja Vidic, John Terry and Richard Dunne"],
           ["A. Cristiano Ronaldo", "B. Carlos Tevez",
           "C. Thierry Henry", "D. Alan Shearer"],
           ["A. 1992-93", "B. 1991-1992", "C. 1989-90", "D. 1993-94"],
           ["A. Chelsea", "B. Manchester United",
           "C. Arsenal", "D. Liverpool"],
           ["A. Edwin Van der Sar", "B. David De Gea",
           "C. Petr Cech", "D. Peter Schmeichel"],
           ["A. 26", "B. 24", "C. 20", "D. 22"],
           ["A. Pierre-Emerick Aubameyang, Mohamed Salah and Sadio Mane",
           "B. Harry Kane, Mohamed Salah and Sadio Mane",
            "C. Pierre-Emerick Aubameyang, Hiung Ming Son and Sadio Mane. ",
            "D. Pierre-Emerick Aubameyang, Mohamed Salah and Jamie Vardy"],
           ["A. Cristiano Ronaldo", "B. Shane Long",
            "C. Carlos Tevez", "D. Zlatan Ibrahimovic"],
           ["A. World Football Cup / The Cup",
           "B. World Cup Trophy / World Trophy",
            "C. Jules Rimet Trophy / Victory",
            "D. Victory / orld Football Cup"],
           ["A. Argentina", "B. Brazil", "C. Spain", "D. Uruguay"],
           ["A. Brazil", "B. Italy", "C. Germany", "D. Mexico"],
           ["A. Spain, Italy and Germany", "B. Argentina, France and Uruguay",
            "C. Argentina, Brazil and Spain",
            "D. Italy, Netherlands and Uruguay"],
           ["A. Italy", "B. Germany", "C. Netherlands", "D. Spain"],
           ["A. Spain, Italy and Germany", "B. Argentina, France and Uruguay",
            "C. Italy, Netherlands and Uruguay",
            "D. United States, Canada and Mexico"],
           ["A. Mexico 1986", "B. Germany 1990",
            "C. Spain 1982", "D. Italy 1986"],
           ["A. Cristiano Ronaldo", "B. Miroslav Klose",
            "C Lionel Messi", "D. Fernando Torres"],
           ["A. Diego Maradona", "B. Gica Hagi",
            "C. Franz Beckenbauer", "D. Ronaldo Nazario"],
           ["A. Jamie Vardy (2014) and Harry Kane (2018)",
            "B. Gary Lineker (1986) and Jamie Vardy (2018)",
            "C. Gary Lineker (1986) and Raheem Sterling (2018)",
            "D. Gary Lineker (1986) and Harry Kane (2018)"]]


start_quiz()


while restart_game():
    start_quiz()


print("Thank you and have a nice day! :)")

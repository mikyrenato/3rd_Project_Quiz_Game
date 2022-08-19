import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz_game')

def get_quiz_data():

    while True:
        print("Please enter quiz data.")

        data_str = input("Enter your data here:\n")

        quiz_data = data_str.split(",")

        if validate_data(quiz_data):
            print("Data is valid!")
            break

    return quiz_data


def validate_data(values):

    try:
        [int(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def main():

    data = get_quiz_data()
    quiz_data = [int(num) for num in data]
    update_worksheet(quiz_data, "Sheet1")


print("Welcome to the football quiz")
main()
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

    data_str = input("Enter your data here:\n")

    quiz_data = data_str.split(",")

    return quiz_data

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
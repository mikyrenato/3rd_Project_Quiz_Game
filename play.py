import gspread
import pandas as pd
from tabulate import tabulate
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

def leaderboard():

    lead = SHEET.worksheet('Leaderboard')

    data = lead.get_all_values()

    size = lambda dat: dat[1]

    data.sort(key=size, reverse=True)

    print(tabulate(data, headers=['Leaderboard', 'Table']))


leaderboard()


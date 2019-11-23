from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from ExpaData import get_expa_data

# If modifying these scopes, delete the file token.pickle.
from LcUtils import lcs
from MonthCellsUtils import month_cells_mc_term_2019_2, months_mc_term, month_cells_mc_term_2018_2, \
    month_cells_lc_term_2019, month_cells_lc_term_2018, months_lc_term

SCOPES = ['https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'
SPREADSHEET_ID = '1KXMLGX7Vze8bsEUGaLEA4xen7PU0mjVd5A8IoOz0aFM'


def update_fin_co_data(year: int = 2019, term: str = 'lc term'):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    if term == 'lc term':
        months = months_lc_term
    else:
        months = months_mc_term

    if year == 2019 and term == 'mc term':
        term = 'mc term 19.2'
    elif year == 2018 and term == 'mc term':
        term = 'mc term 18.2'
    elif year == 2019 and term == 'lc term':
        term = 'lc term 19'
    elif year == 2018 and term == 'lc term':
        term = 'lc term 18'
    else:
        term = 'mc term 19.2'

    if term == 'mc term 19.2':
        month_cells = month_cells_mc_term_2019_2
    elif term == 'mc term 18.2':
        month_cells = month_cells_mc_term_2018_2
    if term == 'lc term 19':
        month_cells = month_cells_lc_term_2019
    elif term == 'lc term 18':
        month_cells = month_cells_lc_term_2018
    else:
        month_cells = month_cells_mc_term_2019_2

    value_input_option = 'USER_ENTERED'

    # print(month_cells)
    # print(months)

    for lc in lcs:
        print(lc)
        for month in months:
            if month == 'January':
                year += 1

            range_name = lc + ' ' + month_cells[month]

            value_range_body = {
                'range': range_name,
                'majorDimension': 'ROWS',
                'values':
                    get_expa_data(year, month, lc)

            }

            request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=range_name,
                                                             valueInputOption=value_input_option, body=value_range_body)
            response = request.execute()

            print(response)

            if month == 'January':
                year -= 1


def main():
    update_fin_co_data(year=2019, term='lc term')


if __name__ == '__main__':
    main()

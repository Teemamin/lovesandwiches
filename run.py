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
SHEET = GSPREAD_CLIENT.open('love_sandwich')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)


def get_sales_data():
    """
    Get sales data from user
    """
    print("please enter sales dta from the last market")
    print("data should be six numbers seperated by commas ")
    print("10,20,30,40,50,60\n")
    data_str = input("enter your data here:")
    sale_data = data_str.split(",")
    validate_data(sale_data)


def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values required, {len(values)} is provided")
    except ValueError as e:
        print(f"inavlid data {e}, please try again \n")


get_sales_data()

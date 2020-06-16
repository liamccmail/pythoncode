"""
Exporting a csv file to Google Sheets
Liam Cunliffe

"""

import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def scan_df(df):
    for val in df.columns:
        yield val # Holds column names from csv
    for row in df.to_numpy():
        for val in row:
            yield val # Holds data from each row

def df_to_gsheet(df, sheet):
    sheet.clear() # Clears current selected G Sheet
    (row, column) = df.shape # Creates tuple of max rows and max columns
    print(gspread.utils.rowcol_to_a1(row + 1, column))
    cells = sheet.range("A1:{}".format(gspread.utils.rowcol_to_a1(row + 1, column))) # Sets the range of cells for gsheet from A1 to bottom right of sheet eg. A1:D38 for forecast_tab
    for cell, value in zip(cells, scan_df(df)): # zip(cells, scandf(df)) combines the correct cell with its value from the dataframe
        cell.value = value # assigns the cell the value from the dataframe
    sheet.update_cells(cells) # Fills gsheet will all cell values

# This section involves authorization of credentials taken from the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive.file',"https://www.googleapis.com/auth/drive"] 
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/liamcunliffe/Documents/HelloFreshHomework/service_account.json', scope)
gc = gspread.authorize(credentials) # authorises credentials

forecast = '/Users/liamcunliffe/Documents/HelloFreshHomework/ops_tech_homework_files/Part2/w03_forecast.csv'
# forecast = 'w03_forecast.csv' USE THIS LOCATION
picklist = '/Users/liamcunliffe/Documents/HelloFreshHomework/ops_tech_homework_files/Part2/w03_picklist.csv'
# picklist = 'w03_picklist.csv' USE THIS LOCATION

fcdf = pd.read_csv(forecast) # Read in forecast csv as dataframe
pldf = pd.read_csv(picklist) # Read in picklist csv as dataframe

forecast_spreed = gc.open("Forecast W03") # open gsheet for which we want to add data
forecast_tab = forecast_spreed.worksheet("Forecast_tab") # select forecast_tab
picklist_tab = forecast_spreed.worksheet("picklist_tab") # select picklist_tab

df_to_gsheet(fcdf, forecast_tab) # send forecast dataframe to gsheet
df_to_gsheet(pldf, picklist_tab) # send picklist dataframe to ghseet

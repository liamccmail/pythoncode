"""
Extraction of specified column names in deliveries_extract.csv
Liam Cunliffe

open csv file
identify columns which need to be added to new file.
identify rows which need to be deleted
delete rows, and add them to new csv file
insert Category column
insert OT column using the comparitors
Export to csv
add all new rows to new clean_deliveries_extract.csv file

"""
import csv
import pandas as pd
pd.options.display.max_columns = None 
import numpy as np

# This is the location of where the original deliveries_extract.csv was located on my computer, will need to change when sent over
fileloc = '/Users/liamcunliffe/Documents/HelloFreshHomework/ops_tech_homework_files/Part2/deliveries_extract.csv'
# fileloc2 = 'deliveries_extract.csv' Set this to file loc when sending over.

columns_list = ["Delivery Key", "SKU", "Ingredient", 
                "PO number", "Supplier Code", "Supplier Name", 
                "Week", "Expected Total Number of units", "Final Count:\nUnits per case", 
                "% of Total Rejected", "Total Quantity Rejected", "Final Quantity", 
                "Shortage", "Planned Delivery Date", "Auto insert Date Stamp", 
                "Planned Delivery Time Start", "Planned Delivery Time End", "Delivery Receive Time"] # All columns selected for new file

 
df = pd.read_csv(fileloc, usecols=columns_list) # Reads in the columns specified above

df.rename(columns = {"Expected Total Number of units" : "Expected Quantity",
                     "Final Count:\nUnits per case" : "Received Quantity",
                     "Auto insert Date Stamp" : "Actual Delivery Date",
                     "Delivery Receive Time" : "Actual Delivery Time"}, inplace = True) # Renaming columns to specified names 

df.insert(13, "Category", df["SKU"].str[:3]) # Sets cell values of Category to first 3 letters of SKU value

df["Actual Delivery Date"] = pd.to_datetime(df["Actual Delivery Date"]) # Converting Date to be able to compare
df["Planned Delivery Date"] = pd.to_datetime(df["Planned Delivery Date"]) # Converting Date to be able to compare#
df["Actual Delivery Time"] = pd.to_datetime(df["Actual Delivery Time"]).dt.strftime('%H:%M:%S') # Convert time to be able to compare
df["Planned Delivery Time Start"] = pd.to_datetime(df["Planned Delivery Time Start"]).dt.strftime('%H:%M:%S') # Convert time to 24 hours
df["Planned Delivery Time End"] = pd.to_datetime(df["Planned Delivery Time End"]).dt.strftime('%H:%M:%S') # Convert time to be able to compare

check1 = (df["Actual Delivery Date"] > df["Planned Delivery Date"]) # Checks if the actual delivery date is after the planned date
check2 = (df["Actual Delivery Time"] > df["Planned Delivery Time End"]) # Checks if the time of day is after the planned time of delivery

df.insert(14, "OT", "") # Insert OT column, with empty cells
df.loc[check1, "OT"] = "0" # Checks delivery dates and assigns 0 to all cells which were more than a day after the planned delivery date
df.loc[(df.OT == ""), "OT"] = "1" # Sets all remaining columns to 1 (Eg. came before or same day as planned delivery date)
df.loc[(df.OT == "1") & (check1) & (check2), "OT"] = "0" # Runs both checks to see if the time of delivery is before the planned time of delivery

deleted_rows = df[df["Supplier Name"] == "not found"] # Creates new table of suppliers with unknown names
deleted_rows.to_csv("deleted_rows.csv") # Exporting deleted rows to csv
df = df[df["Supplier Name"] != "not found"] # Removes rows where supplier name is not found


df = df[["Delivery Key", "SKU", "Ingredient", "PO number", "Supplier Code", "Supplier Name", "Week", "Expected Quantity", "Received Quantity", "% of Total Rejected", "Total Quantity Rejected", "Final Quantity", "Shortage", "Category", "OT", "Planned Delivery Date", "Actual Delivery Date", "Planned Delivery Time Start", "Planned Delivery Time End", "Actual Delivery Time"]]
print(df)

df.to_csv("clean_deliveries_extract.csv") # Export cleaned file to csv
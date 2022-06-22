"""
Joining 2 extracts to forcast number of ingredients needed for a week
Liam Cunliffe

"""
import csv
import pandas as pd
pd.options.display.max_columns = None 
import numpy as np

# This is the location of where the original deliveries_extract.csv was located on my computer, will need to change when sent over
forecast = '/Users/liamcunliffe/Documents/HelloFreshHomework/ops_tech_homework_files/Part2/w03_forecast.csv'
picklist = '/Users/liamcunliffe/Documents/HelloFreshHomework/ops_tech_homework_files/Part2/w03_picklist.csv'
#forecast = 'w03_forecast.csv'  USE THIS LOCATION 
#picklist = 'w03_picklist.csv'  USE THIS LOCATION

fcdf = pd.read_csv(forecast) # read in forecast dataframe
pcdf = pd.read_csv(picklist) # read in picklist dataframe
fcpidf = pd.DataFrame(columns=["Week", "Sku_Code", "Quantity"]) # Initializing the forecast per ingredient dataframe

unique_list_of_ingredients = pcdf["sku_code"].unique() # Extracts all unique ingredient sku codes

# This function takes 2 lists and multiplies their opposite index value
# Used to multiple the values of pick list with corresponding recipe
def multiply_vals(l1, l2):
    if len(l1) < 1 or len(l2) < 1:
        return 0
    q = 0
    for i in range(len(l1)):
        q += l1[i] * l2[i]
    return q

for ingr in unique_list_of_ingredients: # Iterate through all ingredients
    if pcdf["sku_code"].str.contains(ingr).any():
        curr_df = pcdf[pcdf["sku_code"].str.contains(ingr)] # Selects the rows which contain the ingredient name
        picks_list = curr_df["picks"].to_list() # creates list of all picks from specified ingredient
        list_of_recipe_indexes = curr_df["recipe_index"].to_list() # converts all recipe indexes into list
        list_of_recipe_sizes = curr_df["nb_people"].to_list() # converts all recipe sizes into list
        rs = list(map(lambda x, y:(x,y), list_of_recipe_indexes, list_of_recipe_sizes))  # Merges recipe indexes and sizes into 1 tuple inside of a list
        meal_nr_list = []
        count = 0
        for r in rs: # to loop through recipe and pull out meal_nr
            filtereddf = fcdf[(fcdf["recipe"] == r[0]) & (fcdf["size"] == r[1])] # selects corresponding recipe and size rows with forecasted number of meals
            if filtereddf.empty: # checks to see if the filtered dataframe is empty
                try:
                    del picks_list[count] # deletes pick list value if the recipe index was not contained in forcast eg. indexes 30, 31, 32
                except:
                    continue # if the picks list is empty, continue onto the next section
            else:
                meal_nr_list += filtereddf["meal_nr"].to_list() # creates list of meal_nr to multiply with ingredient pick list values
            count += 1
        quantity = multiply_vals(picks_list, meal_nr_list) # evaulates the quantity by multipling the sum of meal_nr by the sum of picks for an ingredient
        if quantity > 0: # Neglects all recipes not included in forecast
            week = pcdf.loc[pcdf["sku_code"] == ingr, "hf_week"].iloc[0] # extracts week from picklist
            curr_df_len = len(fcpidf) # Used to find location to append new row
            row = [week, ingr, quantity] # sets up new row to add to table
            fcpidf.loc[curr_df_len] = row # adds new row to table

fcpidf.to_csv("forcast_per_ingredientPYTHON.csv") # Export data to csv file






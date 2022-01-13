# from art import logo
import pandas as pd
import os
import math

# print(logo)

"""
    Write a program that can compare the 3 separate camera checks each day.
    The script should accept each file as in input
    Script needs to compare each line and column to find differences in values

"""
# read in all three files
path = input("Please provide the path to the file folder: ")

# create a list files path
files_list = os.listdir(path)

# print(files_list)



compare = {}
for file in files_list:
    pathFile = os.path.join(path, file)
    temp_df = pd.read_csv(pathFile, header=None)

    # Change all text in column to lower or uppercase
    temp_df[1] = temp_df[1].str.lower()
    temp_df[1] = temp_df[1].replace({'y': 'yes', 'n': 'no'})
    # print(temp_df)

    for idx, row in temp_df.iterrows():
        key = row[0]
        value = row[1]
        
        # print(key, value)

        if key not in compare.keys():
            compare[key] = []

        compare[key].append(value)



for k, v in compare.items():
    total = 0
    
    if v.count(v[0]) == len(v):
        print(f"✓ {k} {v[0]}")
    else:
        for item in v:
            try:
                total += float(item)
            except Exception as e:
                print(e)
                pass
            average = total / len(v)
            print(f"{k} Total: {total}, Average: {round(average)}")

        
        # print(f"✘ {k}: {v}")
    
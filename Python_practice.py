        # -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
from types import CoroutineType

# Add a variable to load a file from a path.
file_to_load = 'Resources\election_results.csv'
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1: Create a county list and county votes dictionary.

counties = []
county_votes = {}


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
        
    for row in reader:

       
        # 3: Extract the county name from each row.
        counties_name = row[1]
  
       
       
       
       
        if counties_name not in counties:             

            # 4b: Add the existing county to the list of counties.
            counties.append(counties_name)

            # 4c: Begin tracking the county's vote count.

            county_votes[counties_name] = 0

        # 5: Add a vote to that county's vote count.

            county_votes[counties_name] +=1







    




    












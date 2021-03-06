# Election Analysis
An audit of the results of a local election was completed in order to find a number of data points, including voter turnout and the winner of the election.  Specifically, we were charged with finding the following:

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software:  Python version 3.9.7 & Visual Studio Code version 1.61.0

## Summary of Results
The following sections will address the election results based on our audit.

### Total Votes and the Candidates

Overall, there were 369,711 votes cast in the election.  These votes were divided between 3 candidates:  Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane

### The Candidates and Votes Received
The breakdown of votes received is as follows:

   - Charles Casper Stockham received 85,213 total votes, which was 23.0% of the total votes.
   - Diana DeGette received 272,892 total votes, which was 73.8% of the total votes.
   - Raymon Anthony Doane received 11,606 total votes, which was 31.0% of the total votes.

### Winner of the Election
Based on these results the winner of the election was Diana DeGette.

## Challenge Overview
The challenge was designed to find data regarding voter turnout for each county in the election and to output the results in the terminal as well as write them to a text file. The data for each county was considered along with the overall 369,711 votes.


## Challenge Summary
There were 3 counties that participated in the election:  Arapahoe, Denver, & Jefferson. 

### Voter Turnout By County
   - Arapahoe turned out 24,801 votes, which constituted 3.1% of the overall voter turnout
   - Denver turned out 306,055 votes, which constituted 82.8% of the overall voter turnout
   - Jefferson turned out 38,855 votes, which constituted 10.5% of the overall voter turnout


### Largest Voter Turnout
Based on these results, Denver had the largest voter turnout by a large margin.

## Overall Election Audit Summary

The code used for this audit is very versatile and could be used for future elections.  It uses dictionaries, lists, loops and conditions to gather and store data, avoid redundancies, and execute mathematical functions to declare a winner of the election.  By changing the document that is read(file_to_load), new election data can be pulled into the script and adopted to any election.  

Additionally, with simple modifications there is the possibility to get more information that could assist the commission.  For example, one could examine the county turnout based on the number of registered voters for each county, which would adjust the turnout percentage based on county population and not the overall turnout.  The number of registered voters would need to be documented and the code adjusted accordingly. 

Finally, one of the positive aspects of this code is that once the data is run through, it can be written to a text file, as seen below.  This allows for an easier reading of the results. 

![overall results](https://github.com/cflavallee/Election_Analysis/blob/main/Resources/Overall%20Election%20Results.PNG)

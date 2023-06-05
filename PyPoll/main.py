import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
textpath = os.path.join("Analysis", "analysis.txt")

charles_votes = 0
diana_votes = 0
raymon_votes = 0

with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # skips the header for calculations
    for row in csvreader:
        if row[2] == "Charles Casper Stockham":
            charles_votes+= 1
        if row[2] == "Diana DeGette":
            diana_votes+= 1
        if row[2] == "Raymon Anthony Doane":
            raymon_votes+= 1
    totalvotes = charles_votes+diana_votes+raymon_votes
    votelist = [charles_votes, diana_votes, raymon_votes]
    if max(votelist) == diana_votes:
        winner = "Diana DeGette"
    if max(votelist) == charles_votes:
        winner = "Charles Casper Stockham"
    if max(votelist) == raymon_votes:
        winner = "Raymon Anthony Doane"
    print("Total Votes: ", str(totalvotes))
    print("Charles Casper Stockham: ",str("{:.3%}".format(charles_votes/totalvotes)), str(charles_votes))
    print("Diana DeGette: ",str("{:.3%}".format(diana_votes/totalvotes)), str(diana_votes))
    print("Raymon Anthony Doane: ",str("{:.3%}".format(raymon_votes/totalvotes)), str(raymon_votes))
    print("Winner: ", winner)
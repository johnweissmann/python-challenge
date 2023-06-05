import os
import csv
#import dependencies

#create path for external files
csvpath = os.path.join("Resources", "election_data.csv")
textpath = os.path.join("Analysis", "analysis.txt")

#start at 0 votes for each candidate
charles_votes = 0
diana_votes = 0
raymon_votes = 0

with open(csvpath, encoding="UTF-8") as csvfile: #open csv so we can read it
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # skips the header for calculations
    for row in csvreader: #create a loop that adds a vote to the respective category each time it appears
        if row[2] == "Charles Casper Stockham":
            charles_votes+= 1
        if row[2] == "Diana DeGette":
            diana_votes+= 1
        if row[2] == "Raymon Anthony Doane":
            raymon_votes+= 1
    totalvotes = charles_votes+diana_votes+raymon_votes #add up all the votes to get total votes
    votelist = [charles_votes, diana_votes, raymon_votes]
    #create an if statement that determines which vote count was the highest and then saves their name in the variable "winner"
    if max(votelist) == diana_votes:
        winner = "Diana DeGette"
    if max(votelist) == charles_votes:
        winner = "Charles Casper Stockham"
    if max(votelist) == raymon_votes:
        winner = "Raymon Anthony Doane"
    
    # print the results to the terminal
    print("Total Votes: ", str(totalvotes))
    print("Charles Casper Stockham: ",str("{:.3%}".format(charles_votes/totalvotes)), str(charles_votes))
    print("Diana DeGette: ",str("{:.3%}".format(diana_votes/totalvotes)), str(diana_votes))
    print("Raymon Anthony Doane: ",str("{:.3%}".format(raymon_votes/totalvotes)), str(raymon_votes))
    print("Winner: ", winner)
    
    #convert the results to lists so I can use the txt.writelines function
    Total_Votes = ["Total Votes: ", str(totalvotes)]
    Charles = ["Charles Casper Stockham: ",str("{:.3%}".format(charles_votes/totalvotes)), str(charles_votes)]
    Diana = ["Diana DeGette: ",str("{:.3%}".format(diana_votes/totalvotes)), str(diana_votes)]
    Raymon = ["Raymon Anthony Doane: ",str("{:.3%}".format(raymon_votes/totalvotes)), str(raymon_votes)]
    Winner = ["Winner: ", winner]

with open(textpath,"w") as txt: #write the analysis file
    txt.writelines("Election Results")
    txt.writelines("\n") #creates a new line
    txt.writelines("---------------------------")
    txt.writelines("\n")
    txt.writelines(Total_Votes)
    txt.writelines("\n")
    txt.writelines("---------------------------")
    txt.writelines("\n")
    txt.writelines(Charles)
    txt.writelines("\n")
    txt.writelines(Diana)
    txt.writelines("\n")
    txt.writelines(Raymon)
    txt.writelines("\n")
    txt.writelines("---------------------------")
    txt.writelines("\n")
    txt.writelines(Winner)
    txt.writelines("\n")
    txt.writelines("---------------------------")
import os
import csv
from statistics import mean

csvpath = os.path.join("Resources", "budget_data.csv")

month = 0 # start the months at zero
total = 0 # start the total value at zero
# total_change = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999999]
month_of_change = []
net_change_list = []

with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row
    next(csvreader, None) # skips the header for calculations

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    month += 1
    total += int(first_row[1])
    prev_net = int(first_row[1])
    for row in csvreader:
        month+= 1        
        total+= int(row[1])
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        prev_net = int(row[1])
        if(net_change > greatest_increase[1]):
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    print("Total Months:",month)
    print("Total:","${:}".format(total))
    print("Average Change:","${:}".format(round(net_monthly_avg,2)))
    print("Greatest Increase in Profits:", greatest_increase[0],"${:}".format(greatest_increase[1]))
    print("Greatest Decrease in Profits:", greatest_decrease[0],"${:}".format(greatest_decrease[1]))
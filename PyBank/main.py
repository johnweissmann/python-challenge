import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
textpath = os.path.join("Analysis", "analysis.txt")

month = 0 # start the months at zero
total = 0 # start the total value at zero
net_change_list = []
greatest_increase = ["",0] # create an empty list with a value at index 1 that everything will be bigger than
greatest_decrease = ["",9999999999999999] # do the same for decrease but with a value that everyhting will be smaller than

with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # skips the header for calculations
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
    print("Total Months: ",month)
    print("Total: ","${:}".format(total))
    print("Average Change: ","${:}".format(round(net_monthly_avg,2)))
    print("Greatest Increase in Profits: ", greatest_increase[0],"${:}".format(greatest_increase[1]))
    print("Greatest Decrease in Profits: ", greatest_decrease[0],"${:}".format(greatest_decrease[1]))
    totalmonthssolution = ["Total Months: ",str(month)] 
    totalsolution = ["Total: ",str("${:}".format(total))]
    avgchangesolution = ["Average Change: ",str("${:}".format(round(net_monthly_avg,2)))]
    incsolution = ["Greatest Increase in Profits: ", str(greatest_increase[0])," ",str("${:}".format(greatest_increase[1]))]
    decsolution = ["Greatest Decrease in Profits: ", str(greatest_decrease[0])," ",str("${:}".format(greatest_decrease[1]))]
with open(textpath,"w") as txt:
    txt.writelines("Financial Analysis")
    txt.writelines("\n")
    txt.writelines("---------------------------")
    txt.writelines("\n")
    txt.writelines(totalmonthssolution)
    txt.writelines("\n")
    txt.writelines(totalsolution)
    txt.writelines("\n")
    txt.writelines(avgchangesolution)
    txt.writelines("\n")
    txt.writelines(incsolution)
    txt.writelines("\n")
    txt.writelines(decsolution)
    txt.writelines("\n")
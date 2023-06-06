import os #import dependencies
import csv

csvpath = os.path.join("Resources", "budget_data.csv") #create paths for external files
textpath = os.path.join("Analysis", "analysis.txt")

month = 0 # start the months at zero
total = 0 # start the total value at zero
net_change_list = [] #create an empty list for the net change
greatest_increase = ["",0] # create an empty list with a value at index 1 that everything will be bigger than
greatest_decrease = ["",9999999999999999] # do the same for decrease but with a value that everyhting will be smaller than

with open(csvpath, encoding="UTF-8") as csvfile: #open csv for reading
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # skips the header for calculations
    first_row = next(csvreader) #get the first row value 
    month += 1 #add a month so we get all months counted
    total += int(first_row[1]) #start with the total value of the first row
    prev_net = int(first_row[1]) #create a value that we can compare with to determine what the net change will be 
    for row in csvreader:
        month+= 1  #add a month for each row      
        total+= int(row[1]) #add each amount to the total for total value 
        net_change = int(row[1]) - prev_net 
        net_change_list.append(net_change)
        prev_net = int(row[1]) #get the net change by subtracting the previous value from the current one, add it to the net change list, and then reset the value
        if(net_change > greatest_increase[1]): #determine if greatest increase
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        if(net_change < greatest_decrease[1]): #determine if greatest decrease
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    print("Total Months: ",month)
    print("Total: ","${:}".format(total))
    print("Average Change: ","${:}".format(round(net_monthly_avg,2)))
    print("Greatest Increase in Profits: ", greatest_increase[0],"${:}".format(greatest_increase[1]))
    print("Greatest Decrease in Profits: ", greatest_decrease[0],"${:}".format(greatest_decrease[1]))
    
    #convert the results to lists so i can use the txt.writelists function
    totalmonthssolution = ["Total Months: ",str(month)] 
    totalsolution = ["Total: ",str("${:}".format(total))]
    avgchangesolution = ["Average Change: ",str("${:}".format(round(net_monthly_avg,2)))]
    incsolution = ["Greatest Increase in Profits: ", str(greatest_increase[0])," ",str("${:}".format(greatest_increase[1]))]
    decsolution = ["Greatest Decrease in Profits: ", str(greatest_decrease[0])," ",str("${:}".format(greatest_decrease[1]))]

#write the txt file for analysis
with open(textpath,"w") as txt:
    txt.writelines("Financial Analysis")
    txt.writelines("\n") #create a new line
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
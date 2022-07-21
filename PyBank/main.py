import os
import csv

#output file is git/pythonChallenge/PyBank/analysis/PyBankOutput.txt

#define the path to the csv file
csvpath = os.path.join('resources', 'budget_data.csv')

#create counters for the values needed. months, p&l, 
totalMonths = 0
totalProfitLoss = 0
value = 0
change = 0

#create lists to hold those values
dates = []
profits = []

#acccess the csv file and define what separates the data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #this will skip the header row
    firstRow = next(csvreader) 

    totalMonths += 1 #this is the same as totalMonths = totalMonths + 1

    totalProfitLoss += int(firstRow[1])
    value = int(firstRow[1])

    for row in csvreader:

        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        totalMonths += 1
        totalProfitLoss = totalProfitLoss + int(row[1])
        avgChange = sum(profits)/len(profits)

    greatestIncrease = max(profits)
    greatestIncIndex = profits.index(greatestIncrease)
    greatestIncDate = dates[greatestIncIndex]

    greatestDecrease = min(profits)
    greatestDecIndex = profits.index(greatestDecrease)
    greatestDecDate = dates[greatestDecIndex]

#printout the analyis

printoutput = (
    f"Financial Analysis\n"
    f"---------------------------------------------\n"
    f"Total Months: {str(totalMonths)}\n"
    f"Total: ${str(totalProfitLoss)}\n"
    f"Average change: ${str(round(avgChange,2))}\n"
    f"Greatest increase in profits: {greatestIncDate} (${str(greatestIncrease)})\n"
    f"Greatest decrease in profits: {greatestDecDate} (${str(greatestDecrease)})\n")

print(printoutput)    

#write the analysis to the output file
with open('analysis', 'PyBankoutput.txt', 'w') as f:
    f.write(
        f"Financial Analysis\n"
        f"---------------------------------------------\n"
        f"Total Months: {str(totalMonths)}\n"
        f"Total: ${str(totalProfitLoss)}\n"
        f"Average change: ${str(round(avgChange,2))}\n"
        f"Greatest increase in profits: {greatestIncDate} (${str(greatestIncrease)})\n"
        f"Greatest decrease in profits: {greatestDecDate} (${str(greatestDecrease)})\n")
    
#use this as template to send the analysis to the output file
#sourceFile = open('python.txt', 'w')
#print('Pretty cool, huh!', file = sourceFile)
#sourceFile.close()

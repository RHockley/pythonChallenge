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
avgChange = 0

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
        change = int(row[1]-value)
        profits.append(change)
        value = int(row[1])

        totalMonths += 1
        totalProfitLoss = totalProfitLoss + int(row[1])
        avgChange = sum(profits)/len(profits)

    greatestIncrease = max(profits)
    greatestDecrease = min(profits)

#use this as template to send the analysis to the output file
#sourceFile = open('python.txt', 'w')
#print('Pretty cool, huh!', file = sourceFile)
#sourceFile.close()

import os
import csv

#define the path to the csv file
csvPath = os.path.join('resources', 'election_data.csv')

#create lists needed
candidates = []
numVotes = []
percentVotes = []

#set counter for votes
totalVotes = 0

#read the csv
with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #this reads the header row

    for row in csvreader:
        totalVotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            numVotes.append(1)
        else:
            index = candidates.index(row[2])
            numVotes[index] += 1

        for votes in numVotes:
            percentage = (votes/totalVotes) * 100
            percentage = round(percentage)
            percentage = "%.3f" % percentage
            percentVotes.append(percentage)

        winner = max(numVotes)
        index = numVotes.index(winner)
        winningCandidate = candidates[index]

print("Election Results")
print("----------------------------------------")
print(f"Total votes: {str(totalVotes)}")
print("----------------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentVotes[i])} ({str(numVotes[i])}))")
print("----------------------------------------")
print(f"Winner: {winningCandidate}")
print("----------------------------------------")

lines = ['Election Results', 
        '----------------------------------------',
        f'Total Votes: {str(totalVotes)}', 
        '----------------------------------------', 
        f'Winner: {winningCandidate}']
        
with open('analysis/PyPollOutput.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
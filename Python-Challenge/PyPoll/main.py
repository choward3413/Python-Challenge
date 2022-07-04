import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
outputFile = os.path.join("Analysis", "electionAnalysis.txt")

totalVotes = 0
candidates = []
candidateVotes = {}
winCount = 0
winningCandidate = ()


# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    firstRow = next(csv_reader)

    totalVotes +=1
    

    for row in csv_reader:
        totalVotes +=1
          #check to see if candidate is in list
        if row[2] not in candidates:
          #add to list
             candidates.append(row[2])
        #add to dictionary also
             candidateVotes[row[2]] = 1

        else:
            candidateVotes[row[2]] +=1


#print(candidateVotes)

voterOutput = ""
for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votesPercent =(float(votes) / float(totalVotes)) *100.00

    voterOutput += f"{candidate} : {votesPercent:.3f}% ({votes:,})\n"

    if votes > winCount:
        winCount = votes
        winningCandidate = candidate

    winningCandidateOutput = f"winner: {winningCandidate}\n-----------------"    

    

output = (
        f"\nElection Results \n"
        "-----------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        "--------------------------\n"
        f"{voterOutput}"
        "---------------------------\n"
        f"Winner: {winningCandidate}\n"
        "---------------------------\n"



)

print(output)

with open(outputFile, "w") as textFile:
    textFile.write(output)


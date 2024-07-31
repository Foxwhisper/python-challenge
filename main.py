"""
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote
"""

#import files to use in this project
import os
import csv

#path for csv file and text file
election_data_csv = os.path.join(".","Resources", "election_data.csv")
analysis_txt = os.path.join(".", "Analysis", "election_analysis.txt")

#variables
candidates = []
votes = []

#open the cvs file
with open(election_data_csv, 'r') as file:
    csvreader=csv.reader(file,delimiter=",")
    
    header = next(csvreader)
    
    for row in csvreader:
        
        if row[2] in candidates:
        	#count up 1
            index = candidates.index(row[2])
            votes[index] += 1
#is this the beginning 
        else:
        	index = len(candidates)
        	candidates.append(row[2])
        	votes.append(1)

#determine the winner
winner_index = votes.index(max(votes))


print('Election Results\n')
print('--------------------------\n')
print(f'Total Votes: {sum(votes)}\n')
print('--------------------------\n'
	)

#votes received by person and the percent of votes each candidate won
#and the winner
#print the results
for x in range(0,len(candidates)):
	print(f'{candidates[x]}: {round(votes[x] / sum(votes) * 100,3)}% ({votes[x]})')
print('--------------------------\n')
print(f'Winner: {candidates[winner_index]}\n')

with open(analysis_txt, 'w', newline='') as output:
	output.write(
		'Election Results\n'
		'--------------------\n'
		f'Total Votes: {sum(votes)}\n'
		'--------------------\n'
	)
	for x in range(0,len(candidates)):
		output.write(f'{candidates[x]}: {round(votes[x] / sum(votes) * 100,2)}% ({votes[x]})\n')
	output.write(
		'--------------------\n'
		f'Winner: {candidates[winner_index]}\n'
		'--------------------\n'
	)	
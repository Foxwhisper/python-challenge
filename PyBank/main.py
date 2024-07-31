"""
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#print the analysis to the terminal and export a text file with the results
"""

#import files to use in this project
import os
import csv

#path for csv file and text file
budget_data_csv = os.path.join(".","Resources", "budget_data.csv")
analysis_txt = os.path.join(".", "Analysis", "budget_analysis.txt")

#declare variables
month = 0
grand_total = 0
previous_value = 0
changes = []
average_change = 0
total_change = 0
low_change = 0
high_change = 0
low_month = ["",0]
high_month = ["",0]



#open the cvs file
with open(budget_data_csv, 'r') as file:
    csvreader=csv.reader(file,delimiter=",")
    header = next(csvreader)
    
    #Loops

    for row in csvreader:
        current_value = int(row[1])
        #how to count the amount of months
        month += 1
        grand_total += current_value


#profit/losses
        if previous_value != 0:
            change = current_value - previous_value
            changes.append(change)

            if change > high_change:
                high_change = change
            if change > high_month[1]:
                high_month[0] = row[0]
                high_month[1] = change

            elif change < low_change:
                low_change = change
            elif change < low_month[1]:
                low_month[0] = row[0]
                low_month[1] = change

        previous_value = current_value


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    average_change = sum(changes) / len(changes)


# create the output
print('Financial Analysis\n', '\r')
print('--------------------------\n', '\r'
        f'Total Month: {month}\n'
        f'Total: ${grand_total}\n'
        f'Average Change: ${round(average_change,2)}\n')
print(f'Greatest Increase in Profits: {high_month[0]} (${high_month[1]})\n'
    f'Greatest Decrease in Profits: {low_month[0]} (${low_month[1]})\n')


with open(analysis_txt, 'w', newline='') as output:
    output.write('PyBank Results\n')




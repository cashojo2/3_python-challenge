# PyBank challenge - financial data set

# import modules
import os
import csv

# set up variables / objects
months = 0
profits = 0
dates = []
changes = []

# set csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# use csv module to open and read file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # create previous row variable for later use
    pre_row = next(csvreader)
    
    # adjustments to compensate for previous row in calculations
    months = months + 1
    profits = profits + int(pre_row[1])
    # dates.append(pre_row[0])

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        # add up total number of months ie. # of rows
        months = months + 1

        # net total amount of "Profit/Losses" over the entire period (ie. running total / sum)
        profits = profits + int(row[1])

        # create a list of the change in the "Profit/Losses" column, append value for each row
        changes.append(int(row[1]) - int(pre_row[1]))

        #create list of the dates
        dates.append(row[0])

        # adjust previous row variable for next iteration
        pre_row = row


# calculate average change using list of changes created in loop
avg_change = sum(changes) / len(changes)
avg_change = round(avg_change, 2)

# dtm greatest increase in profits (amount) by looping through list of changes
greatest_inc = -10000
for x in changes:
    if x > greatest_inc:
        greatest_inc = x

# dtm greatest decrease in profits (amount)
greatest_dec = 100000
for x in changes:
    if x < greatest_dec:
        greatest_dec = x

# use the index of greatest_inc from changes list to dtm the corresponding date from dates list
index1 = changes.index(greatest_inc)
date1 = dates[index1]

# use the index of greatest_dec from changes list to dtm the corresponding date from dates list
index2 = changes.index(greatest_dec)
date2 = dates[index2]

# return results in terminal
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(profits))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + date1 + " ($" + str(greatest_inc)+ ")")
print("Greatest Decrease in Profits: " + date2 + " ($" + str(greatest_dec)+ ")")

# return results in text file

# set the output path
output_path = os.path.join("analysis", "pybank_results.txt")

# open the file 
with open(output_path, 'w') as output_file:
    output_file.write('Financial Analysis')
    output_file.write('\n')
    output_file.write('-------------------------------------')
    output_file.write('\n')
    output_file.write('Total Months: ' + str(months))
    output_file.write('\n')
    output_file.write('Total: $' + str(profits))
    output_file.write('\n')
    output_file.write('Average Change: $' + str(avg_change))
    output_file.write('\n')
    output_file.write('Greatest Increase in Profits: ' + date1 + ' ($' + str(greatest_inc)+ ')')
    output_file.write('\n')
    output_file.write('Greatest Decrease in Profits: ' + date2 + ' ($' + str(greatest_dec)+ ')')
    
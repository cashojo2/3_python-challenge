import os
import csv

# set up variables / objects
total_votes = 0
candidates = {}

# set csv file path
csvpath = os.path.join('Resources', 'election_data.csv')

# use csv module to open and read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first
    csv_header = next(csvreader)

    # read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        # use conditional to count votes
        # dict: key = name (str), value = vote tally (int)
        # if csv row candidate name already in dict, then:
        if candidate_name in candidates:
            # update vote tally by adding one
            candidates[candidate_name] = candidates[candidate_name] + 1
            # if not, add new key-value pair entry to dict for new candidate
        else:
            candidates[candidate_name] = 1


# determine the winner
winner = max(candidates, key=candidates.get)


# Output results to the terminal
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------------")
# calculate percentages and print
for candidate_name in candidates:
    percentage = round((candidates[candidate_name] / total_votes *100), 3)
    print(candidate_name + ": " + str(percentage) + "% (" + str(candidates[candidate_name]) + ")")
print("--------------------------------")
print("Winner: " + winner)


# return results in text file

# set the output path
output_path = os.path.join("analysis", "pypoll_results.txt")

# open the file 
with open(output_path, 'w') as output_file:
    output_file.write("Election Results")
    output_file.write('\n')
    output_file.write("--------------------------------")
    output_file.write('\n')
    output_file.write("Total Votes: " + str(total_votes))
    output_file.write('\n')
    output_file.write("--------------------------------")
    output_file.write('\n')
    for candidate_name in candidates:
        percentage = round((candidates[candidate_name] / total_votes *100), 3)
        output_file.write(candidate_name + ": " + str(percentage) + "% (" + str(candidates[candidate_name]) + ")")
        output_file.write('\n')
    output_file.write("--------------------------------")
    output_file.write('\n')
    output_file.write("Winner: " + winner)

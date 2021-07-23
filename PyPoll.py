# Objectives:
# Total no. votes cast
# List of candidates who received votes
# Total votes per candidate
# % of votes per candidate
# Who won the election

# import dependencies
import csv
import os

# initialize variables
total_votes = 0
candidate_options


# read data
file = os.path.join("Resources","election_results.csv")
with open(file) as election_data:

    # perform analysis
    # read file
    file_reader = csv.reader(election_data)

    # skip and print header row
    headers = next(file_reader)
    print(headers)

    # extract data
    for row in file_reader:
        total_votes += 1

    # print results
    print(f'\nTotal Votes: {total_votes}\n')


# write results
# results_file = os.path.join("analysis","election_analysis.txt")
# with open(results_file, "w") as election_analysis:
   # election_analysis.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson\n")

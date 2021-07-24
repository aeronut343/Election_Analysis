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
candidate_options = []
candidate_votes = {}
winning_count = 0
winning_percentage = 0.0
winning_candidate = ""

# initialize file paths
file = os.path.join("Resources","election_results.csv")
results_file = os.path.join("analysis","election_analysis.txt")

# read data
with open(file) as election_data:

    # perform analysis
    # read file
    file_reader = csv.reader(election_data)

    # skip header row
    headers = next(file_reader)

    # extract data
    for row in file_reader:
        # increase vote counter
        total_votes += 1

        #gather candidate name
        candidate_name = row[2]

        # add candidate to the list of options if they are not already
        if candidate_name not in candidate_options:
            # add the candidate to the list
            candidate_options.append(candidate_name)

            # start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # increment candidate vote tally
        candidate_votes[candidate_name] += 1
with open(results_file, "w") as txt_file:
    # print and write election results
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # determine vote percentages
    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        # print and write candidate results
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # determine winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    # print and write winning candidate summary
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

# print results
# print(f'\nTotal Votes: {total_votes}\n')
# print(f'\nCandidate options are: {candidate_options}\n')
# print(f'\n{candidate_options[0]} received {candidate_votes[candidate_options[0]]} votes\n')
# print(f'\n{candidate_options[1]} received {candidate_votes[candidate_options[1]]} votes\n')
# print(f'\n{candidate_options[2]} received {candidate_votes[candidate_options[2]]} votes\n')


# write results
# results_file = os.path.join("analysis","election_analysis.txt")
# with open(results_file, "w") as election_analysis:
   # election_analysis.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson\n")

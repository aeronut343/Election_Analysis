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
county_options = []
county_votes = {}
winning_count = 0
winning_percentage = 0.0
winning_candidate = ""
highest_turnout = 0
highest_turnout_county = ""
highest_turnout_percent = 0.0

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

        # -----CANDIDATE SECTION-----
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

        # -----COUNTY SECTION-----
        # gather county name
        county_name = row[1]

        # add county to list if not present
        if county_name not in county_options:
            # add county to options
            county_options.append(county_name)

            # start tracking county vote tally
            county_votes[county_name] = 0

        # increment county vote tally
        county_votes[county_name] += 1


with open(results_file, "w") as txt_file:
    # print and write election results
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # -----CANDIDATE SECTION-----
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

    #-----COUNTY SECTION-----
    for county in county_options:
        cvotes = county_votes[county]
        cvote_percent = float(cvotes) / total_votes *100

        # print and write county results
        county_results = (f"{county}: {cvote_percent:.1f}% ({cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        # determine highest voter turnout
        if (cvotes > highest_turnout) and (cvote_percent > highest_turnout_percent):
            highest_turnout = cvotes
            highest_turnout_percent = cvote_percent
            highest_turnout_county = county
        
    # create, print and write highest turnout summary
    highest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_turnout_county}\n"
        f"-------------------------\n")

    print(highest_turnout_summary)
    txt_file.write(highest_turnout_summary)
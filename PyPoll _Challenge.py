# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter for candidates and counties
total_votes_candidate = 0
total_votes_counties = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
#county options and county votes
counties_options = []
counties_votes = {}
# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0
#track the winning county, vote count and percentage
largest_county = 0
largest_county_count = 0
largest_percent_county = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count for candidates and county
        total_votes_candidate += 1
        total_votes_counties +=1
        # Get the candidate name from each row
        candidate_name = row[2]
        #get the county name from each row
        county_name = row [1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        #if the county does not match any element in list, add the county to the list
        if county_name not in counties_options:
            #add the county name to the county list
            counties_options.append(county_name)
            # being tracking the county voter turn out in the dictionary
            counties_votes[county_name] = 0
        # add a vote to the county count
        counties_votes[county_name] +=1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {total_votes_candidate:,}\n"
        f"-----------------------------------\n\n"
        f"\nCounty Votes:\n" )
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #get county votes count and percent for county
    for i in counties_votes:
        county_votes = counties_votes[i]
        county_vote_percent = float(county_votes) / float(total_votes_counties) * 100
        county_results = (
             f"{i}: {county_vote_percent:.1f}% ({county_votes:,})\n")
        #print each county vote percent and count to terminal
        print(county_results)
        #save the county results to the text file
        txt_file.write(county_results)
        #determine county with largest turnout
        if (county_votes > largest_county_count) and (county_vote_percent > largest_percent_county):
            largest_count_county = county_votes
            largest_county = i
            largest_percent_county = county_vote_percent

    # Print the largest county turnout results to the terminal.
    largest_county_turnout = (
        f"-----------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-----------------------------------\n")
    print(largest_county_turnout)
    # Save the largest county turnout results to text file
    txt_file.write(largest_county_turnout) 
        
    #get candidate votes count and percent
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes_candidate) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count_candidate) and (vote_percentage > winning_percentage_candidate):
            winning_count_candidate = votes
            winning_candidate = candidate
            winning_percentage_candidate = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"Winning Percentage: {winning_percentage_candidate:.1f}%\n"
        f"-----------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

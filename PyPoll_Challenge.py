#
#
#
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# challenge step 2 initialize string to hold county name for county with largest turnout
largest_county_turnout = ""
# initialize variable to hold number of votes of the largest county that had the largest turnout
largest_county_count = 0


# 1: Create a county list and county votes dictionary.
#challenge step 1 initialize count list
county_options = []
# initialize counties dictionary to hold county as key and votes cast for each county as values
county_votes = {}

# 2: Track the largest county and county voter turnout.
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        # challenge step 3 write script that gets the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        
        # step 4a check if county name acquired is in the counties list
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            # challenge step 4b add the county to the counties list if not present
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            # challenge step 4c begin counting that county’s votes
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        # challenge step 5 add vote to county’s vote count as it loops
        county_votes[county_name] += 1

 
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    # challenge step 6a loop through to get county from county dictionary
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        # challenge step 6b initialize variable to hold county’s votes retrieved from county dictionary
        county_individual_votes = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        # challenge step 6c alculate county’s votes as percentage of total votes
        county_vote_percentage = float(county_individual_votes) / total_votes * 100

        # 6d: Print the county results to the terminal.
        # challenge step 6d print current county, its percentage of total votes, and its total votes
        county_results = (f"Total County Votes: {county_name}: {county_vote_percentage:.1f}% {county_individual_votes:,}\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        # challenge step 6f determine country with largest vote count and add it to variable largest_county_count
        if (county_individual_votes > largest_county_count):
            largest_county_count = county_individual_votes
            winning_county = (
            f"-------------------------\n"
            f" Largest County Turnout: {county_name}\n"
            f"-------------------------\n")

    # 7: Print the county with the largest turnout to the terminal.
    print(winning_county)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


# Get the total votes cast for the election.

# Assign a variable for the file to load and the path.
file_to_load = '/Users/joshzaragoza/Desktop/Data Bootcamp/Election_Analysis/Resources/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Close the file.
election_data.close()
import pandas as pd
from pathlib import Path

#file path
file = Path("Resources/election_data.csv")

election_df = pd.read_csv(file)

print("Election Results")

print("-"*26)

#Total Votes
total_votes= len(election_df["Ballot ID"])

print(f"Total Votes: {total_votes}")
print("-"*26)

#list of who received votes
candidates = election_df["Candidate"].unique()

# vote counts
votes = election_df["Candidate"].value_counts().reset_index()
votes.columns = ["Candidate", "Vote Count"]

#percentage
votes["Percentage"] = (votes["Vote Count"] / total_votes) * 100

# winner
winner = votes.loc[votes["Vote Count"].idxmax(), "Candidate"]

#print candidates with percentage and vote count

for index, row in votes.iterrows(): 
    print(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})")

print("-"*26)
print(f"Winner: {winner}")
print("-"*26)


# results go here
output_file = "C:\\Users\\gurja\\OneDrive\\pandas_challenge\\PyPoll\\Analysis\\Results_PyPoll.txt"

# write mode
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-" * 26 + "\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-" * 26 + "\n")
    for index, row in votes.iterrows():
        candidate_info = f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})"
        file.write(candidate_info + "\n")
    file.write("-" * 26 + "\n")
    file.write(f"Winner: {winner}\n")
    file.write("-" * 26 + "\n")

print(f"Results exported to {output_file}")
#prerequisite library
import pandas as pd
from pathlib import Path

#file path
file = Path("C:\\Users\gurja\OneDrive\pandas_challenge\PyBank\Resources/budget_data.csv")

budget_df = pd.read_csv(file)

# I see now that i have accessed the csv properly
print(budget_df.head())


print(" Financial Analysis")

#I can multiple it, its faster
print("-"*26)

#total month calculation
months = budget_df["Date"].nunique()

print(f"Total Months: {months}")

#net profit/loss
net_profit = budget_df["Profit/Losses"].sum()

print("Total: $" + str(net_profit))

#change in profit/loss, then average 
budget_df["change"]= budget_df["Profit/Losses"].diff()
avg_change = budget_df["change"].mean()

print("Average Change: " + str(avg_change))

#greatest increase in profits
great_increase = budget_df["change"].max()
index = budget_df["change"].idxmax()
date = budget_df.loc[index, "Date"]

print("Greatest Increase in Profit: $" + str(great_increase) + " " + str(date))

#greatest derease in profits
great_decrease = budget_df["change"].min()
index_two = budget_df["change"].idxmin()
date_two = budget_df.loc[index_two, "Date"]

print("Greatest Increase in Profit: $" + str(great_decrease) + " " +str(date_two))

output_file = r"C:/Users/gurja/OneDrive/pandas_challenge/PyBank\Analysis/Results.txt"

# export to text file
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-" * 26 + "\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: {avg_change}\n")
    file.write(f"Greatest Increase in Profit: ${great_increase} ({date})\n")
    file.write(f"Greatest Decrease in Profit: ${great_decrease} ({date_two})\n")

# Print a message indicating that the results have been exported to the text file
print("Results exported to", output_file)
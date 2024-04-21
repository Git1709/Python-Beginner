import pandas as pd

# Given dataset (sample data)
data = {
    "Person": list(range(33, 61)),
    "Birthdate": [
        "November 6, 2000", "November 21, 2000", "December 23, 2000", "December 7, 2000",
        "January 18, 2000", "January 4, 2000", "February 9, 2000", "February 1, 2000",
        "February 18, 2000", "March 7, 2000", "April 15, 2000", "March 1, 2000",
        "May 31, 2000", "April 3, 2000", "May 29, 2000", "May 14, 2000",
        "June 25, 2000", "June 11, 2000", "July 9, 2000", "July 21, 2000",
        "September 20, 2000", "August 18, 2000", "September 1, 2000",
        "October 19, 2000", "October 5, 2000", "October 15, 2000",
        "November 2, 2000", "November 15, 2000"
    ]
}

# Create a DataFrame from the given data
df = pd.DataFrame(data)

# Convert birthdates to datetime objects
df["Birthdate"] = pd.to_datetime(df["Birthdate"])

# Filter for Tuesdays
tuesday_birthdays = df[df["Birthdate"].dt.day_name() == "Tuesday"]

# Count the number of people with Tuesday birthdays
count_tuesday_birthdays = len(tuesday_birthdays)

print(f"Number of people born on a Tuesday: {count_tuesday_birthdays}")

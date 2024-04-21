def create_points_table(matches):
    """
    Creates the IPL points table based on match results.

    Args:
        matches: A list of strings, where each string represents a round-robin
            match outcome. Each match outcome is a comma-separated string where
            the first team is the winner, and all other teams are losers.

    Returns:
        A list of strings representing the points table in descending order
            of wins.
    """

    # Initialize a dictionary to store wins for each team
    team_wins = {team: 0 for team in ["CSK", "DC", "KKR", "MI", "PK", "RR", "RCB", "SH"]}

    # Iterate through each match result
    for match in matches:
        winner, *losers = match.split(",")
        team_wins[winner] += len(losers)  # Increment winner's score by the number of losers

    # Sort teams by wins (descending) and then alphabetically
    sorted_teams = sorted(team_wins.items(), key=lambda x: (-x[1], x[0]))

    # Create the points table string
    points_table = [f"{team}:{wins}" for team, wins in sorted_teams]
    return points_table

# Get match data from user input
print("")
matches = []
for _ in range(8):  # Adjusted to loop 8 times
    match_result = input().strip()
    matches.append(match_result)

# Create and print the points table
points_table = create_points_table(matches)
for row in points_table:
    print(row)

# Volleyball Team Performance Analysis

This Python script collects information about volleyball matches, including the team's points, sets won/lost, match outcomes, and calculates various statistics.

## Variables and Accumulators
- `totalPointsWon`: Total number of points won from all matches.
- `totalPointsLose`: Total number of points lost in all matches.
- `matchWonCount`: Counter for matches won.
- `matchLoseCount`: Counter for matches lost.
- `pointsPerMatchWon`: Total points earned for one match.
- `pointsPerMatchLose`: Total points lost for one match.
- `pointsPerSetWon`: Points earned for one set won.
- `pointsPerSetLose`: Points lost for one set lost.
- `setsWonPerMatch`: Number of sets won in one match.
- `setsLosePerMatch`: Number of sets lost in one match.
- `totalSetsWon`: Total number of sets won in all matches.
- `totalSetsLose`: Total number of sets lost in all matches.
- `fiveSetsMatchCount`: Number of matches finishing in 5 sets (3-2).
- `threeSetsMatchWonCount`: Number of matches finishing in 3 sets (3-0).
- `wonMatchesCount`: Counter for matches won without losing a set.
- `loseMatchesCount`: Counter for matches losing without winning a set.
- `differenceBiggest`: The biggest point difference in one match.
- `totalSetsPlayed`: Total number of sets played in all matches.
- `differenceMatch`: The match with the biggest won-lose point difference.
- `biggestDifferenceMatch`: The name of the opposite team in the match with the biggest difference.

## User Input and Calculation
- The script prompts the user to enter the number of matches the team played.
- For each match, the script collects information about points won and lost for each set. It calculates various statistics, such as the total points, sets won/lost, match outcomes, and more.
- The script identifies matches that finished in 3 sets or 5 sets, determines match outcomes, and calculates averages and percentages.

## Results and Analysis
- After collecting information for all matches, the script calculates and prints various results, including total points won/lost, averages, match outcomes, and the match with the biggest point difference.

## Note
- The script assumes valid inputs and doesn't handle invalid inputs explicitly. Additional input validation could be added if needed.

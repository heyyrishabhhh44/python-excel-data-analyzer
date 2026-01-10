import csv

# Store all scores for analysis
scores = []

# Read CSV file row by row
# Convert score values to integers
# Append them for calculation

# Open and read a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        print(row)
        scores.append(int(row[1]))

# Calculate basic statistics
total_score = sum(scores)
average_score = total_score / len(scores)

print("Total Score:", total_score)
print("Average Score:", average_score)

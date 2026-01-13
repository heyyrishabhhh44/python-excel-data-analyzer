# Read numbers from a file and generate summary statistics

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


def generate_summary(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum


numbers = read_numbers_from_file('numbers.txt')
total, average, maximum, minimum = generate_summary(numbers)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

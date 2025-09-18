# python program to read from csv file and prints top scorers

import csv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

# Function to get top N scorers from the data
def get_top_scorers(data, top_n=3):
    # Assuming the first row is the header
    header = data[0]
    scores_index = header.index('Score')
    name_index = header.index('Name')
    
    # Extracting names and scores, converting scores to float for comparison
    scores = [(row[name_index], float(row[scores_index])) for row in data[1:]]
    
    # Sorting by score in descending order and getting top n
    top_scorers = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n] # key=lambda x: x[1] → tells sorted to sort by the second item (score) in the tuple otherwise it will sort by name (first item)
    
    return top_scorers

# Example usage
data = read_csv('example.csv')
top_scorers = get_top_scorers(data, top_n=3)
print(f"Top 3 Scorers: {top_scorers}")
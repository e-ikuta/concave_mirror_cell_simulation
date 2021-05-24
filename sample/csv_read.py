import csv

# read
with open('sample.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    print(l)

import csv

l = [[1,2,3],[4,5,6]]

with open('sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)

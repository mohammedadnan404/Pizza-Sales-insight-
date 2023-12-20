import csv

with open('D:/pizza_sales portfolio project/pizzas.csv', 'r') as infile, open('D:/pizza_sales portfolio '
                                                                              'project/New_pizzas.csv', 'w',
                                                                              newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    for row in reader:
        writer.writerow(row)

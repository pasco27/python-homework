# I've been provided budget_data.csv for analysis. 
# Data contains two columns: Date and P/L
# The following is a script analyzing the data. 


# import libraries needed
import os
import csv

# print a header for table cleanliness 
print("-"*27)
print("Financial Analysis")
print("-"*27)


# import the csv file 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
# I used this block of code to print the csv, checking format.
 #   for row in csv_reader:
 #       print(row)
 # 
 # I see there are two columns, and that the first row is a header titles 'Date' & 'Profit / Loss'    
 # Knowing that the first row is a header and seeing that the column1 data is monthly,
 # the total number of months in the data:
  
    csv_header = next(csv_reader)  # skips header in the count.
    data = list(csv_reader)
    row_count = len(data) 
    print(f'Total Months : {row_count}')

# net P/L for the dataset is the summation of that column 

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)  # again skipping header for the calc
    total_pl = 0
    for row in csv_reader: 
        total_pl += float(row[1])
        formatted_total_pl = "{:.2f}".format(total_pl)
    print(f'Total P/L : ${total_pl}')

# average month/month P/L over entire dataet 

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader) 
    previous_row = 0 
    for row in csv_reader:
        difference = float(row[1]) - previous_row
        previous_row = float(row[1])
        avg_difference = (difference/(row_count))
        formatted_avg_diff = "{:.2f}".format(avg_difference) 
    print(f'Average Change: ${formatted_avg_diff}')
## I'm trying to round this number but it will not??! 


# greatest increase in profits, with date and amount
# It may help here to append another column?? 
#### can I append "difference 

# greatest decrease in losses, with date and amount 


# export a text file with results 
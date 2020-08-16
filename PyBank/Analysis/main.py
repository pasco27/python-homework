# I've been provided budget_data.csv for analysis. 
# Data contains two columns: Date and P/L
# The following is a script analyzing the data. 


# import libraries needed
import os
import csv


# import the csv file 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
# I used this block of code to print the csv, checking format.
 #   num_rows = 0
 #   for row in csv_reader:
 #       num_rows += 1
 #       print(num_months)
 # 
 # I see there are two columns, and that the first row is a header titles 'Date' & 'Profit / Loss'    
 # Knowing that the first row is a header and seeing that the column1 data is monthly,
 # the total number of    
    
    data = list(csv_reader)
    row_count = len(data)
    num_months = row_count - 1   
    print(f'Total Months = {num_months}')


######## --- csvreader.__next__()


## analyze the total P/L for the entire dataset 
# net total P/L over entire dataset 


# average month/month P/L over entire dataet 


# greatest increase in profits, with date and amount


# greatest decrease in losses, with date and amount 




# export a text file with results 







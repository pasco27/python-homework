# I've been provided election_data.csv for analysis.
# Data contains three columns: Voter ID, County, and Candidate.
# The following is a script analyzing the data.

# import libraries needed
import os
import csv

f = open("pypoll_output.txt", "a")

# print a header for table cleanliness 
print("-"*27, file = f)
print("Election Results", file = f)
print("-"*27, file = f)

# print a the csv file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')


with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    #for i,row in enumerate(csv_reader):
     #   print(row)
      #  if(i >= 5):
       #     break

    # or move these up above 18
    candidates = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []
    row_count = 0
    
    for row in csv_reader:
        candidates.append(row[2])
        row_count += 1 

    print(f'Total Votes: {row_count}', file = f)

    print("-"*27, file = f)

    for row in candidates:
        if row == "Khan":
            Khan.append(row[0])
            Total_Khan = len(Khan)
            Khan_percentage = (Total_Khan / row_count)*100
       
        if row == "Correy":
            Correy.append(row[0])
            Total_Correy = len(Correy)
            Correy_percentage = (Total_Correy / row_count)*100
    
        if row == "Li":
            Li.append(row[0])
            Total_Li = len(Li)
            Li_percentage = (Total_Li / row_count)*100
    
        if row == "O'Tooley":
            OTooley.append(row[0])
            Total_OTooley = len(OTooley)
            OTooley_percentage = (Total_OTooley / row_count)*100

    totals = [Total_Khan, Total_Correy, Total_Li, Total_OTooley]
    winner = max(totals)


    print(f'Khan: {"{:,.2f}".format(Khan_percentage)}% ({Total_Khan})', file = f)
    print(f'Correy: {"{:,.2f}".format(Correy_percentage)}% ({Total_Correy})', file = f)
    print(f'Li: {"{:,.2f}".format(Li_percentage)}% ({Total_Li})', file = f)
    print(f'OTooley: {"{:,.2f}".format(OTooley_percentage)}% ({Total_OTooley})', file =f)

    print("-"*27, file = f)

    if winner == Total_Khan:
        print("Winner: Khan", file = f)
    if winner == Total_Correy:
        print("Winner: Correy", file = f)
    if winner == Total_Li:
        print("Winner: Li", file = f)
    if winner == Total_OTooley:
        print("Winner: OTooley", file = f)

    print("-"*27, file = f)



### with open(outpath, 'w') as csvfile:
### I know I'm "probably" supposed to print with this function
### Could not get it to work

   






##########   
   
 #   cn = Counter(candidates)
 #   for k,v in cn.items:
 #       print("[{}][{}].format(k,v)

 # ^^^^ This counter would've been badass had it worked! 


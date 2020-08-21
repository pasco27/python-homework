# I've been provided election_data.csv for analysis.
# Data contains three columns: Voter ID, County, and Candidate.
# The following is a script analyzing the data.

# import libraries needed
import os
import csv


# print a header for table cleanliness 
print("-"*27)
print("Election Results")
print("-"*27)

# print a the csv file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')

    #for i,row in enumerate(csv_reader):
     #   print(row)
      #  if(i >= 5):
       #     break

    csv_header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)
    print(f'Total Votes: {row_count}')

    print("-"*27)


candidates = []
Khan = []
Correy = []
Li = []
OTooley = []

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    for row in csv_reader:
        candidates.append(row[2])

    for row in candidates:
        if row == "Khan":
            Khan.append(row[0])
            Total_Khan = len(Khan)
            Khan_percentage = (Total_Khan / row_count)*100
    
  
    for row in candidates:   
        if row == "Correy":
            Correy.append(row[0])
            Total_Correy = len(Correy)
            Correy_percentage = (Total_Correy / row_count)*100
        
    for row in candidates:
        if row == "Li":
            Li.append(row[0])
            Total_Li = len(Li)
            Li_percentage = (Total_Li / row_count)*100
      
    for row in candidates:
        if row == "O'Tooley":
            OTooley.append(row[0])
            Total_OTooley = len(OTooley)
            OTooley_percentage = (Total_OTooley / row_count)*100

    totals = [Total_Khan, Total_Correy, Total_Li, Total_OTooley]
    winner = max(totals)


    print(f'Khan: {Khan_percentage}% ({Total_Khan})')
    print(f'Correy: {Correy_percentage}% ({Total_Correy})')
    print(f'Li: {Li_percentage}% ({Total_Li})')
    print(f'OTooley: {OTooley_percentage}% ({Total_OTooley})')

    print("-"*27)

    print(f'Winner: {winner}')

    print("-"*27)

### now need to work export to txt file and printing winner 

   






   
   
 #   cn = Counter(candidates)
 #   for k,v in cn.items:
 #       print("[{}][{}].format(k,v)

 # ^^^^ This counter would've been badass had it worked! 


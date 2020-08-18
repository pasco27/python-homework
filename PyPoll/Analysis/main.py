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

#with open(csvpath, 'r') as csvfile:
#    csv_reader = csv.reader(csvfile, delimiter = ',')

    #for i,row in enumerate(csv_reader):
     #   print(row)
      #  if(i >= 5):
       #     break

#    csv_header = next(csv_reader)
#    data = list(csv_reader)
#    row_count = len(data)
#    print(f'Total Votes: {row_count}')

#    print("-"*27)


    #did some studying after my first program -- I think I can use lists as a useful item here.
voter_id = []
county = []
candidates = []

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    for row in candidates:
        totals(row[0])
     #   print(len(candidates))  <- this prints the whole list numerically, not just the total length

     #   candidates.sort(key = len)
     #   print(candidates)              <- this prints every line name 

  #  for name in zip(candidates):
   #     print(name)




    #for now, we're really only working with the candidate list

 #   from collections import Counter
 #   Counter(candidates)


    #candidate.sort()
    #-or-
 #   sorted(candidates)


   #for candidate in candidates:
   #    print(candidate)






    # need to make a new list with all of these
    # then sort 
    # can interate over each to pull the 

    # can loop through each list; each name would be counted 


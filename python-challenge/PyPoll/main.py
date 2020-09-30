# Dependencies
import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

#Specify the file to write to
outPath = os.path.join("analysis", "poll.csv")

#Open the file using "write" mode.  Specify the variable to hold the content
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader, None)
    #Find the number of months.  Subtracting the first row because it's the header
    votes = len(list(csvreader))

    #






    
with open(outPath, 'w') as datafile:
    
    #initialize the csv.writer
    csvwriter = csv.writer(datafile, delimiter=",")

    #write the first row (column headers)
    csvwriter.writerow(["Election Results"])

    #write the second row
    csvwriter.writerow(["Total Votes:", votes])



#Create variables for total months and calculate the total months from the csv file
# vTotMonths

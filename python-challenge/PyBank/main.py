# Dependencies
import os
import csv

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

#Specify the file to write to
outPath = os.path.join("..", "analysis", "bank.csv")

#Open the file using "write" mode.  Specify the variable to hold the content
with open(bank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimeter=",")
    for row in csvreader:
        #Find the total number of months

    
with open(outPath, 'w') as datafile:
    
    #initialize the csv.writer
    csvwriter = csv.writer(datafile, delimeter=',')

    #write the first row (column headers)
    csvwrite.writerow(["Date", "Profit/Losses"])

    #write the second row
    


#Create variables for total months and calculate the total months from the csv file
TotMonths






# Print a statement displaying the total months
print(f"Total Months: + {TotMonths}")



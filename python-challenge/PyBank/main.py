# Dependencies
import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

#Specify the file to write to
outPath = os.path.join("analysis", "bank.csv")

#Open the file using "write" mode.  Specify the variable to hold the content
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader, None)
    #Find the number of months.  Subtracting the first row because it's the header
    months = len(list(csvreader))-1

    #Sum all of the data in the second column
   # money = int(csvreader[1])
    #total = sum(money)

    #Find the greatest increase in profits
    #dateinc will be the date that the greatest increase in profits occurs
    #amountinc variable will represent the amount of the greatest increase in profits

    #Find the greatest decrease in profits
    #datedec will be the date that the greatest decrease in profits occurs
    #amountdec variable will represent the amount of the greatest decrease in profits



    
with open(outPath, 'w') as datafile:
    
    #initialize the csv.writer
    csvwriter = csv.writer(datafile, delimiter=",")

    #write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])

    #write the second row
    csvwriter.writerow(["Total Months:", months])

    # write the third row printing the sum of profits and losses in the second column
   #3 csvwriter.writerow(["Total:", total])

    #write the fourth row
    #csvwriter.writerow(["Greatest Increase in Profits:", dateinc, amountinc])

     #write the fifth row
   # csvwriter.writerow(["Greatest Decrease in Profits:", datedec, amountdec])




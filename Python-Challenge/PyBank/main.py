
import os
import csv

#path to collect data for resources
#budget_csv = os.path.join("..", "Resources","budget_data.csv")
budget_csv = os.path.join("Resources", "budget_data.csv")

outputFile = os.path.join("Analysis", "budgetAnalysis.txt")

totalMonths = 0
totalRevenue = 0
monthlyChange = [] 
months = []


#open and read
with open(budget_csv) as csv_file:
    #create reader
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)
    #print(f"header: {csv_header}")

    firstRow = next(csv_reader)

    #firstMonth = 

    totalMonths +=1

        #add revenue 
    totalRevenue += float(firstRow[1])
    #previous revenue
    
    previousRevenue = float(firstRow[1])
    #move to first row
        

    for row in csv_reader:        
        totalMonths +=1

        #add revenue 
        totalRevenue += float(row[1])

        #calculate change 
        change = float(row[1])- previousRevenue
        #add change to the list of monthly changes
        monthlyChange.append(change)

        months.append(row[0])

        #update previous revenue
        previousRevenue = float(row[1])

#calculate avg change in revenue over each month
averageChange = sum(monthlyChange) / len(monthlyChange)

greatestIncrease = [months[0], monthlyChange[0]]
greatestDecrease = [months[0], monthlyChange[0]]



for m in range(len(monthlyChange)):
    #calculate greatest increase
    if(monthlyChange[m] > greatestIncrease [1]):
        greatestIncrease[1] = monthlyChange[m]
        greatestIncrease[0] = months[m]

        #calculate gratest decrease
    if(monthlyChange[m] < greatestDecrease [1]):
        greatestDecrease[1] = monthlyChange[m]
        greatestDecrease[0] = months[m]    


output = ( 
        f"\nFinancial Analysis \n"
          "-----------------------\n"
         f"Total months: = {totalMonths} \n"
         f"Total:  ${totalRevenue:,.2f} \n"
         f"Average Change: ${averageChange:,.2f}\n"
         f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.2f})\n" 
         f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})\n"
        )


print (output)

#export output to output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)


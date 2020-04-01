#call modules that are need for reading/writing and pathing
import csv
import os

# hey Leo this helped me find the file to read!
#print(os.listdir("../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/"))

# data file
budget_data = "../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/budget_data.csv"
#add arrays and variables for holding data
profit_net = 0 #the variable for the total profit/loss column
change =[] #used below make the change in profit/loss a list
months = [] #a list of the months in the first column to match the chchchchange index
chchchchange = [] #turn and face the strange

#read data file and capture header data
with open(budget_data, 'r', newline='') as csvfile: #open data file and read it
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)    # Pulls header data (I could understand this better)
    
    for row in csvreader:
        profit_net = profit_net + (int(row[1])) #profit/loss are strings and need to be converted for summing
        change.append(int(row[1])) #used below to calculate the month-over-month change
        months.append(row[0]) #makes the months a list so I can use the index of the Min/max above in change
i = 0
for i in range(len(change)): #loop through i to get the list of month-over-month changes
    if i >=1:
         chchchchange.append(change[i] - change[i -1]) #month-over-month change I could only figure out as a new list, not as a row above
    i += 1

#I've added commas for numbers, because that is easier to read.  I hope I don't lose points for this
#originally I used variables for the Greatest Increase and Decrease but I changed them below just to see if I could(I think variables are eaiser read in the code)
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months)}') #count of the rows minus the header
print(f'Total: ${profit_net: ,}') #sum of the profit/loss column.  
print(f'Average  Change: ${(round(sum(chchchchange)/(len(months)-1),2)): ,}') #I looked up sum on the internet. Round also. -1 to account for difference in list lengths
print(f'Greatest Increase in Profits: {months[chchchchange.index(max(chchchchange))+1]} (${max(chchchchange): ,})')#use the index of the maximum gain from chchchchange lsit to get the same index as month list
print(f'Greatest Decrease in Profits: {months[chchchchange.index(min(chchchchange))+1]} (${min(chchchchange): ,})')#as above but for the minimum

#there is a way to do both print and write at once but I don't understand yet.  So I've done it separately below
output_file = open("results_PyBank.txt","w+")
output_file.write('Financial Analysis \n')
output_file.write('---------------------------- \n')
output_file.write(f'Total Months: {len(months)} \n')
output_file.write(f'Total: ${profit_net: ,} \n')
output_file.write(f'Average  Change: ${(round(sum(chchchchange)/(len(months)-1),2)): ,} \n')
output_file.write(f'Greatest Increase in Profits: {months[chchchchange.index(max(chchchchange))+1]} (${max(chchchchange): ,}) \n') 
output_file.write(f'Greatest Decrease in Profits: {months[chchchchange.index(min(chchchchange))+1]} (${min(chchchchange): ,})')
output_file.close()
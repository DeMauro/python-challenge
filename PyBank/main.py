#call modules that are need for reading/writting and pathing
import csv
import os

# hey Leo this helped me find the file to read!
#print(os.listdir("../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/"))

# open data file
budget_data = "../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/budget_data.csv"
#add arrays and variables for holding data (maybe can remove some later)
mcount = 0
profit_net = 0
change =[] #used below make the profit/loss a list of intergers
months = [] #a list of the months minus the first line (and header) to match the chchchchange index
chchchchange = [] #turn and face the strange

#read data file and capture header data
with open(budget_data, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)    #this guy, wha? was with  - print(f"CSV Header: {csv_header}").  Pulling the header I think but how

    for row in csvreader:
        mcount = mcount + 1 #count months in column 1 (I think this works because of the csv_header above?)
        profit_net = profit_net + (int(row[1])) #profit/loss are strings and need to be convereted for summing
        change.append(int(row[1])) #used below to calculate the month over month change
        months.append(row[0]) #makes the months a list so I can use the index of the Min/max above in change
i = 0
for i in range(len(change)): #loop through i to get the list of month over month changes
    if i >=1:
         chchchchange.append(change[i] - change[i -1]) #month over month change I could only figure out as a new list, not as a row above
    i += 1

ncount = mcount - 1 #minus 1 month for averging change (since there is one less from the total months)
big = max(chchchchange) # the biggest number in the list.  Yay internet with Max
little = min(chchchchange) #as above so below, except...like, the little guy
big_index = chchchchange.index(big) #the index of the Greatest Increase so I can get the month   
little_index = chchchchange.index(little)#the index of the Greatest Decrease so I can get the month

#I've added commas for numbers, because that is easier to read.  I hope I don't lose points for this
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {mcount}') #count of the rows minus the header
print(f'Total: ${profit_net: ,}') #sum of the profit/loss column.  
print(f'Average  Change: ${(round(sum(chchchchange)/ncount,2)): ,}') #I looked up sum on the internet. Round also
print(f'Greatest Increase in Profits: {months[big_index +1]} (${big: ,})') #shift index up one number to account for the row removed from the change list
print(f'Greatest Decrease in Profits: {months[little_index +1]} (${little: ,})')#shift index as above

#there is a way to do both print and write at once but I don't understand yet.  So I've done it seperatly below
output_file = open("results_PyBank.txt","w+")
output_file.write('Financial Analysis \n')
output_file.write('---------------------------- \n')
output_file.write(f'Total Months: {mcount} \n')
output_file.write(f'Total: ${profit_net: ,} \n')
output_file.write(f'Average  Change: ${(round(sum(chchchchange)/ncount,2)): ,} \n')
output_file.write(f'Greatest Increase in Profits: {months[big_index +1]} (${big: ,}) \n') 
output_file.write(f'Greatest Decrease in Profits: {months[little_index +1]} (${little: ,})')

output_file.close()
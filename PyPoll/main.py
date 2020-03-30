#call modules that are need for reading/writting and pathing
import csv
import os

# open data file
election_data = "../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyPoll/Resources/election_data.csv"

vcount = 0 #total number of votes cast
cand_list = [] #list of candidates
candidates = [] #the total list of of all occurances of candidate names.  I just can't figure this out for row[2] of csvreader


with open(election_data, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)    #this guy, wha? was with  - print(f"CSV Header: {csv_header}").  Pulls header data but how?

    for row in csvreader:
        vcount = vcount + 1 #count the total number of columns to get total votes (I think this works because of the csv_header above?)
        candidates.append(row[2]) #all instances of candidate names, for counting votes later
        if row[2] not in cand_list:  #I tried with a boolean and failed misarably this was smarter but the web helped
            cand_list.append(row[2]) #list of candidate names without repeats        
    
vote_count=[0] * len(cand_list)#creates an array of zeros based on number of candidates (one zero for each candidate. In this case looks like [0, 0, 0, 0]) Thanks internet
percent=[0] * len(cand_list)#as above, for the percentages
i = 0
for i in range(len(cand_list)): #okay; for each of the candidates...
    x = 0
    y = cand_list[i]
    for line in candidates:
        if line == y: #match their name in the full list of candidate names...                
            x =x + 1
            vote_count[i] = x # then add one vote to that name's index position in the list of votes.  vote_count and cand_list now have matching indexes for candidae and # of votes

i = 0
for i in range(len(vote_count)):  #creating percentages of total votes for each candidate.  Again, indexes in the list match the other two lists.
    x = 0
    x = (vote_count[i]/vcount)*100
    percent[i] = x

#I've added commas for numbers, because that is easier to read.  I hope I don't lose points for this
print("Election Results")
print('-------------------------')
print(f'Total Votes: {vcount:,}') #total number of votes cast
print('-------------------------')
i=0
for i in range(len(cand_list)):# iterates through all candidates and matches index numbers in lists.  Could be 2 or 50 candidates
    print(f'{cand_list[i]}: {percent[i]: .3f}% ({vote_count[i]:,})') #why take the percent out to the 3rd decimal without the precision?
print('-------------------------')
w = max(vote_count)#matches the index number of the biggest number of votes to that candidates index
winner = vote_count.index(w)
print(f'Winner: {cand_list[winner]}')
print('-------------------------')

#there is a way to write to both screen and file but I can't figure out the module
#this is a different way of printing to a file than PyBank because of the iteration for candidate, percent, and vote count
output_file = open("results_PyPoll.txt","w+")
print("Election Results", file=output_file)
print('-------------------------', file=output_file)
print(f'Total Votes: {vcount:,}', file=output_file)
print('-------------------------', file=output_file)
i=0
for i in range(len(cand_list)):
    print(f'{cand_list[i]}: {percent[i]: .3f}% ({vote_count[i]:,})', file=output_file) 
print('-------------------------', file=output_file)
print(f'Winner: {cand_list[winner]}', file=output_file)
print('-------------------------', file=output_file)
output_file.close()
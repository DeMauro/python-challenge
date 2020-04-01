#call modules that are needed for reading/writing and pathing
import csv
import os

# open data file
election_data = "../../du-den-data-pt-03-2020-u-c/Homework-3-Python/PyPoll/Resources/election_data.csv"

cand_list = [] #list of individual candidates
candidates = [] #the total list of all occurrences of candidate names.  Used to tally candidate votes and get percentages of total votes

with open(election_data, 'r', newline='') as csvfile: #open and read the data dile
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)    # Pulls header data (I could understand this better)

    for row in csvreader:
        candidates.append(row[2]) #all instances of candidate names, for counting votes and creating percentages later (basically total votes)
        if row[2] not in cand_list:  #I tried with a Boolean and failed miserably. This was smarter but the web helped
            cand_list.append(row[2]) #list of candidate names without repeats        
    
vote_count=[0] * len(cand_list)#creates an array of zeros based on number of candidates (one zero for each candidate. In this case looks like [0, 0, 0, 0]) Thanks internet
percent=[0] * len(cand_list)#as above, for the percentages
i = 0
for i in range(len(cand_list)): #okay; for each of the candidates (no matter how many)...
    x = 0
    y = cand_list[i]
    for line in candidates:
        if line == y: #match their name in the full list of candidate names...                
            x =x + 1
            vote_count[i] = x # then add one vote to that name's index position in the list of votes.  vote_count and cand_list now have matching indexes for candidate and # of votes

i = 0
for i in range(len(vote_count)):  #creating percentages of total votes for each candidate.  Indexes in the list match the other two lists.
    x = 0
    x = (vote_count[i]/len(candidates))*100 #I thought using the length of the candidate list as total votes was smart, but I hurt my arm patting my own back
    percent[i] = x

#I've added commas for numbers, because that is easier to read.  I hope I don't lose points for this
print("Election Results")
print('-------------------------')
print(f'Total Votes: {len(candidates):,}') #total number of votes cast(*pat*, *pat*)
print('-------------------------')
i=0
for i in range(len(cand_list)):# iterates through all candidates and matches index numbers in lists.  Could be 2 or 2,000 candidates
    print(f'{cand_list[i]}: {percent[i]: .3f}% ({vote_count[i]:,})') #why take the percent out to the 3rd decimal without the precision?
print('-------------------------')
print(f'Winner: {cand_list[vote_count.index(max(vote_count))]}')#originally I did this with variables but figured out how to refer to the index of one list in another list
print('-------------------------')

#there is a way to write to both screen and file but I can't figure out the module
#this is a different way of printing to a file than PyBank because of the iteration for candidate, percent, and vote count
output_file = open("results_PyPoll.txt","w+")
print("Election Results", file=output_file)
print('-------------------------', file=output_file)
print(f'Total Votes: {len(candidates):,}', file=output_file)
print('-------------------------', file=output_file)
i=0
for i in range(len(cand_list)):
    print(f'{cand_list[i]}: {percent[i]: .3f}% ({vote_count[i]:,})', file=output_file) 
print('-------------------------', file=output_file)
print(f'Winner: {cand_list[vote_count.index(max(vote_count))]}', file=output_file)
print('-------------------------', file=output_file)
output_file.close()
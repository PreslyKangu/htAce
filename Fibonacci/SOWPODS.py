# start by importing the random library
import random

#type in all the list of words needed
details = []
with open ('Sowpods.txt', 'r')as f :
    line = f.readline().strip()
    details.append(line)
    while line:
        line =f.readline() .strip()
        details.append(line)

#generating a randon number

random_index = random.randint(0, len(details))

#now take the details
print("Random details:", details[random_index])




student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
alphadict = {}

df = pandas.read_csv('Day-26/nato_phonetic_alphabet.csv')
for (index, row) in df.iterrows():
    alphadict[row.letter] = row.code
#TODO 1. Create a dictionary in this format:
print(alphadict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter a Word")
names = [ word for word in name]
nameslist = [alphadict[item.capitalize()] for item in names]
print(nameslist)

   

    
    

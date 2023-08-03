letter = input("")
word = 'Faisal'

blanks =['_ _ _ _ _ _']
print(blanks)

for i in range(0,len(word)):
    if letter in word:
        blanks[i+1] = letter
        
print(blanks)
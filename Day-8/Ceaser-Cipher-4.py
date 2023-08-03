alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

    
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def ceaser(text,shift,direction):
        if direction == 'encode':
            encoded = ''
            for i in range(0,len(text)):
                if text[i] in alphabet:
                    encoded+=alphabet[(alphabet.index(text[i]))+shift]
                else:
                    encoded += text[i]
                    
            print(f"Encoded Word:{encoded}") 
        elif direction == 'decode':
            decoded = ''
            for i in range(0,len(text)):
                if text[i] in alphabet:
                    decoded+=alphabet[(alphabet.index(text[i]))-shift]
                else:
                    decoded += text[i]
            print(f"Decoded Word:{decoded}")

flag = True
print(logo)
while(flag):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >26:
        shift = shift%26
    ceaser(text,shift,direction) 
    print("type 'yes if you want to continue otherwise 'no")
    choice = input()
    if choice == 'yes':
        flag = True
    else:
        flag = False
              
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

     #Since z is the last index we need to copy the A_Z again in the alphabet list
    #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
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
              
   
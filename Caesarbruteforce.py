# WE brute fore the caesar cipher with python script
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
msg = input('Please enter the cipher text:')
msg = msg.upper()
#also add msg.lower

vocab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#loops through all of the possible keys
for key in range(26):
    decoded = ""

    #decodes message with given key
    for i in msg:
        if i.isspace():
            decoded = decoded + i
        else:
            letter = vocab.index(i)
            letter = letter - key
            letter = letter % 26
            decoded = decoded + vocab[letter]

    print('Key: %s  Decoded: %s' % (key, decoded))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

#this code uses rotate to encrypt the plain text

import string
import collections
# this code pieces uses rotate for caesar cipher like literally rorate LOL
def Caesar(input ,k):
    upper=collections.deque(string.ascii_uppercase)
    lower =collections.deque(string.ascii_lowercase)
    upper.rotate(k)
    lower.rotate(k)
    upper ='' .join(list(upper))
    lower ='' .join(list(lower))
    return input.translate(str.maketrans(string.ascii_uppercase,upper)).translate(str.maketrans(string.ascii_lowercase,lower))
plain =input("ENTER YOU PLAIN TEXT:")
k= int(input("Enter your key:"))
print(  Caesar(plain,k))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#   
"""I have this another piece of code below I saw online using ord()"""
#check for errors in this line :43
"""
import string
# first ask if you want to encrypt or decrypt
whatto_do =input("Encrypt=1 \t Bruteforce=0 \t choose what you want to proceed with :\n -->")
plain=input("Enter plain text:\n")
#now if ypu chose encrypt
if whatto_do =="1":
    k=int(input("Enter your key(0-26):\t"))

#now the basic stuff is done but we need to  define  a function  to solve the caesar cipher and we need to provide it with what all it does
def Caesar(input,k):
    #k is a global variable whose value will be used
    output=""
    input=input.lower()
    #define a input and output cuz you will get a plain text and a encrypted text although there is already variabales for that so u define new local variables instead of the local variable
    for x in input:
        if x in str.ascii_letters:
            temp = ord(x)+k
            if temp > ord("z"):            # this line is showing syntax error!?
            temp=temp-26
            #this is done cuz if the letter exceeds z it goes back to a
            output =output+chr(temp)
        else:
            output=output+x
            return output
#now that the cipher is complete
if  whatto_do =="1":
    print(Caesar(plain,k))
else:
    #this code is what will work for brute force
    for  k in range(26):
        print("key = "+str(k))
        print(Caesar(plain,k))

"""

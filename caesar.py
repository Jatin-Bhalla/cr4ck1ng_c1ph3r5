# from operator import mod


# plain =input("enter your message :\t")
# k =int(input("enter a key(0-25) :\t"))
# mode = input("set as DECRYPT\\ENCRYPT:\t")
# vocab ='ABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz1234567890!@$%^&*()_+=-}{][\\/><,.:;""~ '
# cipher=''

# for vocabulary in plain:
#     if vocabulary in vocab:
#         vocabularyIndex=vocab.find(vocabulary)
#         if mode=='encrypt'or  mode=='Encrypt' or  mode=='ENCRYPT': cipherIndex =vocabularyIndex + k
#         elif mode=='decrypt' or  mode=='Decrypt'  or  mode=='DECRYPT': cipherIndex =vocabularyIndex - k
#         cipherIndex =vocabularyIndex -k
#         if cipherIndex >= len(vocab): cipherIndex-= len(vocab)
#         elif cipherIndex <= len(vocab): cipherIndex+= len(vocab)
#         cipher+= vocab[cipherIndex]
#     else: cipher += vocabulary
# print(cipher)

###############################################
from cgitb import text
import string
plain=input("enter your PLAIN text:\t")
i=input("Select ENCRYPT/DECRYPT:\t")
if i =="ENCRYPT" or "encrypt" :
    k =int(input("enter a key number(0-25) :\t"))
elif i== "DECRYPT" or "decrypt":
    k =int(input("enter a key number(0-25) :\t"))
    k %=26
#  if k=0 we get the same
alphabet = string.ascii_lowercase
shifted_alphabet =alphabet[k:] +alphabet[:k]
#k: append the alphabet till k shift
# :k means we append everything that came before shift
table =str.maketrans(alphabet,shifted_alphabet)
encrypted =plain.translate(table)
print(encrypted)

###################################################
# Caesar cipher as a function:
import string
def caesar( plain,k,alphabet):
    def k (alphabet):
        return alphabet[k:]+alphabet[:k]
    k_alphabet =tuple(map(k_alphabet,alphabet))
    final_alphabet=''.join(alphabet)
    final_k_alphabet =''.join(k_alphabet)
    table=str.maketrans(final_alphabet,final_k_alphabet)
    return text.translate(table)

plain=input("Enter your PLAIN TEXT:\t")
k=int(input("Enter a number from 0-25:\t"))
print(caesar(plain,k,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))

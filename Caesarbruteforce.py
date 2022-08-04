# WE brute fore the caesar cipher with python script
""" This code ends up providing with every possiblility for the cipher for the english language as there are only 26 letters therefore only 25 possible crypts exist"""
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
for i in range(len(string.ascii_uppercase)):
    print( i,"|" , Caesar(plain,1))

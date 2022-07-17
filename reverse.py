from email import message
#REVERSE CIPHER

plain =input("Enter the PLAIN TEXT:\t ")
cipher=''#SINGLE QUOTES

i=len(plain)-1                                   #I=4
#i use this statement here because all the variable in the print statement exist after this line  
#puting this statement above would give an  error because the variabled does not exist
print( " this is value of i at this moment\t",i,"\t this is the value of plain[i]:\t",plain[i],"\t this is the value of  cipher:\t",cipher )
while i>=0:
    cipher=cipher+plain[i]  # WE PUT THE VALUE OF I IN AN INDEXING FUNCTION  CONCATENATES ONE BY ONE  leaving plain[i] with a single value and cpher with concatenated value of reverse string of plain
    #As a matter of fact we can ALSO SHOW the actual inner workings of the while loop at each iteration or interval
    print( " this is value of i at this moment\t",i,"\t this is the value of plain[i]:\t",plain[i],"\t this is the value of  cipher:\t",cipher )
    i=i-1
print(cipher) 
#we can put the PLAIN TEXT  to get the reverse text
#we can put the reversed text to get the PLAIN text




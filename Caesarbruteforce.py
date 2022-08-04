# WE brute fore the caesar cipher with python script
cipher =input("enter the cipher:\n -->")
symbol='abcdefghijklmnopqrstuvwxyz'

"""we need to use loop to end up with every possible outcome which may or may not make any sense"""
for k in range(len(symbol)):
    plain=""
    for symbol in message:
        if symbol in symbol:
            symbolIndex=symbol.find(symbol)
            translatedIndex =symbolIndex -k
            if  translatedIndex<0:
                translatedIndex = translatedIndex +len(symbol)
                translated = translated +symbol[translatedIndex]
            else:
                 translated =translated+symbol
            print('kay # %s:%s'%(k,translated))

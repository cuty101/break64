import binascii

def b64encode(string):
    base64index = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    longBin = ""
    print("Convert from String to Decimal to Binary")
    for char in string:
        value = str(ord(char))
        binary = format(ord(char), "08b")
        longBin = longBin + binary
        print(char+" = "+value+ " = "+binary)
    print("~"*60)
    splitList = [longBin[i:i+6] for i in range(0, len(longBin), 6)]
    tempPop = splitList.pop()
    if len(tempPop)!=8:
        tempPop = str(tempPop)
        tempPop = tempPop+("0"*(6-len(tempPop)))
        tempPop = str(tempPop)
    splitList.append(tempPop)
    splitString = ""
    splitString = " | ".join(splitList)
    print("Split the long binary to sets of 6 bits")
    print(splitString)
    print("~"*60)
    print("Total Length of string: "+str(len(string)))
    splitList.reverse()
    length = len(splitList)
    while splitList!=[]:
        tempPop = splitList.pop()
        decimal = int(tempPop, 2)
        print(tempPop +" = "+ str(decimal)+" = "+base64index[decimal])
    padding = (len(string)%3)
    if padding==2: padding = 1
    elif padding==1: padding = 2
    print("~"*60)
    print("If numbers of bytes are not divisible by 3, paddings will be added in the form of '=' to make it divisible by 3 since 3 bytes are converted to 4 sextets.")
    print("Numbers of Padding: "+str(padding))
    print("~"*60)
    string = string.encode("ascii")
    #string = binascii.b2a_base64(string, newline=False)
    string = binascii.b2a_base64(string)
    string = string.decode("ascii")
    print("Final Answer:")
    print(string)

def b64decode(string):
    base64index = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    longBin=""
    stringNoPad = string.replace("=","")
    print("Remove all '=' and convert each character to 6 bit of base64 index table")
    for i in stringNoPad:
        char = base64index.index(i)
        sextet = "{0:b}".format(char).zfill(6)
        longBin+=sextet
        print(i+" = "+str(char)+" = "+ sextet)
    print("~"*60)
    splitList = [longBin[i:i+8] for i in range(0, len(longBin), 8)]
    print("Combine them into sets of 8 bits, and remove all remaining '0' bits that do not make up a byte.")
    print(splitList)
    tempPop = splitList.pop()
    if len(tempPop)==8: splitList.append(tempPop)
    print(splitList)
    print("~"*60)
    splitList.reverse()
    length=len(splitList)
    print("Convert the bytes to the respective ASCII Character")
    while splitList!=[]:
        tempPop = splitList.pop()
        decimal = int(tempPop, 2)
        if len(tempPop)!=8:continue
        print(tempPop+" = "+str(decimal)+" = "+chr(decimal))
    print("~"*60)
    string = binascii.a2b_base64(string)
    string = string.decode("ascii")
    print("Final Answer:")
    print(string)

value = input("What do you want to do?\n1) base64 encode\n2) base64 decode\n")
string = input("Input string: ")
if value == "1":
    b64encode(string)
elif value == "2":
    b64decode(string)

print("(/^.^)/ This program is created by Verno. \(^.^\)")

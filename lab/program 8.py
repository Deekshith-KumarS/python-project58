inputString=input("Enter a string:")
countUpper=0
countLower=0
countSpaces=0
for i in inputString:
    if i.isupper():
        countUpper+=1
    elif i.islower():
        countLower+=1
    elif i.isspace():
        countSpaces+=1
print(f"Count of uppercase characters:{countUpper}")
print(f"Count of lowercase characters:{countLower}")
print(f"Count of spaces :{countSpaces}")
inputString=inputString.swapcase()
print(f"The toggled string is {inputString}")
string=input("Enter a string:")
countDigits=0
countLetters=0
for i in string:
    if i.isalpha():
        countLetters+=1
    elif i.isdigit():
        countDigits+=1
print(f"The number of letters is {countLetters}")
print(f"The number of digits is {countDigits}")
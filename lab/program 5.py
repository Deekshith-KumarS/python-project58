number=(1,7,5,67,69,96,24,36)
countOdd=0
countEven=0
for x in number:
    if not x%2:
        countEven+=1
    else:
        countOdd+=1
print(f"The count of even numbers ={countEven}")
print(f"The count of odd numbers={countOdd}")
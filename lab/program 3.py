a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
product=a*b
if product<=1000:
    result=product
else:
    result=a+b
print(f"The result is {result}")
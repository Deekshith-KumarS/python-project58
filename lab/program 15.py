import string,os
if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_uppercase:
    with open("letters\\"+letter+".txt","w") as f:
        f.writelines(letter)
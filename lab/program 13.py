with open ("myfile.txt","r") as fp:
    lines=len(fp.readlines())
print("The total number of lines=",lines)
fp.close
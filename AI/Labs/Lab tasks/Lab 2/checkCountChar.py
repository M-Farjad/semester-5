str=str(input("Enter a string: "))
count = 0
c=(input("Enter a character: "))[0]
for i in str:
    if i==c:
        count+=1
print("The character",c,"appears",count,"times in the string",str)
def getVowels():
    str1=''
    str = input("Enter a string: ")
    for i in str:
        if i in "aeiouAEIOU":
            str1 += i
    return str1

str = getVowels()
print('the vowels found in string are: ',str)
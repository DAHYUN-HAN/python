dict = {}

word = '19970718486940621412'

for char in word :
    
    if char not in dict :
        dict[char] = 1
    else :
        dict[char] = dict[char] + 1
        
print(dict)


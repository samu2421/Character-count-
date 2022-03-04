print("Enter the name of the string ")
str = input()

res = {}

for keys in str:
    res[keys] = res.get(keys, 0) + 1 

print("Count of characters in", str , "is :\n ", res)

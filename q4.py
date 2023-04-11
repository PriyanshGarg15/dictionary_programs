#Check whether given Key already exists in a Python Dictionary
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
n=int(input())
if n in d.keys():
    print("present")
else:
    print("not present")

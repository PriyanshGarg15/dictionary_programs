#Python program to sort (ascending and descending) a dictionary by value
import operator
d = {"p": 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=dict(sorted(d.items(),key=operator.itemgetter(1)))
print(a)
b=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print(b)

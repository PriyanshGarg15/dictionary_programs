#Print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys
d={}
for i in range(1,16):
    a=i
    b=i*i
    c={a:b}
    d.update(c)
print(d)
# --(or)
# d = dict()

# for x in range(1,16):
#     d[x]=x*x

# print(d) 

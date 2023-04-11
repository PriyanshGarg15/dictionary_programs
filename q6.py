#Generate and print a dictionary that contains a number in the form (x, x*x)
n=int(input())
d={}
for i in range(1,n+1):
    a=i
    b=i*i
    c={a:b}
    d.update(c)
print(d)
#or
# n=int(input("Input a number "))
# d = dict()

# for x in range(1,n+1):
#     d[x]=x*x

# print(d) 

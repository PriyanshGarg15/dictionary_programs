#Program to concatenate dictionaries to create a new one
d={1:1}
d1={2:2}
d2={3:3}
d3={}
for i in (d,d1,d2):
    d3.update(i)
print(d3)

d1={"grade":7, "roll":7, "age":12}
print(str(d1))
x=7
r=0
for k in d1:
    if d1[k]==x:
        r=r+1
print("Frequency of x is:",r)
#Q1. Print out Prime no. in one column and Composite no. in the other
c=0
p=[]
co=[]
for i in range(1,101):
    for j in range(1,101):
        if i%j==0:
            c+=1
    if c>2:
        co.append(i)
    else:
        p.append(i)
    c=0
print("Prime","       ","Composite")
for i in range(0,74):
    if i<26:
        print(p[i],"             ",co[i])
    else:
        print("no more prime   ",co[i])

 

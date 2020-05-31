## Function

def average(a,b):     # Declaring a fuction
    m=(a+b)/2         # Code of the function
    return(m)
    
#avg=average(11,23)    # Calling the function
#print(avg)


# Problem 1
def quad(a,b,c):
    global D
    D = ((b**2)-(4*a*c))**0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)
    print("First Root: ",x1)
    print("Second root: ",x2)

def disAnalysis(D):
    sq = D**2
    print("Square of D is ", sq)

## Lambda (Inline Function)

greeting = lambda name: print("Hello",name)
# funcName = lambda arguments: command

## File Handling

# Steps
# 1. Open the file
# 2. Read/Write
# 3. Close
# Modes r/w/a -> Text(t) binary->(b)



# Write
file= open('./Study Material/Codes/new.csv','w')
dat='1,akhil,47.8'
dat1='2,sumit,60'  
file.write(dat)
file.write("\n")
file.write(dat1)
file.close()

# Read
file= open('./Study Material/Codes/new.csv','r')
x = file.read()
#x= list(x)   # to convert into list
print(x)
file.close()

## Runtime Error Handling (try, except and finally)

a=int(input())
b=int(input())
try:     # the commands inside try block are prioritized and if they give error then this block is skipped and the commands in except block will be executed
    c=a/b
except:
    print("You didnt fill all the values")
finally:  # this will get executed in the end regardless which of the above block was executed
    print(c)


# Q. Building the same app as in previous assignment and upgrading it to use CVS to store and fetch data

def showShop():
    global inp
    print("**************************************************")
    print("\t My Mobiles Shop")
    print("**************************************************")
    print("\t 1. Show All Products")
    print("\t 2. Buy Product")
    print("\t 3. Add Product")
    print("\t 4. Exit")
    print("**************************************************")
    print()
    inp = int(input("Select an Option "))
    print()

def genBill(cust,phone,quan,cost,Fcost):
    print("**************************************************")
    print("\t My Mobiles Shop")
    print("**************************************************")
    print()
    print("\t Customer's Name:",cust)
    print("\t Customer's Phone:",phone)
    print("\t Bought",quan,product[ID])
    print("\t Cost:",cost)
    print("**************************************************")
    print("\t Final Cost with taxes",Fcost)
    print("**************************************************")
    print("\t Thank you for shopping with us")
    print()



def allProducts():
    print("SNO\tProduct\t\tIn Stock\tRate")
    for item in all_products:
        print("%d\t%s\t\t%d\t\t%s" %(int(item[0]), item[1],int(item[2]), item[3]))
    print()


showShop()

prod_ids=[]
IDs=[]
file=open('./ass06_AkhilJayan.csv','r')
products=[]
for line in file:
    products.append(line.strip())
all_products=[]
for i in range(len(products)):
    all_products.append(products[i].split(','))

try:
    while True:
        if inp == 1:
            allProducts()
            showShop()
            continue
            
        elif inp == 2:
            allProducts()
            ID=int(input("Product's Serial number "))
            for i in all_products:
                IDs.append(int(i[0]))
            if ID in IDs:
                item=all_products[prod_id-1]
            quan=int(input("How many? "))
            if quan > int(item[2]):
                print("These many not in stock")
            elif quan<=0:
                print("Please enter a valid quantity")
            else:
                sure=input("Are you sure?(Y or N) ")
                if sure=="Y" or sure=="y":
                    cust=input("Your name: ")
                    phone=input("Your Phone no: ")
                    cost= quan * int(item[3])
                    Fcost= cost + cost*0.18
                    (item[2]) -= quan
                    genBill(cust,phone,quan,cost,Fcost)
                    showShop()
                else:
                    print("Continue Exploring")
                    print()
                    showShop()
            continue

        elif inp == 3:
            username=input("Username: ")
            password=input("Password: ")
            if username == "Admin" and password == "password":
                    file=open('./ass06_AkhilJayan.csv','a')
                    prod = []
                    prod.append(len(all_products)+1)
                    prod.append(input("Enter the Product Name: "))
                    prod.append(int(input("Quantity: ")))
                    prod.append(input("Rate: "))
                    all_products.append(prod)
                    line=''
                    line+=str(prod[0])+','+prod[1]+','+str(prod[2])+','+prod[3]
                    file.write(line)
                    showShop()
                    continue
            else:
                print("Invalid Username or Password")
                continue

        elif inp == 4:
            break
except:
    print("Seed file not found")
finally:
    file.close()

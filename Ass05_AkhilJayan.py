## Q. Building a shop interface which can show products, buy and add products.

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
    print("\t Final Cost with taxes",Fcost)
    print()
    print("\t Thank you for shopping with us")
    print()

def delprod(ID):
    SNO.remove(SNO[ID])
    product.remove(product[ID])
    inStock.remove(inStock[ID])
    price.remove(price[ID])


def allProducts():
    print("%s\t%s\t%s\t%s"%(SNO[0],product[0],inStock[0],price[0]))
    for i in range(1,len(product)):
            print("%d\t%s\t%d\t%d"%(SNO[i],product[i],inStock[i],price[i]))
    print()

showShop()


SNO=['ID',1,2,3,4,5]
product=['Product','SmartPhone','HeadPhones','ScreenGaurd','Chargers','MemoryCards']
inStock=['\tInStock',20,100,200,100,120]
price=['Price',200,30,5,10,50]


while True:
    if inp == 1:
        allProducts()
        showShop()
        continue
        
    elif inp == 2:
        allProducts()
        ID=int(input("Product's Serial number "))
        quan=int(input("How many? "))
        if quan > inStock[ID]:
            print("These many not in stock")
        elif quan<=0:
            print("Please enter a valid quantity")
        else:
            sure=input("Are you sure?(Y or N) ")
            if sure=="Y" or sure=="y":
                cust=input("Your name: ")
                phone=input("Your Phone no: ")
                cost= quan * price[ID]
                Fcost= cost + cost*0.18
                inStock[ID] -= quan
                genBill(cust,phone,quan,cost,Fcost)
                if inStock[ID]==0:
                    delprod(ID)
                else:
                    pass
                showShop()
            else:
                print("Continue Exploring")
                print()
                showShop()
        continue

    elif inp == 3:
        username=input("Username: ")
        password=input("Password: ")
        if username=="Admin" and password=="Pass":
            addProd = input("What product do you wanna add? ")
            addStock = int(input("How many do you have "))
            addPrice = int(input("How much is a single piece worth? "))
            print()
            addSer = SNO[-1] + 1
            SNO.append(addSer)
            product.append(addProd)
            inStock.append(addStock)
            price.append(addPrice)
            allProducts()
            showShop()
            continue
        else:
            print("Invalid Username or Password")
            continue

    elif inp == 4:
        break

# Q. Building the same app as in previous assignment and upgrading it to use SQL and database to store and fetch data

import sqlite3 as sq
conn = sq.connect('shop.db')
cur = conn.cursor()
qry='create table if not exists admins(username text, password text)'
cur.execute(qry)
qry1='create table if not exists users(username text, password text)'
cur.execute(qry1)
qry3='create table if not exists shopItems(ID text, Product text, inStock text, Rate text)'
cur.execute(qry3)
##qry14 = '''insert into users(username,password) values ('User','Pass')'''
##cur.execute(qry14)
##qry4 = '''insert into admins(username,password) values ('Admin','password')'''
##cur.execute(qry4)
##qry5 = '''insert into shopItems(ID,Product,inStock,Rate) values ('1','Smartphone','20','200')'''
##cur.execute(qry5)
##qry6 = '''insert into shopItems(ID,Product,inStock,Rate) values ('2','Headphone','100','30')'''
##cur.execute(qry6)
##qry7 = '''insert into shopItems(ID,Product,inStock,Rate) values ('3','Screengaurd','200','5')'''
##cur.execute(qry7)
##qry8 = '''insert into shopItems(ID,Product,inStock,Rate) values ('4','Charger','100','10')'''
##cur.execute(qry8)
##qry9 = '''insert into shopItems(ID,Product,inStock,Rate) values ('5','MemoryCard','120','50')'''
##cur.execute(qry9)


def showLanding():
    global inp1
    print("**************************************************")
    print("\t My Mobiles Shop")
    print("**************************************************")
    print("\t 1. Login")
    print("\t 2. Register")
    print("**************************************************")
    print()
    inp1 = int(input("Select an Option "))

def allProducts():
    print("SNO\tProduct\t\tIn Stock\tRate")
    for item in all_products:
        print("%d\t%s\t\t%d\t\t%s" %(int(item[0]), item[1],int(item[2]), item[3]))
    print()

def genBill(cust,phone,quan,cost,Fcost):
    print("**************************************************")
    print("\t My Mobiles Shop")
    print("**************************************************")
    print()
    print("\t Customer's Name:",cust)
    print("\t Customer's Phone:",phone)
    print("\t Bought",quan,item[1])
    print("\t Cost:",cost)
    print("**************************************************")
    print("\t Final Cost with taxes",Fcost)
    print("**************************************************")
    print("\t Thank you for shopping with us")
    print()

def showShop():
    global inp
    print("**************************************************")
    print("\t My Mobiles Shop")
    print("**************************************************")
    print("\t 1. Show All Products")
    print("\t 2. Buy Product")
    print("\t 3. Exit")
    print("**************************************************")
    print()
    inp = int(input("Select an Option "))
    print()

showLanding()

IDs=[]
prod_ids=[]
qry2 = '''select * from shopItems where 1'''
x = cur.execute(qry2)
all_products = x.fetchall()
qry10 = '''select * from admins where 1'''
y = cur.execute(qry10)
admins = y.fetchall()
qry11 = '''select * from users where 1'''
z = cur.execute(qry11)
users = z.fetchall()
conn.commit()


try:
    while True:
        if inp1 == 1:
            username=input("Username: ")
            password=input("Password: ")
            if (username,password) in admins:
                prod = []
                prod.append(len(all_products)+1)
                prod.append(input("Enter the Product Name: "))
                prod.append(int(input("Quantity: ")))
                prod.append(input("Rate: "))
                all_products.append(prod)
                qry7 = '''insert into shopItems(ID,Product,inStock,Rate) values (prod[0],prod[1],prod[2],prod[3])'''
                cur.execute(qry7)

            elif (username,password) in users:
                showShop()
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
                        item=all_products[ID-1]
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
    ##                        (item[2]) -= quan
                            genBill(cust,phone,quan,cost,Fcost)
                            showShop()
                        else:
                            print("Continue Exploring")
                            print()
                            showShop()
                    continue

                elif inp==3:
                    break


            else:
                print("Incorrect Password or Email")
            
except:
    print("Seed file not found")

finally:
    conn.close()
        











        
        

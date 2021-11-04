Products=[]
def LoadDataFromFile():
    print('Loading...')
    f = open('database.csv','r')
    
    for row in f:
        info = row[:-1].split(',')
        NewDict = {'code':info[0],'name':info[1],'price':info[2],'count':info[3]}
        Products.append(NewDict)
    print('Database loaded succesfully!')
def ShowMenu():

    print('Welcome to our store :')
    print('1 - Add')
    print('2 - Edit')
    print('3 - Delete')
    print('4 - Show List')
    print('5 - Search')
    print('6 - Buy')
    print('7 - Save and Exit')

def Search():
    while True :   
        print('1 - search by code ')
        print('2 - search by name ')
        Choice = int(input())
        if Choice == 1 :    
            c = input('Enter product Code : ')
            for i in range(len(Products)):
                if Products[i]['code']==c:
                    print(Products[i])
                    return(i)
                    
        if Choice == 2 :
            n = input('Enter product name : ')
            for i in range(len(Products)):
                if Products[i]['name']==n:
                    print(Products[i])
                    return(i)
                    
        print("Product Not found !")
        print('1 - try again !')
        print('2 - Go back to main menu ')
        CC = int(input())
        if CC == 2 :
            break

def Add():
    while True :
        code = input('Enter product code : ')
        breaker = True 
        for i in range(len(Products)):
            if Products[i]['code']==code:
                print('code already taken !')
                breaker = False
        if breaker == True :
            break
    while True :
        name = input('Enter product name : ')
        breaker = True
        for i in range(len(Products)):
            if Products[i]['name']==name:
                print('name already in storage !')
                breaker = False
        if breaker == True :
            break           
    DictBuf = {'code':code,'name' :name, 'price':input('Enter product price : '),'count' : input('How many of this product you have in store ? ')}

    Products.append(DictBuf)
    print("product succesfully added !")
    
def Edit():
    i = Search()
    while True : 
       
        print('1 - edit code')
        print('2 - edit name ')
        print('3 - edit price')
        print('4 - edit count')
        print('5 - save and go back to main menu ')
        choice = int(input("Please choose an option : "))
        if choice == 1 :
            Products[i]['code'] = input('Enter code : ')          
        if choice == 2 :
            Products[i]['name'] = input('Enter name : ')
        if choice == 3 :
            Products[i]['price'] = input('Enter price : ')
        if choice == 4 :
            Products[i]['count'] = input('Enter count : ')
        if choice == 5 :
            break
      
def Delete():
    i = Search()
    Products.pop(i)
    print('Product deleted succesfully !')
   
def ShowList():
    print('ID\tName\tPrice\tCount')
    for p in Products : 
        print(p['code'],'\t',p['name'],'\t',p['price'],'\t',p['count'])
       
def Buy():
    i = Search()
    while True :
        print('How many of this product do you want to buy ? ')
        Count = int(input())
        if (int(Products[i]['count']) - Count) >= 0 :
            Products[i]['count'] = int(Products[i]['count']) - Count
            print('Thanks for your purchase')
            print('Total : ',(int(Products[i]['price']) * Count))
        else :
            print('we dont have that many of this product !!! ')
            print('1 - buy less amount ')
            print('2 - buy all we have in storage ')
            print('3 - go back to main menu ')
            CC =  int(input())
            if CC == 2 :
                Count = Products[i]['count']
                print('Thanks for your purchase')
                print('Total : ',(int(Products[i]['price']) * Count))
                Products[i]['count']=0
            if CC == 3 :
                break
                
def SaveData():
    f = open('DataBase.csv','w')
    for i in range(len(Products)):
        s = Products[i]['code']+','+Products[i]['name']+','+Products[i]['price']+','+Products[i]['count']+'\n'
        f.write(s)
            
LoadDataFromFile()
while True :
    ShowMenu()
    c = int(input('enter your choice : '))
    if c == 1:
        Add()
    if c == 2:
        Edit()
    if c == 3:
        Delete()
    if c == 4:
        ShowList()
    if c == 5:
        Search()
    if c == 6:
        Buy()
    if c == 7:
        SaveData()
        exit()
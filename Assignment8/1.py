class Kasr :
    def __init__(self,s,m):
        self.s = s
        self.m = m 
    
    def sum (a,b):
        r = Kasr( ( (a.s*b.m) + (a.m*b.s) ) , (a.m*b.m) )

        return r 

    def sub (a,b):
        r = Kasr( ( (a.s*b.m) - (a.m*b.s) ) , (a.m*b.m) )
        return r 
    
    def mul (a,b):
        r = Kasr((a.s * b.s) , (a.m * b.m))
        return r
        
    def div (a,b):
        r = Kasr( (a.s * b.m) , (a.m * b.s) )
        return r
    
    def Print(self):
        for i in range(self.s,1,-1):
            if self.s%i==0 and self.m%i==0 :
                self.s //=i
                self.m //=i
        print(self.s,'/',self.m)


a = Kasr(int(input("Soorat kasr a : ")),int(input("Makhraj kasr a = ")))
b = Kasr(int(input("Soorat kasr b : ")),int(input("Makhraj kasr b = ")))


while True : 
    print("Choose from options below : ")
    print("1- a*b ")
    print("2- a/b ")
    print("3- a+b ")
    print("4- a-b ")
    print("5- enter a and b again")
    print("6- Exit")
    c=int(input())
    
    if c == 1 :
        a.mul(b).Print()
    if c == 2 :
        a.div(b).Print()
    if c == 3 :
        a.sum(b).Print()
    if c == 4 :
        a.sub(b).Print()
    if c == 5 :
        a.s = int(input("Soorat kasr a : "))
        a.m = int(input("Makhraj kasr a = "))
        b.s = int(input("Soorat kasr b : "))
        b.m = int(input("Makhraj kasr b = "))
    if c == 6 :
        exit()


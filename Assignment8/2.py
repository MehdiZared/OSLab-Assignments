class Time :
    def __init__(self,h,m,s):
        self.s = s
        self.m = m 
        self.h = h
    def sum (a,b):
        r = Time(  (a.h+b.h) , (a.m+b.m)  , (a.s+b.s) )
        if r.s > 59 :
            r.s -= 60 
            r.m += 1
        if r.m > 59 :
            r.m -= 60
            r.h += 1
        return r 
    def sub (a,b):
        r = Time(  (a.h-b.h) , (a.m-b.m)  , (a.s-b.s) )
        if r.s < 0 :
            r.s += 60 
            r.m -= 1
        if r.m < 0 :
            r.m += 60
            r.h -= 1
        return r 
    def Print(self):
      print(self.h , ":" , self.m , ":" , self.s)
    def TimetoSec(self) :
        return (self.h*3600 + self.m*60 + self.s )
    @staticmethod
    def SecondtoTime(s):
        H = s//3600
        s = s%3600
        M = s//60
        S = s%60
        print(H , ":" , M , ":" , S)

a = Time(int(input("Hours a: ")),int(input("Minutes a : ")),int(input("Seconds a : ")))
b = Time(int(input("Hours b: ")),int(input("Minutes b : ")),int(input("Seconds b : ")))

while True : 
    print("Choose from options below : ")
    print("1- a+b ")
    print("2- a-b ")
    print("3- Time to Seconds")
    print("4- Seconds to Time")
    print("5- Exit")
    c=int(input())
    
    if c == 1 :
        a.sum(b).Print()
    if c == 2 :
        a.sub(b).Print()
    if c == 3 :
        print("a : " ,a.TimetoSec() , " Seconds")
        print("b : " ,b.TimetoSec() , " Seconds")
    if c == 4 :
        a.SecondtoTime(int(input("Enter seconds : ")))
    if c == 5 :
        exit()


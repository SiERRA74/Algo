
#Suite de Fibonacci en ittération et recursivité 

def fibo(X):
    Fn0 = 0
    Fn1 = 1
    r = 0
    print(Fn0)
    print("___________")
    print(Fn1)
    print("___________")
    while r < X :
        r = Fn0 + Fn1
        Fn1,Fn0 = r,Fn1
        print(r)
        print("___________")
    return ""

#print(fibo(300))

def fiboRec(Fn0 = 0, Fn1 = 1, r = 0):
    if r > 300:
        return ""
    r = Fn0 + Fn1
    print(r)
    fiboRec(Fn0 = Fn1, Fn1 = r, r = Fn0 + Fn1 )

#fiboRec()

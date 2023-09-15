def power(x, n):
    if x == 0 and n == 0:
        print('error')
    elif n == 0 or x == 1:
        return 1
    elif x == 0:
        return 0
    else : 
        return  x*power(x, n-1)  
print(power(2,3))
print(power(0,3))
print(power(5,1))

def fact(n):
    if n == 0 :
        return 1
    else :
        return n*fact(n-1)
print(fact(0))
print(fact(1))
print(fact(8))
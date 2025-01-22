
def sqr(num):
    return num*num


def sqrt(num):
    
    lis = []
    
    for i in range(100000):
        if i*i == num:
            lis.append(i)
            lis.append(-i)
            break
            
    return lis

def expo(num, expo):
    
    num1 = num
    
    for i in range(1, expo):
        num *= num1
        
    return num
        
        
            
    

def factor(num):
    
    lis = []

    for i in range(2,int(num/2 + 1)):
        
        for j in range(2, int(num/2 + 1)):
        
            if num/j == int(num/j):
                num = num/j
                lis.append(j)
                break
            
    lis.append(int(num))
    
    return lis
    

    
    




def roots(a, b,c):
    
    lis = []

    count = 0
    add = b
    product = a*c
    
    for i in range(-1000,1001):
        if count == 0:
            for n in range(-1000,1001):
                
                if (i*n) == product and (i + n) == add:
                    lis.append(i)
                    lis.append(n)
                    count += 1
            
    return lis

    if count == 0:
        print('No integral number roots')
        
        

                
        

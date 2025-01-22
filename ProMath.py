
def Sqr(num):
    print(num*num)

def Factor(num):
    
    lis = []

    for i in range(2,int(num/2 + 1)):
        
        for j in range(2, int(num/2 + 1)):
        
            if num/j == int(num/j):
                num = num/j
                lis.append(j)
                break
            
    lis.append(int(num))
    
    return lis
    

    
    




def Roots(a, b,c):
    
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
        
        

                
        

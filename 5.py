# Interview-Question



def calculateSum(n) : 

    if (n <= 0) : 

        return 0

    fibo =[0] * (n+1) 

    fibo[1] = 1

    sm = fibo[0] + fibo[1] 

    for i in range(2,n+1) : 

        fibo[i] = fibo[i-1] + fibo[i-2] 

        sm = sm + fibo[i] 

    return sm 

n = 4

print("Sum of Fibonacci numbers is : " , 

      calculateSum(n)) 

  

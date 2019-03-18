'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''



def Amicable():
    
    numbers = range(10000)


    for n in numbers:
        sum_of_a = 0
        sum_of_b = 0
       
        i = 1
        while(i < n):
            k = 0
            if(n % i == 0):
                sum_of_a = sum_of_a + i
                
            i = i + 1

        i1 = 1 
        while(i1 < sum_of_a):
            k1 = 0
            if(sum_of_a % i1 == 0):
                sum_of_b = sum_of_b + i1
                
            i1 = i1 + 1
 

        if((sum_of_a != sum_of_b) and (sum_of_b == n)):
            print("A amicable: ",sum_of_a)
            print("B amicable: ",sum_of_b)

    pass

Amicable()

#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#


A = 100

def factorialDigitSum(A):
    result_power = 1
    result_sum = 0
    while A > 0:
        result_power = result_power * A
        A -= 1
    print("Power: ",result_power)

    #while result_power > 0:
    #    d = result_power % 10
    #    result_power = result_power // 10
    #    result_sum += d

    for i in str(result_power):
        result_sum += int(i)
        
    print("Sum of digits: ",result_sum)

pass 

factorialDigitSum(A)

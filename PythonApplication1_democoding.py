# Demo Application
#
# This is a demo task.
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# •	N is an integer within the range [1..100,000];
# •	each element of array A is an integer within the range [−1,000,000..1,000,000].
#
#

A = [-1,-3,2,4,5]

def solution(A):
    A_sorted = sorted(A)

    A_sorted.append(A_sorted[len(A_sorted)-1]+1)
   
    A_sorted = list(set(A_sorted))

    i = 0
    counter = 0
    A_sorted_pos = []
    while i < len(A_sorted):
        if(A_sorted[i] > 0):
            A_sorted_pos.append(A_sorted[i])
            counter += 1
        i += 1
    if(len(A_sorted_pos) == 0):
        print(1)
           

    l = 0
    while l < (len(A_sorted_pos)-1):
        if(A_sorted_pos[l] != l + 1):
            print(l+1)
            break
        l += 1
        if(A_sorted_pos[len(A_sorted_pos)-1]) == l+1:
            print(A_sorted_pos[len(A_sorted_pos)-1])
        
pass


solution(A)
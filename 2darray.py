import sys
import math
a = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    a.append(arr_temp)
    
max_sum =-63
    
for i in range(4):
    for j in range(4):
        check_sum = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        '''
        top = sum(a[i][j:j+2]) 
        mid = a[i+1][j+1]
        bottom = sum(a[i+2][j:j+2])
        check_sum = top + mid + bottom           
        '''
        if check_sum > max_sum:
            max_sum = check_sum
            
print max_sum

'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

ans - 19

'''
import random

def print_2D_array():
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end=" ")
        print()
        
def find_sum():
    total = 0
    for i in arr:
        for j in i:
            total += j
    print(total)  

arr = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        arr[i][j] = random.randint(1,9)
        
print_2D_array()
find_sum()
        
        

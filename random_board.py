import random

def print2DArray():
    for i in arr:
        print(i)

arr = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        arr[i][j] = random.randint(1,9)
        
print2DArray()
        
        

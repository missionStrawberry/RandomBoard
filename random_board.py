arr = [[0 for i in range(10)] for j in range(10)]

for i in arr:
    for j in arr[i]:
        j = int(random() * 9 + 1)
        
print2DArray()
        
        
def print2DArray():
    for i in arr:
        for j in i:
            print(j)

row = int(input())
column = int(input())
arr = []
for i in range(row):
    arr.append(list(map(int, input().split())))
print(arr)
saddle_elemi = None
saddle_elemj = None
for i in range(row):
    for j in range(column):
        elem = arr[i][j]
        if elem == max(arr[i]) and elem == min([x[j] for x in arr]):
            saddle_elemi = i
            saddle_elemj = j
            
print(saddle_elemi, saddle_elemj )


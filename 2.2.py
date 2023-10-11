x = int(input())
pr = [i for i in range(x + 1)]
pr[1] = 0
i = 2
while i <= x:
    if pr[i] != 0:
        j = i + i
        while j <= x:
            pr[j] = 0
            j = j + i
    i += 1
pr = [i for i in pr if i != 0]
print(pr)

Max=0
for i in range(len(pr)-1, -1, -1):
    if x%pr[i]==0:
        Max=pr[i]
        break
print(Max)

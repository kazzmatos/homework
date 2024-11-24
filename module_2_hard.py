n = input('Введите число в первом поле ')
result1 = []
k = 1
for i in range(1, int(n)):
    for j in range(k, int(n)):
        if j != i and int(n) % (i + j) == 0:
            result1.append ([i, j])
        else: continue
    k += 1
result2 = []
for l in range(0, len(result1)):
    result2.extend(result1[l])
for m in range(0, len(result2)):
    result2[m] = str (result2[m])
result = "".join(result2)
print(result)




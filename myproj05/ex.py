target = [1, 1, 1, 1, 2, 2, 2, 23, 3, 4, 4, 45, 6, 1, 2, 3, 5, 2, 312, 412, 2, 2, 5, 3]

groupby = list(set(target))
result = dict()
for ip in groupby:
    result[ip] = target.count(ip)

print(result)

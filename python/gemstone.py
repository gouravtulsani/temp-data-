arr = ['abcdde','baccd','eeabg']
result = set(arr[0])
for s in arr[1:]:
    result.intersection_update(s)
return len(result)
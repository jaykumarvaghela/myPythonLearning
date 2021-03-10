arr1 = [1,2,3,4,5] 
arr2 = [4,5,6,7,8]

new = []
for i in arr1:
    if i not in arr2:
        new.append(i)
for i in arr2:
    if i not in arr1:
        new.append(i)


print(new)
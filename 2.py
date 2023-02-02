def func(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1 & set2
    return list(set3)
print(func([1,2,3,4],[2,3,5]))

def Merge(l1,l2):
    list=(l1+l2)
    list.sort()
    return(list)

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]

print("Merge and sort 2 list:",Merge(l1,l2))
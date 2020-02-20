a={"Atul","Vijay","Suraj"}
b={16,12,18}
print("String is:"+str(a))
print("Values are:"+str(b))

#convert list to dictionary
res={}
for key in b:
    for value in a:
        res[key]=value
        a.remove(value)
        break

print("Dictionary :"+str(res))
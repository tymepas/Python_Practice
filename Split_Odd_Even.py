'''
def splitevntodd(A):
    even=[]
    odd=[]
    for i in A:
        if (i%2==0):
            even.append(i)
        else:
            odd.append(i)
        print("Even List:",even)
        print("Odd List:",odd)
#Driver Code
A=list()
x=int(input("Enter the size of list:"))
print("Enter the elements of list:")
for i in range(int(x)):
    k=int(input(""))
    A.append(k)
splitevntodd(A)
'''

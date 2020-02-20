from collections import Counter
def common(str1,str2):
    a=Counter(str1)
    b=Counter(str2)
    commonDict=a & b

    if len(commonDict)==0:
        print(-1)
        return

    commonChars=list(commonDict.elements())
    commonChars=sorted(commonChars)
    print.join(commonChars)
if __name__=="__main__":
    str1="Char"
    str2="integer"
    common(str1,str2)
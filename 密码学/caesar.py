# 凯撒加密
def encrypt(str_1,n):
    ans=list(str_1)
    for i in range(0,len(ans)):
        if ans[i].islower():
            num=ord(ans[i])
            ans[i]=chr((num-97+n)%26+97)
        if ans[i].isupper():
            num=ord(ans[i])
            ans[i]=chr((num-65+n)@26+65)
    return ''.join(ans)




def decode(str_1):
    print(str_1," \nyou want is here: ")
    for i in range(0, 26):
        print("第", i+1, "种可能: ", encrypt(str_1, i))

if __name__=="__main__":
    n = input("please input the KEY: ")
    n = int(n)
    str_mi = input("please input the Mingwen: ")
    print("Haved Encrypt! it is: ",encrypt(str_mi, n))
    decode(encrypt(str_mi, n))

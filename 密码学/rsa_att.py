def egcd(a,b):
    if a==0:
        return(b,0,1)
    else:
        g,y,x=egcd(b%a,a)
        return (g,x-(b//a)*y,y)
def modinv(a,m):
    g,x,y=egcd(a,m)
    return x%m

if __name__=='__main__':
    n=int(input("请输入n："))
    c1=int(input("请输入c1："))
    e1=int(input("请输入e1："))
    c2=int(input("请输入c2："))
    e2=int(input("请输入e2："))
    temp=egcd(e1,e2)
    s1=temp[1]
    s2=temp[2]

    if(s1<0):
        s1=-s1
        c1=egcd(c1,n)[1]%n
    elif s2<0:
        s2=-s2
        c2=egcd(c2,n)[2]%n
    m=(c1**s1)*(c2**s2)%n
    print(m)
"""
PS D:\密码学课程设计> python3 rsa_att.py
请输入n：5456887
请输入c1：2972540
请输入e1：5
请输入c2：3055093
请输入e2：13
173024
"""

from lblock import *

skey="00101100111000000101010100101000"
k=[8,2,5,5,0,14,12,2]
res=""
for i in range(0,8):
    x = '{:04b}'.format(k[7-i])
    res=res+x
print (skey)
print(res)
if res == skey:
    print("密钥一致")

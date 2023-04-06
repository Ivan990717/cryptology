from lblock import *

output_dif=[0]
dic=[]
input1=""
input2=""
for x in range(0,16):
    for i in range(0,16):
        a = '{:04b}'.format(i)
        for j in range(0,i):
             b='{:04b}'.format(j)
             inXor=str_xor(a,b)
             outa=sBoxConfusion(a,0)
             outb=sBoxConfusion(b,0)
             outXor=str_xor(outb,outa)
             res=int(outXor[0])*8+int(outXor[1])*4+int(outXor[2])*2+int(outXor[3])
             if res ==x:
                 #print(a,b,outa,outb)
                 print("输入差分为：",hex(int(inXor,2)),"输出差分为：",hex(res),"输入的明文对为：",hex(int(a,2)),hex(int(b,2)))


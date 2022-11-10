from tkinter import *
from RSA1 import*

def run1():
     message = inp1.get()
     txt.insert(END,"n=")
     txt.insert(END,n)
     txt.insert(END,"\ne=")
     txt.insert(END,e)
     txt.insert(END,"\nd=")
     txt.insert(END,d)
     s = encrypt(e, n, message)
     txt.insert(END, "\n加密结果为:")   # 追加显示运算结果
     txt.insert(END,s)


def run2(x,y):
     cipher =x
     d = y
     M = decrypt(d, n, cipher)
     txt.insert(END, "\n解密结果为:")
     txt.insert(END, M)

     
p, q = gen_key()
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = gmpy2.invert(e, phi)
root = Tk()
root.geometry('460x240')
root.title('RSA加密器')

lb1 = Label(root, text='请输入密文')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

# 加密-直接调用 run1()
btn1 = Button(root, text='加密', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
# 解密-直接调用 run2()
btn2 = Button(root, text='解密', command=lambda: run2(inp1.get(), inp2.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)


# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.6, relheight=1.0)

root.mainloop()

"""
PS D:\密码学课程设计> python3 AES.py    
初始字节逆转换           0xfa7648efea54713db6c6c972462eb47
round[ 1 ].行逆移位      0xf626c13fea7eb97dba56447246c478e
round[ 1 ].字节逆转换    0xfbabb8820c893c859f298c16a6b816e6
round[ 1 ].轮密钥逆加    0xc922a8ed7dd351683639ad2df23cf3f9
round[ 1 ].列逆混合      0x3295141dc955d0dbe9c177d0cf3e5d68
round[ 2 ].行逆移位      0x323e77dbc9955dd0e9551468cfc1d01d
round[ 2 ].字节逆转换    0xa1d1029f12ad8d60ebed9bf75fdd60de
round[ 2 ].轮密钥逆加    0xaa4424a4517ef0e233a7d721a249a4fa
round[ 2 ].列逆混合      0x501a022673f1a817e236c2741d186ada
round[ 3 ].行逆移位      0x5018c217731a6a74e2f102da1d36a826
round[ 3 ].字节逆转换    0x6c34a8878f4358ca3b2b6a7ade246f23
round[ 3 ].轮密钥逆加    0xfa650783c7050373a0b25b2efbfae7d1
round[ 3 ].列逆混合      0xc5d70e07309f8b96374f021d1df86fbd
round[ 4 ].行逆移位      0xc5f8029630d76f1d379f0ebd1d4f8b07
round[ 4 ].字节逆转换    0x7e16a35080d06deb26ed7cdde92ce38
round[ 4 ].轮密钥逆加    0x71e6e19fd61af26361b1bd2060d5779e
round[ 4 ].列逆混合      0xd2f78b4746add86e94c8d2c3c73768c4
round[ 5 ].行逆移位      0xd237d26e46f768c394ad8bc4c7c8d847
round[ 5 ].字节逆转换    0x7fb27f459826f733e718ce8831b12d16
round[ 5 ].轮密钥逆加    0x6fd347d330368824ead050d85c29fe5d
round[ 5 ].列逆混合      0xdf93a7c3679490c915bed0c9346b21a8
round[ 6 ].行逆移位      0xdf6bd0c9679321c91594a7a834be90c3       
round[ 6 ].字节逆转换    0xef0560120a227b122fe7896f285a9633       
round[ 6 ].轮密钥逆加    0xbc87f754b2533c938a3f6828480adb28       
round[ 6 ].列逆混合      0xc932a9ca6da87ff442d15137f875122e       
round[ 7 ].行逆移位      0xc97551f46d32123742a8a92ef8d17fca       
round[ 7 ].字节逆转换    0x123f70bab3a139b2f66fb7c3e1516b10       
round[ 7 ].轮密钥逆加    0x8d2cad5a5852e975ebc6110524d9c74c       
round[ 7 ].列逆混合      0x842608fcf4e972f99eb816098f6c8015       
round[ 8 ].行逆移位      0x846c16f9f42680099ee908158fb872fc       
round[ 8 ].字节逆转换    0x4fb8ff69ba233a40dfebbf2f739a1e55       
round[ 8 ].轮密钥逆加    0x29cc9ae8cec3376729b1c92eabbb14cf       
round[ 8 ].列逆混合      0x41b3c7a29e15dd0b05a11bc088fcba05       
round[ 9 ].行逆移位      0x41fc1b0b9eb3bac00515c70588a1dda2       
round[ 9 ].字节逆转换    0xf855449edf4bc01f362f313697f1c91a       
round[ 9 ].轮密钥逆加    0xbd31352ecddfa8b9b4954a10b98ab581       
round[ 9 ].列逆混合      0xeb06562c7da91ec9ad9ca5efd0e7d2e2       
round[ 10].行逆移位      0xebe7a5c97d06d2efada956e2d09c1e2c       
round[ 10].字节逆转换    0x3cb0291213a57f6118b7b93b601ce942       
round[ 10].轮密逆钥加    0x112233445566778899aabbccddeeff
plaintext = 0x112233445566778899aabbccddeeff
"""

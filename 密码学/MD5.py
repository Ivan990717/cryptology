# 程序中：大端字节序
A = 0X67452301
B = 0XEFCDAB89
C = 0X98BADCFE
D = 0X10325476
# 常数T
T = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
     0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
     0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
     0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
     0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
     0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
     0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
     0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
     0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
     0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
     0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
     0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
     0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
     0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
     0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
     0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391, ]
maxInt = 0x100000000  # 2的32次方
S = [7, 12, 17, 22, 7, 12, 17, 22,
     7, 12, 17, 22, 7, 12, 17, 22,
     5,  9, 14, 20, 5,  9, 14, 20,
     5,  9, 14, 20, 5,  9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23,
     4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21,
     6, 10, 15, 21, 6, 10, 15, 21, ]


def fill(sequence):
    '将字节序列按小端序填充成512位【16整数*4字节】的倍数'
    count = len(sequence)
    multi_16s = ((count+8)//64+1)*16              # 共需要整数的个数，每个整数存储4个字节的数据
    print("共输入了", count*8, "位")
    sequence += [0]*(multi_16s*4-count)           # 用 0 填充
    sequence[count] |= 128                      # 用一个 1 补在后面
    multi_4bytes = []
    for i in range(len(sequence)//4):
        sequence[i*4+3], sequence[i*4+2], sequence[i*4+1], sequence[i *
                                                                    4] = tuple(sequence[i*4:(i+1)*4])              # 大端序存储
        multi_4bytes.append(int("".join(["{:08b}".format(
            ii) for ii in sequence[i*4:(i+1)*4]]), 2))              # 每四个Ascii合并成一个4字节整数
    multi_4bytes[-2], multi_4bytes[-1] = int("{:064b}".format(
        count*8)[32:], 2), int("{:064b}".format(count*8)[:32], 2)
    return multi_4bytes


def shift(x, n):
    '循环左移'
    return ((x << n) | (x >> (32-n)))


def F(X, Y, Z):
    return (X & Y) | ((~X) & Z)


def G(X, Y, Z):
    return (X & Z) | (Y & (~Z))


def H(X, Y, Z):
    return X ^ Y ^ Z


def I(X, Y, Z):
    return Y ^ (X | (~Z))


def Go(a, b, c, d, fun, m, s, K):
    thesum = (a + fun(b, c, d) + int(m) + K) % maxInt
    return (b+shift(thesum, s)) % maxInt


def int32ToHex(a):
    '32位整型集合转16进制'
    md5 = ''
    for i in a:
        x = "{:08x}".format(i)          # 整型【32位2进制】->8位16进制
        md5 += x[6:]+x[4:6]+x[2:4]+x[:2]          # 每两位切割, 切割4刀->逆序【大端变小端】
    return md5


if __name__ == "__main__":
    #text = input("请输入要摘要的字符串:")
    print("请输入信息输入字符串不能为空：")
    message = input().replace(' ', '')
    try:
        text = open('D:\密码学课程设计\MD5cipher.txt', 'w', encoding='utf-8')
        text.write(message)
        text.close()
        print("文件输出成功！")
    except IOError:
        print('文件加解密出错！！！')
    cipherText = open('D:\密码学课程设计\MD5cipher.txt', 'r', encoding='utf-8')
    text = cipherText.read()
    cipherText.close()
    text = text.replace('\n', '')
    sequence = list(bytes(text, 'utf-8'))      # 将unicode转换为字节序列
    text_int4 = fill(sequence)                # 将字节序列按小端序填充成4字节整数
    for i in range(len(text_int4)//16):             # 主循环
        a, b, c, d = A, B, C, D
        M = [text_int4[i*16+ii] for ii in range(16)]        # 取出16个整数
        print("M=", M)
        for ii in range(64):
            if ii < 16:
                A, B, C, D = D, Go(A, B, C, D, F, M[ii], S[ii], T[ii]), B, C
                print("i为", ii+1, "时：  A=", hex(A), "  B=",
                      hex(B), "  C=", hex(C), "  D=", hex(D), "\n")
            elif ii < 32:
                A, B, C, D = D, Go(
                    A, B, C, D, G, M[(ii*5+1) % 16], S[ii], T[ii]), B, C
                print("i为", ii+1, "时：  A=", hex(A), "  B=",
                      hex(B), "  C=", hex(C), "  D=", hex(D), "\n")
            elif ii < 48:
                A, B, C, D = D, Go(
                    A, B, C, D, H, M[((ii*3)+5) % 16], S[ii], T[ii]), B, C
                print("i为", ii+1, "时：  A=", hex(A), "  B=",
                      hex(B), "  C=", hex(C), "  D=", hex(D), "\n")
            else:
                A, B, C, D = D, Go(
                    A, B, C, D, I, M[ii*7 % 16], S[ii], T[ii]), B, C
                print("i为", ii+1, "时：  A=", hex(A), "  B=",
                      hex(B), "  C=", hex(C), "  D=", hex(D), "\n")
        A, B, C, D = (A+a) % maxInt, (B+b) % maxInt, (C+c) % maxInt, (D +
                                                                      d) % maxInt                             # 此处还是大端字节
    md5 = int32ToHex([A, B, C, D])
    print("32位小写:", md5)

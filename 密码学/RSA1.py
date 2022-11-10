import gmpy2
from gmpy2 import mpz
import binascii
import re
import codecs
"""
def gen_prime(rs):
    #生成二进制位数为1024的随机素数
    p = gmpy2.mpz_urandomb(rs, 1024)
    while not gmpy2.is_prime(p):
        p = p + 1
    return p


def gen_key():
    #生成密钥
    rs = gmpy2.random_state()
    p = gen_prime(rs)
    q = gen_prime(rs)
    print("p=", p, "\nq=", q)
    print("p.length=", len(p), "\nq.length=", len(q))
    return p, q


def encrypt(e, n, message):
    #将输入消息转换成16进制数字并加密，支持utf-8字符串
    M = mpz(binascii.hexlify(message.encode('utf-8')), 16)
    C = gmpy2.powmod(M, e, n)
    return C


def decrypt(d, n, C):
    #对输入的密文进行解密并解码
    M = gmpy2.powmod(C, d, n)
    #print("解密之后的数据为: ", M)
    return binascii.unhexlify(format(M, 'x')).decode('utf-8')
    # return binascii.unhexlify(format(M)).decode('utf-8')
    # return M

def main():
    # 密钥生成
    p, q = gen_key()
    n = p * q
    print("n=", p, "×", q, "=", n)
    phi = (p - 1) * (q - 1)
    e = 65537
    d = gmpy2.invert(e, phi)
    print("d=n÷e=", d)

    # 输入消息
    text = input('输入待加密的消息：\n')
    
    message = codecs.open('D:\密码学课程设计\Vtext.txt', 'r',
                          encoding=u'utf-8', errors='ignore')
    text = message.read()
    text = text.strip('\n')
    message.close()
    
    print(text)
    # 加密

    C = encrypt(e, n, text)
    print("密文为：", C)
    print("16进制密文：", hex(C))

    # 解密
    print("解密后的消息：", decrypt(d, n, C))


if __name__ == '__main__':
    main()
"""
print(gmpy2.powmod(173024, 5, 5597227))

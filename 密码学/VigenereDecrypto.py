def VigenereDecrypto(c, e):
    k = []
    elen = len(e)
    for i in range(len(c)):
        # chr(((ord(c[i])-65-ord(e[i%elen])-97+26)%26)+97)
        temp = chr(((ord(c[i])-65-ord(e[i % elen])+97+26) % 26)+97)
        k.append(temp)
    res = ''.join(k)
    return res


if __name__ == "__main__":
    print("维吉尼亚解密")
    cipherText = input("please input the text: ")
    key = input("please input the key: ")
    print("解密后的原文为："+VigenereDecrypto(cipherText, key))

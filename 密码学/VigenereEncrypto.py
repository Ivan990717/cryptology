import re


def VigenereEncrypto(input, key):
    out = []
    keylen = len(key)
    for i in range(len(input)):
        temp = chr(((ord(input[i])-97+ord(key[i % keylen])-97) % 26) + 97)
        out.append(temp)
    res = ''.join(out)
    return res


if __name__ == '__main__':
    flag = input("维吉尼亚加密\nplease input the kind of plaintext: ")
    key = input("please input the key: ")
    if flag == "words":
        plainText = input("please input the text: ")
        print("加密后的密文为："+VigenereEncrypto(plainText, key))
    if flag == "article":
        cipherText = open('D:\密码学课程设计\m.txt', 'r', encoding='utf-8')
        plainText = cipherText.read()
        cipherText.close()
        plainText = plainText.replace('\n', '')
        plainText = plainText.replace(' ', '')
        r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        plainText = re.sub(r, '', plainText)
        print("加密后的密文为："+VigenereEncrypto(plainText, key))
        text = open('D:\密码学课程设计\Vtext.txt', 'w', encoding='utf-8')
        text.write(plainText)
        text.close()
        print("文件输出成功")

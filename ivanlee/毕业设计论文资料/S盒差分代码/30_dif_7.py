from lblock import *
import random

def hexhex(a):
    return hex(int(a,2))
def regular_encode(message,key):
    left_plain=message[:32]
    right_plain=message[32:]
    print("原明文a为：",hexhex(left_plain[:4]))
    mes_tmp = left_plain  # 把左半边明文存起来
    shift_plain = left_turn(right_plain, 8)  # 右半边明文循环左移8位

    key_f = key[0:32]
    print("使用的32位密钥为：", key_f)
    #f_result = fun_f(mes_tmp, key_f)  # 轮函数的结果与又明文异或
    tmp = str_xor(left_plain, key_f)
    z = ""
    for i in range(0, 8):
        z += sBoxConfusion(tmp[i * 4:(i + 1) * 4], 7 - i)
    # for i in range(0,8):
    res = z[4:8] + z[12:16] + z[0:4] + z[8:12] + z[20:24] + z[28:32] + z[16:20] + z[24:28]
    righttext = str_xor(res, shift_plain)  # 两边交换
    lefttext = mes_tmp
    #print("输入S0盒的数据：",z[24:28])
    return lefttext + righttext

def difference_encode(message,key):
    dif=random.randint(1,15)
    guzhang='{:04b}'.format(dif)
    print("输入故障f为：",guzhang,"(",hexhex(guzhang),")")
    #xor=str_xor(guzhang,message[60:])
    f = str_xor(guzhang, message[:4])
    left_plain=f+message[4:32]
    right_plain=message[32:]
    in_dif=str_xor(right_plain+left_plain,message)
    #print("输入差分为：",in_dif)
    mes_tmp = left_plain  # 把左半边明文存起来
    shift_plain = left_turn(right_plain, 8)  # 右半边明文循环左移8位

    key_f = key[0:32]
    #print("使用的32位密钥为：", key_f)
    #f_result = fun_f(mes_tmp, key_f)  # 轮函数的结果与又明文异或
    tmp = str_xor(left_plain, key_f)
    z=""
    for i in range(0,8):
        z+=sBoxConfusion(tmp[i*4:(i+1)*4],7-i)
    #for i in range(0,8):
    res=z[4:8]+z[12:16]+z[0:4]+z[8:12]+z[20:24]+z[28:32]+z[16:20]+z[24:28]
    righttext = str_xor(res, shift_plain)  # 两边交换
    lefttext = mes_tmp
    return lefttext+righttext

if __name__ == '__main__':
    plain = "1010010010110001011100010010011010000111100110011100100110101111"
    key = "10111000101010110110010001001001111110110001101100000101100111000000101010100101"
    real_cipher=regular_encode(plain,key)
    print("real_cipher=",real_cipher)
    dif1_cipher=difference_encode(plain,key)
    dif2_cipher=difference_encode(plain,key)
    xor1_dif=str_xor(dif1_cipher,real_cipher)
    xor2_dif=str_xor(dif2_cipher,real_cipher)
    for i in range(0,16):
        if i ==8:
            print("****************")

        if xor1_dif[i*4:i*4+4]!=xor2_dif[i*4:i*4+4]:
            print(xor1_dif[i*4:i*4+4],"(",hexhex(xor1_dif[i*4:i*4+4]),")",xor2_dif[i*4:i*4+4],"(",hexhex(xor2_dif[i*4:i*4+4]),")""*")

        else:
            print(xor1_dif[i * 4:i * 4 + 4], "(", hexhex(xor1_dif[i * 4:i * 4 + 4]), ")", xor2_dif[i * 4:i * 4 + 4],
                  "(", hexhex(xor2_dif[i * 4:i * 4 + 4]), ")")


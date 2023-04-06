from S_box import *
from time import *
import re

def str2bin(message):
    res = ""
    for i in message:  # 对每个字符进行二进制转化
        tmp = bin(ord(i))[2:]  # 字符转成ascii，再转成二进制，并去掉前面的0b
        for j in range(0, 8-len(tmp)):  # 补齐8位
            tmp = '0' + tmp  # 把输出的b给去掉
        res += tmp
    #print("转化之后的字符串： ", res)
    return res

# 二进制转化为字符串
def bin2str(bin_str):
    res = ""
    tmp = re.findall(r'.{8}', bin_str)  # 每8位表示一个字符
    for i in tmp:
        res += chr(int(i, 2))  # base参数的意思，将该字符串视作2进制转化为10进制
    return res
    # print("未经过编码的加密结果:"+res)
    # print("经过base64编码:"+str(base64.b64encode(res.encode('utf-8')),'utf-8'))

# 字符串异或操作
def str_xor(my_str1, my_str2):  # str，key
    res = ""
    for i in range(0, len(my_str1)):
        # 变成10进制是转化成字符串 2进制与10进制异或结果一样，都是1,0
        xor_res = int(my_str1[i], 10) ^ int(my_str2[i], 10)
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'
    #print("异或后的字符串： ", res)
    return res

def deal_mess(bin_text):
    ans = len(bin_text)
    if ans % 64 != 0:
        for i in range(64 - (ans % 64)):  # 不够64位补充0
            bin_text += '0'
    return bin_text

# 循环左移操作
def left_turn(my_str, num):
    left_res = my_str[num:len(my_str)]
    #left_res = my_str[0:num]+left_res
    left_res = left_res+my_str[0:num]
    return left_res

# 查看秘钥是否为80位
def input_key_judge(bin_key):
    ans = len(bin_key)
    if len(bin_key) <= 80:
        if ans % 80 != 0:
            for i in range(80 - (ans % 80)):  # 不够64位补充0
                bin_key += '0'
    if len(bin_key) > 80:
       bin_key = bin_key[:80]
    print("密钥变为：", bin_key,"(",len(bin_key),")")
    #print(len(bin_key))
    return bin_key

def gen_key(key,num):
    shift_key=""
    ret_key=""
    res=""
    """print(key)
    if num==1:
        return key"""

    shift_key=left_turn(key,29)
    ret_key=sBoxConfusion(shift_key[0:4],9)+sBoxConfusion(shift_key[4:8],8)+shift_key[8:]
    #print("密钥经过S盒变换后：   ",ret_key)
    res = str(bin(num)[2:])
    for gz in range(0, 5 - len(res)):
        res = '0' + res
    tmp=ret_key[30:35]
    tmp=str_xor(tmp,res)
    ret_key=ret_key[:30]+tmp+ret_key[35:]
        #print("密钥经过异或后：    ",ret_key)
    print("密钥经过扩展函数处理之后：",ret_key)
    return ret_key
#S盒功能：对16比特的字符串进行混淆
def sBoxConfusion(bin_str,num):
    res=""
    tmp = int(bin_str,2)
    ans=S[num][tmp]
    res=str(bin(ans)[2:])
    for gz in range(0, 4 - len(res)):
        res = '0' + res
    return res

def fun_f(bin_Str,key):
    res=""
    z=""
    tmp=str_xor(bin_Str,key)
    for i in range(0,8):
        z+=sBoxConfusion(tmp[i*4:(i+1)*4],7-i)
    #for i in range(0,8):
    res=z[4:8]+z[12:16]+z[0:4]+z[8:12]+z[20:24]+z[28:32]+z[16:20]+z[24:28]
    return res

def all_message_encrypt(message, key):
    mes_bin=str2bin(message)   #先转换成字符串明文
    print("明文转变为二进制： ",mes_bin,"(",len(mes_bin),")")
    key_bin=str2bin(key)       #密钥转换成字符串
    print("密钥转变为二进制： ", key_bin,"(",len(key_bin),")")
    mes_bin2=deal_mess(mes_bin)    #把明文填满64位
    print("明文填充之后为： ",mes_bin2,"(",len(mes_bin2),")")
    key_bin2= input_key_judge(key_bin)    #把密钥填满80位
    print("密钥填充之后为： ", key_bin2,"(",len(key_bin2),")")
    #subkey=key_bin2
    #key_bin2=gen_key(key_judge)     #产生第一轮的密钥
    left_plain=mes_bin2[:32]
    right_plain=mes_bin2[32:]
    shift_plain=""
    for i in range(1,33):
        subkey=key_bin2
        #print(subkey,len(subkey))
        print("第",i,"轮：")
        mes_tmp=left_plain      #把左半边明文存起来
        shift_plain=left_turn(right_plain,8) #右半边明文循环左移8位
        #print(subkey)
        #print(subkey[0:33])
        key_f=subkey[0:32]
        print("使用的32位密钥为：" ,key_f)
        key_bin2 = gen_key(key_bin2,i)   #产生每一轮的密钥
        f_result=fun_f(mes_tmp,key_f)    #轮函数的结果与又明文异或
        left_plain=str_xor(f_result,shift_plain)    #两边交换
        right_plain=mes_tmp
        if i==32:
            left_plain,right_plain=right_plain,left_plain
        print("本轮加密后的密文为： ",left_plain+right_plain)
    return left_plain+right_plain




if __name__ == '__main__':
    print("请输入信息输入字符串不能为空：")
    message = input().replace(' ', '')
    print("please input your key：")
    key = input().replace(' ', '')
    begin_time=time()
    s = all_message_encrypt(message, key)
    end_time=time()
    run_time=end_time-begin_time
    #out_mess = bin2str(s)
    print("加密过后的内容:" + s)
    print("运行时间为：",run_time)
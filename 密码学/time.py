import hashlib
import time
s="liyifan"
t1 = time.time()
m = hashlib.md5()
b = s.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
t2=time.time()
print('MD5加密前为 ：' ,s)
print('MD5加密后为 ：' ,str_md5)
print((t2-t1)*5000)


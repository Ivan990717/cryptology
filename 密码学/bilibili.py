from urllib import request
url = "http://111.198.29.45:33206/shop?page="
for i in range(1000):
    response = request.urlopen(url+str(i))
    if "/static/img/lv/lv6.png" in response.read().decode('utf-8'):
        print("lv6在第", i, "页")
        break

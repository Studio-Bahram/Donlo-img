import requests as rq
from py3pin.Pinterest import Pinterest
import time
import json

print("""
Pls go to Site : https://Pinterest.com
and login or Sinup

for download img user and password its necessary
\033[0;32mhttps://StudioBahram.ir\033[0m
""")

try:
    f = open("date.txt","r")
    g = json.load(f)
    email = g.get("email")
    passwod = g.get('password')
    user = g.get('user')
    pinterest = Pinterest(email=email,password=passwod,username=user,cred_root='Pinterest_root')
    pinterest.login()
    print("Pinterest Logined")
    f.close()
except Exception:
    email = input("Enter Email: ")
    passwod = input("Enter Password: ")
    user = input("Enter User: ")
    try:
        pinterest = Pinterest(email=email,password=passwod,username=user,cred_root='Pinterest_root')
        pinterest.login()
        print("Pinterest Logined")
        dic_log = {'email':email,'password':passwod,'user':user}
        with open("date.txt","w") as f:
            json.dump(dic_log,f)
    except Exception:
        print("Soory , I couldn't login ")
        exit()



name_pic = input("Enter text for Search img: ")
if name_pic == "":
    print("Enter txt pls!")
    name_pic = input("Enter text for Search img: ")
    if name_pic == "":
        exit()

num_pic = input("Enter Number for renge img: ")
if num_pic.isnumeric():
    num_pic = int(num_pic)
else:
    print("Enter only nmber!")
    num_pic = input("Enter Number for renge img: ")
    if num_pic.isnumeric():
        num_pic = int(num_pic)
    else:
        exit()


scope='boards'
results = []

search_batch = pinterest.search(scope=scope, query=name_pic)
if len(search_batch) < num_pic:
    num_pic = len(search_batch) -1
if len(search_batch) == 0:
    print("Soory Not Found !")
    exit()
else:
    number_add = 0
    number_img = 0
    while number_add <= num_pic:
        results.append(search_batch[number_add])
        number_add += 1
    if len(results) == 0:
        print("Soory Not Found !")
        exit()
    else:
        while number_img < num_pic:
            url = results[number_img]["image_cover_hd_url"]
            r = rq.get(url, allow_redirects=True)
            with open("mars"+str(time.time_ns())+url[len(url)-4:], 'wb') as f:
                f.write(r.content)
            number_img += 1
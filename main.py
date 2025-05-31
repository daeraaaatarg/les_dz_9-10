# взаємодія з сайтами
import requests
from bs4 import BeautifulSoup
# ОТРИМАТИ ІНФОРМАЦІЮ - get()
# СТВОРИТИ на сервері - post()
# ОНОВЛЕННЯ - put() - перероблює, patch() - додає
# ВИДАЛЕННЯ - delete()
# для перевірки response: https://httpbin.org/get
# 200 - ok; https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

# GET -- при пошуку (інфа не персонально)
get = requests.get("https://httpbin.org/get")
print(get)
print(get.content)    # messy
print(get.text)       # content but good
print("======================================================")
# POST -- приватність (для особистих даних)
post = requests.post("https://httpbin.org/get",
                     data={"Test form":"myFORM"},
                     headers={"h1":"TestTitle"})
print(post)
print(post.content)
print(post.text)

print("======================================================")
print("======================================================")

# parse - законний і незаконний
coin = requests.get("https://coinmarketcap.com/")

if coin.status_code == 200:
    soup = BeautifulSoup(coin.text, features="html.parser")
    soup_list = soup.find_all("div",
                              {"class":"sc-142c02c-0"})
    res = soup_list[0].find("span")
    print(res.text)
print("======================================================")
coin_text = coin.text
coin_parse = coin_text.split("<span>")
for parse_elem in coin_parse:
    if parse_elem.startswith("$"):
        for parse_elem_2 in parse_elem.split("</span>"):
            if parse_elem_2.startswith("$"):
                print(parse_elem_2)

print("======================================================")
print("======================================================")
print("======================================================")
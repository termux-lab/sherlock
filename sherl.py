import requests, os, urllib.request, json, random, time, html2text, bs4
from bs4 import BeautifulSoup as BS
import re
ban = random.randint(0, 2)
os.system("clear")
def nick_search():
    nick = input("\033[35m|  |-[Enter nick]->\033[0m ")
    urls_site = ["https://vk.com/",
    "https://my.mail.ru/mail/",
    "https://www.drive2.ru/users/",
    "https://twitter.com/",
    "https://github.com/",
    "https://instagram.com/",
    "http://forum.3dnews.ru/member.php?username=",
    "https://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=",
    "https://forums.adobe.com/people/",
    "https://ask.fm/",
    "https://badoo.com/profile/",
    "https://www.bandcamp.com/",
    "https://bitcoinforum.com/profile/",
    "blogspot.com",
    "https://dev.to/",
    "https://www.ebay.com/usr/",
    "https://www.gamespot.com/profile/",
    "https://ok.ru/",
    "https://play.google.com/store/apps/developer?id=",
    "https://pokemonshowdown.com/users/",
    "https://www.reddit.com/user/",
    "https://steamcommunity.com/id/",
    "https://steamcommunity.com/groups/",
    "https://tamtam.chat/",
    "https://t.me/",
    "https://www.tiktok.com/@",
    "https://www.twitch.tv/",
    "https://data.typeracer.com/pit/profile?user=",
    "https://www.wikipedia.org/wiki/User:",
    "https://yandex.ru/collections/user/",
    "https://www.youtube.com/",
    "https://www.baby.ru/u/",
    "https://www.babyblog.ru/user/info/",
    "https://www.geocaching.com/profile/?u=",
    "https://habr.com/ru/users/",
    "https://pikabu.ru/@",
    "https://spletnik.ru/user/",
    "https://www.facebook.com/",
    "hhttps://zen.yandex.ru/",
    "https://ggscore.com/ru/dota-2/player?t=",
    "https://www.facebook.com/public/"]
    set_i = 0
    print("\033[35m|   |_\033[0m")
    while True:
        try:
            if set_i==13:
                scan_s = requests.get("https://"+nick+"."+urls_site[set_i])
            else:
                scan_s = requests.get(urls_site[set_i]+""+nick)

            if scan_s:
                if set_i==13:
                    print("\033[35m|     |- https://"+nick+"."+urls_site[set_i]+"\033[0m")
                else:
                    print("\033[35m|     |- "+urls_site[set_i]+""+nick+"\033[0m")
            else:
                print("\033[33m|     |-[No result]\033[0m")
        except:
            print("\033[33m|     |-[No result]\033[0m")
        if set_i+1 == len(urls_site):break
        set_i += 1
def ip_info():
    query = input("\033[35m|  |-[Enter ip]-> \033[0m")
    try:
        r = requests.get(f'http://ip-api.com/json/{query}').json()
        print('\033[36m|     |-[Country]: \033[32m'+str(r['country'])+'\n\033[36m|     |-[CountryCode]: \033[32m'+str(r['countryCode'])+'\n\033[36m|     |-[Region]: \033[32m'+str(r['region'])+'\n\033[36m|     |-[Region Name]: \033[32m'+str(r['regionName'])+'\n\033[36m|     |-[City]: \033[32m'+str(r['city'])+'\n\033[36m|     |-[Zip]: \033[32m'+str(r['zip'])+'\n\033[36m|     |-[Latinude]: \033[32m'+str(r['lat'])+'\n\033[36m|     |-[Longitude]: \033[32m'+str(r['lon'])+'\n\033[36m|     |-[Timezone]:\033[32m '+str(r['timezone'])+'\n\033[36m|     |-[ISP]:\033[32m '+str(r['isp'])+'\n\033[36m|     |-[Org]:\033[32m '+str(r['org'])+'\n\033[36m|     |-[As]:\033[32m '+str(r['as']+'\n\033[36m|\033[0m'))
    except:
        print('\033[31m|  |-Unkown error\033[0m')
    target_ip = query
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}
        page = requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip, headers=headers)
        soup = BS(page.content, "html.parser")
        table = soup.find(class_="table").find("tbody")
        torrents = table.find_all("tr")
        for torrent in torrents:
            first, last = torrent.find_all(class_="date-column")
            first, last = first.text, last.text
            category = torrent.find(class_="category-column").text
            name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
            size = torrent.find(class_="size-column").text
            print(f'\033[36m|     |-[Использовано первый раз]: \033[32m{first}\n\033[36m|     |-[использовано последний раз]: \033[32m{last}\n\033[36m|     |-[тип торента]: \033[32m{category}\n\033[36m|     |-[название торента]:\033[32m {name}\n\033[36m|     |-[размер торента]: \033[32m{size}\n\033[36m|\033[32m\033[0m')
    except:
        print('\033[31m|     |-Unkown error \033[0m')
    a=target_ip[:-2]
    with open('bdclean.txt', 'r') as f:
        nums = f.read().splitlines()
    for i in range(len(nums)):
        if a in nums[i]:
            print("\033[36m|     |-\033[32m"+nums[i]+"\033[0m")

def phone_info():
    phone = input('\033[35m|  |-[Enter phone]-> \033[0m')
    try:
        response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone)
        data = response.json()
        user_country = data[ 'country' ][ 'english' ]
        user_id = data[ 'country' ][ 'id' ]
        user_location = data[ 'country' ][ 'location' ]
        user_city = data[ 'capital' ][ 'english' ]
        user_lat = data[ 'capital' ][ 'latitude' ]
        user_log = data[ 'capital' ][ 'longitude' ]
        user_post = data[ 'capital' ][ 'post' ]
        user_oper = data[ '0' ][ 'oper' ]
        uty = requests.get("https://api.whatsapp.com/send?phone="+phone)
        if uty.status_code==200:
            utl2 = "https://api.whatsapp.com/send?phone="+phone
        else:
            pass
        userr_all_info = '\033[36m|     |-[Country]: \033[32m' + str(user_country) + '\n\033[36m|     |-[ID]:\033[32m ' + str(user_id) + '\n\033[36m|     |-[Location]:\033[32m ' + str(user_location) + '\n\033[36m|     |-[City]: \033[32m' + str(user_city) + '\n\033[36m|     |-[Latitude]: \033[32m' + str(user_lat) +'\n\033[36m|     |-[Longitude]: \033[32m' + str(user_log) +'\n\033[36m|     |-[Index post]: \033[32m' + str(user_post) + '\n\033[36m|     |-[Operator]: \033[32m' + str(user_oper)+"\033[0m"
        user_all_info = f"""{userr_all_info}\n\033[36m|     |-[WhatsApp]: \033[32m{utl2}\033[0m"""
        print(user_all_info)
    except:
        print('\033[31m|     |-Unkown error\033[0m ')
    try:
        page = requests.get('https://mirror.bullshit.agency/search_by_phone/'+phone)
        soup = BS(page.text, 'html.parser')
        classsell=soup.find(class_='media-heading')
        namesell= soup.find_all('h4')
        for classsell in namesell:
            print("\033[36m|     |-[Name]: \033[32m", classsell.text, "\033[0m")
        classtext = soup.find(class_='text-muted')
        nametext = soup.find_all('span')
        for classtext in nametext:
            print("\033[36m|     |-[Address and data]: \033[32m", classtext.text, "\033[0m")
    except:
        print('\033[31m|     |-Unkown error\033[0m')
    a=phone
    with open('bdclean.txt', 'r') as f:
        nums = f.read().splitlines()
    for i in range(len(nums)):
        if a in nums[i]:
            print("\033[36m|     |-\033[32m"+nums[i]+"\033[0m")
def get_html(url):
	return requests.get(url).text

def parse_ua(tutilka):
	soup = BS(tutilka, 'html.parser')
	for x in soup.findAll('td'):
		print(''.join(x.getText().split(' ')))
def ya_search():
    iduser = input("\033[35m|  |-[Enter user ID]-> \033[0mhttps://vk.com/id")
    token = input("\033[35m|  |-[access_token]->\033[30m ")
    r = requests.get("https://api.vk.com/method/newsfeed.getMentions?owner_id="+iduser+"&count=50&access_token="+token+"&v=5.50")
    datar = r.json()
    try:
        for pc in range(len(datar['response']['items'])):
            print("---------------------------")
            print("\033[36m|  |-[\033[33m"+str(pc)+"\033[36m]\033[32m https://vk.com/wall"+str(datar['response']['items'][pc]['to_id'])+"_"+str(datar['response']['items'][pc]['id'])+"\033[0m")
            print("\033[36m|  |\033[0m")
            try:
                print("\033[36m|  |-[Text]: \033[32m"+str(datar['response']['items'][pc]['text'])+"\033[0m")
            except:
                pass
        print("\033[36m|\n|==|-[Result]:\033[32m", pc, "\033[0m")
    except:
        print('\033[31m|     |-Unkown error\033[0m')
        print('\033[31m|     |-Error inf:', datar, "\033[0m")

def vk_track():
    iduser = input("\033[35m|  |-[Enter user ID]->\033[0m https://vk.com/id")
    token = input("\033[35m|  |-[access_token]-> \033[0m")
    new_time = 0
    old_time = 0
    check = 0
    check_time = 0
    online_offline = 0
    old_and_new_time = 0
    print("\033[36m|    |_\033[0m")
    while True:
        time.sleep(5)
        r = requests.get("https://api.vk.com/method/messages.getLastActivity?user_id="+iduser+"&access_token="+token+"&v=5.50")
        onlifline = r.json()
        online_yn =  str(onlifline['response']['online'])
        if online_offline == 0:
            if online_yn == '1':
                print("\033[36m|     |-[Status]: \033[32mOnline\033[0m")
                result_time = time.localtime(onlifline['response']['time'])
                old_time = str(result_time.tm_sec)[0]
                online_offline = 1
            elif online_yn == '0':
                print("\033[36m|     |-[Status]:\033[31m Offline\033[0m")
                online_offline = 2
            else:
                print("\033[36m|     |-[Status]:\033[33m Unkown\033[0m")
                online_offline = 3
        elif online_offline == 1 and online_yn == '0':
            online_offline = 0
        elif online_offline == 2 and online_yn == '1':
            online_offline = 0
        elif online_offline == 1:
            result_time = time.localtime(onlifline['response']['time'])
            if check == 0:
                if old_time == str(result_time.tm_sec)[0]:
                    pass
                elif new_time != old_time and check_time != 0:
                    check_time = 0
                elif old_time != str(result_time.tm_sec)[0] and old_and_new_time != str(result_time.tm_sec)[0] and check_time == 0:
                    print("\033[36m|     |-[\033[34m"+str(result_time.tm_min)+":"+str(result_time.tm_sec)+"\033[36m]:\033[33m Activity noticed. Maybe a message was sent or open VK\033[0m")
                    check_time = 1
                    new_time = str(result_time.tm_sec)[0]
                    old_and_new_time = new_time





banner = ["""\033[35m
       ,_
     ,'  `╲,_
     |_,-'_)
     /##c '╲  (
    ' |'  -{.  )
      /╲__-' ╲[]
     /`-_`╲       \033[0m     Sherlock Apps\033[35m
     '     ╲\033[0m 2.0\033[33m
   ____________________________________
   |   Termux-Lab  |   TG: @termuxlab | Beta
   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[0m
""",
"""\033[35m
         _               _            _
        | |             | |          | |
     ___| |__   ___ _ __| | ___   ___| | __\033[0m 2.0\033[35m
    / __| '_ ╲ / _ ╲ '__| |/ _ ╲ / __| |/ /
    ╲__ ╲ | | |  __/ |  | | (_) | (__|   <
    |___/_| |_|╲___|_|  |_|╲___/ ╲___|_|╲_╲\033[0m\033[33m
        ____________________________________
        |   Termux-Lab  |   TG: @termuxlab | Beta
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[0m
""",
"""
    Sherlock 2.0 \033[35m   ,N.\033[0m
    Apps \033[35m         _/__ ╲
                   -/o╲_╲
                 __╲_-./
                / / V ╲ U-.
    ())        /, > o <    ╲
    <╲.,.-._.-  [-╲ o /__..-1\033[0m \033[33m
    ____________________________________
    |   Termux-Lab  |   TG: @termuxlab | Beta
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[0m
     """]
text = """\033[32m
[1] - Car search(UA)   [5] - Ip scan
[2] - Phone scan       [6] - News feed (Vk)
[3] - Logger           [7] - Get password
[4] - Nick search      [X] - OSINT master
            [9] - Vk tracker
\033[36m
[01] - Live (For Logger)
[02] - Live (For Get password)\033[0m
"""
print(banner[ban])
print(text)
while True:
    numb = input("\033[35m[Enter number]->\033[0m ")
    if numb == "1":
        num = input('\033[35m|  [Enter car number](AX5631AA)-> \033[0m')
        try:
            parse_ua(get_html('https://baza-gai.com.ua/nomer/' + num))
        except:
            print('\033[31m [-] Unkown error\033[0m')
    elif numb == "2":
        phone_info()
    elif numb == "9":
        vk_track()
    elif numb == '5':
        ip_info()
    elif numb == '6':
        ya_search()
    elif numb == '4':
        nick_search()
    elif numb == '3':
        port = input("\033[35m|  |-[Enter port]->\033[0m ")
        os.system("cd logger && php -S localhost:"+port)
    elif numb == "01":
        rezerv = 0
        rf = ""
        while True:
            time.sleep(1)
            try:
                r_file = open("logger/result.txt", "r")
                rf = r_file.read()
                if rf == '':
                    rf = ""
                else:
                    print(rf)
                    sav_file = open("logger/result.txt", "w")
                    sav_file.write("")
                    sav_file.close()
            except:
                save_file = open("logger/result.txt", "w+")
                save_file.write("")
                save_file.close()
    elif numb == '7':
        port = input("\033[35m|  |-[Enter port]->\033[0m ")
        os.system("cd getpassword && php -S localhost:"+port)
    elif numb == 'clear' or numb == "?" or numb == "help":
        if numb=='clear':
            os.system('clear')
        print(text)
    elif numb == '02':
        rezerv = 0
        rf = ""
        while True:
            time.sleep(1)
            try:
                r_file = open("getpassword/result.txt", "r")
                rf = r_file.read()
                if rf == '':
                    rf = ""
                else:
                    print(rf)
                    sav_file = open("getpassword/result.txt", "w")
                    sav_file.write("")
                    sav_file.close()
            except:
                save_file = open("getpassword/result.txt", "w+")
                save_file.write("")
                save_file.close()
    else:
        print("\033[31m||Enter number or comand\033[0m")

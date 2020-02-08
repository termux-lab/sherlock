import requests, os, urllib.request, json, random, time
os.system("clear")
ban = random.randint(0, 3)
if ban == 0:
    banner = """
    ░░░░░░░░▄███▄▄▄░░▄▄▄███▄░░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░████Termux-Lab████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ██▄▄▄██▀▀▀▀██████████▀▀▀▀██▄▄▄██
    ░▀██████▄▄▄░░░░░░░░░░▄▄▄██████▀░
    ░░░▀████████████████████████▀░░░
    ░░▄█▀█▀▀▀▀████████████▀▀▀▀█▀█▄░░
    ░░█▀░▀░░░░░▄▄░░░░░░▄▄░░░░░▀░▀█░░
    ░░█▄░░░░░░█░░█░░░░█░░█░░░░░░▄█░░
    ░░░▀██▄░░░░▀▀░░█░░░▀▀░░░░▄██▀░░░
    ░░░░░▀█▄░░░░░░░▀▀░░░░░░░▄█▀░░░░░
    ░░░░░░░██▄▄░░░████░░░▄▄██░░░░░░░
    ░░░░░▄███████▄▄▄▄▄▄███████▄░░░░░
    ░░░░▄██████████████████████▄░░░░
    ░░░▄█████████████SᕼEᖇᒪOᑕK███▄░░░
    ░░▄██████████████████████████▄░░
    """
elif ban == 1:
    banner = """
       ,_
     ,'  `╲,_
     |_,-'_)
     /##c '╲  (
    ' |'  -{.  )
      /╲__-' ╲[]
     /`-_`╲             ԋҽɾɬσ𝓬ƙ
     '     ╲                TEᖇᗰᑌ-᙭ᒪᗩᗷ
   ____________________________________
   |VK: @termux_lab  | TG: @termuxlab |
   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
elif ban == 3:
    banner="""
         _               _            _
        | |             | |          | |
     ___| |__   ___ _ __| | ___   ___| | __
    / __| '_ ╲ / _ ╲ '__| |/ _ ╲ / __| |/ /
    ╲__ ╲ | | |  __/ |  | | (_) | (__|   <
    |___/_| |_|╲___|_|  |_|╲___/ ╲___|_|╲_╲
        ____________________________________
        |VK: @termux_lab  | TG: @termuxlab |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """
else:
    banner= """
    SᕼEᖇᒪOᑕK        ,N.
                  _/__ ╲
                   -/o╲_╲
                 __╲_-./
                / / V ╲ U-.
    ())        /, > o <    ╲
    <╲.,.-._.-  [-╲ o /__..-1
    ____________________________________
    |VK: @termux_lab  | TG: @termuxlab |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
     """
text = """
[1] - SEᗩᖇᑕᕼ ᑕᗩᖇ   [4] - ᑎIᑕK Sᑕᗩᑎ
[2] - ᑭᕼOᑎE IᑎᖴO   [5] - Iᑭ ᒪOᑕᗩTIOᑎ
[3] - ᒪOGGEᖇ       [6] - ᑕᒪEᗩᖇ
_______________________________
[0] - LIVE        [01] - UP!
"""
print(banner)
print(text)
while True:
    numb = input("[ᗯᖇITE ᑎᑌᗰᗷEᖇ]-> ")
    if numb == "1":
        car_num = input("|  [EᑎTEᖇ ᑕᗩᖇ ᑎᑌᗰᗷEᖇ](а111аа77)-> ")
        try:
            car_nums = car_num.upper()
            nc = car_num.lower()
            numb_car = nc[:6] + '.' + nc[6:]
            a_h=requests.get("https://авто-история.рф/num/"+car_nums+"/")
            km=requests.get("https://www.230km.ru/"+numb_car+".nomer")
            an=requests.get("http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
            if a_h:
                print("|    |_")
                print("|      |https://авто-история.рф/num/"+car_nums+"/")
                print("|      |")
                if km:
                    print("|      |-https://www.230km.ru/"+numb_car+".nomer")
                    print("|      |")
                else:
                    print("|    |")
                    print("|    |-[ᑎO ᖇESᑌᒪT]")
            else:
                print("|    |")
                print("|    |-[ᑎO ᖇESᑌᒪT]")
                print("|    |")
            if len(nc)<8:
                print("|    |-[ᑎO ᖇESᑌᒪT]")
                print("|    |")
            else:
                print("|    |-http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
                print("|    |")


        except:
                print("[ᑎO ᖇESᑌᒪT]")
    elif numb == "2":
        while True:
            try:
                phone = input("|  |-[EᑎTEᖇ ᑭᕼOᑎE]-> ")
                break
            except:
                print("|  |")
                print("|  |-[EᖇᖇOᖇ]")
                print("|  |")

        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
        try:
            infoPhones = urllib.request.urlopen( getInfo )
        except:
            print("|  |")
            print("|  |-[ᑎO ᖇESᑌᒪT]")
            print("|  |")

        infoPhone = json.load( infoPhones )
        try:
            print( u"|  |")
            print( u"|    |-[ᑕOᑌᑎTᖇY]--->", infoPhone["country"]["name"] )
            print( u"|    |-[ᖇEGIOᑎ]---->", infoPhone["region"]["name"] )
            print( u"|    |-[OᑭEᖇᗩTOᖇr]-->", infoPhone["0"]["oper"] )
            print( u"|    |-[ᑕITY]------> ", infoPhone["0"]["name"] )
        except:
            print("|  |")
            print("|  |-[Oᑎ TᕼE TOᖇ TO ᑕOᑎTIᑎᑌE ᗯOᖇKIᑎG ¯╲_(ツ)_/¯]")
            print("|  |")
    elif numb == '5':
        while True:
            try:
                getIP = input("|  |-[EᑎTEᖇ Iᑭ]-> ")
                break
            except:
                print("|  |")
                print("|  |-[EᖇᖇOᖇ]")
                print("|  |")


        url = "https://ipinfo.io/" + getIP + "/json"
        try:
            getInfo_ip = urllib.request.urlopen( url )
            infoList = json.load( getInfo_ip )
        except:
            print("|   |")
            print("|   |-ᑎO ᖇESᑌᒪT]")
            print("|   |")


        def whoisIPinfo(ip):
            try:
                myComand = "whois " + getIP
                whoisInfo = os.popen( myComand ).read()
                return whoisInfo
            except:
                print("|  |")
                print("|  |-[EᖇᖇOᖇ]")
                print("|  |")
        try:
            print( u"|   |_")
            print( u"|     |-[ᑕITY]-------> ", infoList["city"] )
            print( u"|     |-[ᖇEGIOᑎ]-----> ", infoList["region"] )
            print( u"|     |-[ᒪOᑕᗩTIOᑎ]---> ", infoList["loc"] )
            print( u"|     |-[OᑭEᖇᗩTOᖇ]---> ", infoList["org"] )
        except:
            print("|  |")
            print("|  |-[ᑎO ᖇESᑌᒪT]")
            print("|  |")
    elif numb == '6':
        os.system("python3 sherl.py")
    elif numb == '4':
        nick = input("|  |-[EᑎTEᖇ ᑎIᑕK]-> ")
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
        print("|   |_")
        while True:
            try:
                if set_i==13:
                    scan_s = requests.get("https://"+nick+"."+urls_site[set_i])
                else:
                    scan_s = requests.get(urls_site[set_i]+""+nick)

                if scan_s:
                    if set_i==13:
                        print("|     |- https://"+nick+"."+urls_site[set_i])
                    else:
                        print("|     |- "+urls_site[set_i]+""+nick)
                else:
                    print("|     |-[ᑎO ᖇESᑌᒪT]")
            except:
                print("|     |-[ᑎO ᖇESᑌᒪT]")
            if set_i+1 == len(urls_site):break

            set_i += 1

    elif numb == '3':
        port = input("|  |-[EᑎTEᖇ ᑭOᖇT]-> ")
        os.system("php -S localhost:"+port)
    elif numb == "0":
        rezerv = 0
        rf = ""
        while True:
            time.sleep(1)
            try:
                r_file = open("result.txt", "r")
                rf = r_file.read()
                if rf == '':
                    rf = ""
                else:
                    print(rf)
                    sav_file = open("result.txt", "w")
                    sav_file.write("")
                    sav_file.close()
            except:
                save_file = open("result.txt", "w+")
                save_file.write("")
                save_file.close()
    elif numb == '01':
        os.system("python3 install.py up")
    else:
        print(3)

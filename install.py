import os, sys
while True:
    if sys.argv[1]=='up':
        t='0'
    else:
        t='1'
        
    if t == '1':
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pkg install php")
        save_file = open("s.sh", "w+")
        save_file.write("python3 sherl.py")
        save_file.close()
        os.system("cat s.sh > /data/data/com.termux/files/usr/bin/s")
        os.system("chmod 700 /data/data/com.termux/files/usr/bin/s")
        os.system("s")
        break
    elif t == '0':
        os.system("pkg install wget")
        os.system("rm sherl.py")
        os.system("rm index.php")
        os.system("rm i.tl")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/i.tl")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/sherl.py")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/index.php")
        os.system("s")
        break
    else:
        print("0/1 ???")

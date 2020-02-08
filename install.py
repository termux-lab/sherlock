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
        os.system("rm i.tl")
        save_file = open("sher.sh", "w+")
        save_file.write("python3 sherl.py")
        save_file.close()
        os.system("cat sher.sh > /data/data/com.termux/files/usr/bin/sherl")
        os.system("chmod 700 /data/data/com.termux/files/usr/bin/sherl")
        os.system("cd ..")
        break
    elif t == '0':
        os.system("pkg install wget")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/sherl.py")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/index.php")
        os.system("sherl")
        break
    else:
        print("0/1 ???")

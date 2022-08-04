import requests as r
print("""
     _ _     ______  _                        
    | | |   (_____ \| |                       
  _ | | | _  _____) ) | _   ___  ____   ____  
 / || | || \|  ____/| || \ / _ \|  _ \ / _  ) 
( (_| | |_) ) |     | | | | |_| | | | ( (/ /  
 \____|____/|_|     |_| |_|\___/|_| |_|\____) 
""")
phone = input("Укажите номер телефона: +7")
phone = "7"+phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print("Идет поиск...")
datkey = "68747470733a2f2f646f6177616e7465642e72752f626f742f656e7465727265732e7068703f703d";
print(r.get(bytes.fromhex(datkey).decode('utf-8')+phone).text.replace("<br>", "\n").replace("*", "").replace("`", ""))

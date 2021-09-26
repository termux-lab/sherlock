import os, time
os.system("clear")
print("""\033[33m
><0>            ><1>       ###|
       ><1>                ###|
   ><0>             ><0>   ###|\033[0m
""")
print("\033[32mНаблюдаю за логами...\033[0m")
print("Укажите ссылку на историю в соц сетях")
urls = input("link: ")
f = open('./www/insttracker/HIST_URL','w+')
f.write(urls)
f.close()
while True:
	try:
		f = open('./logs/result.txt','r')
		value_f = f.read()
		if(value_f != ""):
			print(value_f)
			f = open('./logs/result.txt','w')
			f.write("")
		f.close()
	except:
		pass	
	

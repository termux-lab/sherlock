#=========================================
import base64, os, requests, json, time #=
from bs4 import BeautifulSoup           #=
#=========================================

#===============================================================================
print("""
Куда будут сохроняться изображения камеры после снимка?
(Def*)[1] /data/data/com.termux/files/home/storage/dcim/camera/
      [2] /data/data/com.termux/files/home/storage/{EDIT}
      [3] /{EDIT}
      [4] /data/data/com.termux/files/home/storage/dcim/OpenCamera/
""")
user_va = input("[S][E]: ")
if(user_va == "1"):
	dir_for_img = "/data/data/com.termux/files/home/storage/dcim/camera/"
elif(user_va == "2"):
	dir_for_img = input("  Подключить глаз шерлока\n к => /data/data/com.termux/files/home/storage/\n .::[Камера смартфона]::.")
elif(user_va == "4"):
	dir_for_img = input("  Подключить глаз шерлока\n к => /data/data/com.termux/files/home/storage/dcim/OpenCamera/\n .::[Приложение OpenCamera]::.")
else:
	dir_for_img = input(" Подключить глаз шерлока к => /")
print("Подключение глаз к "+dir_for_img)
input("Все файлы и папки в '"+ dir_for_img+ "' будут удалены. Это необходимо для оптимальной работы ГлазШерлока \nНажмите Enter. ")
os.system("rm -rf /"+dir_for_img+"/*")
#================================================================================

#================================================================================
def img_check():
	img_load_start = ""
	filelist = []
	for root, dirs, files in os.walk(dir_for_img):
		for file in files:
			filelist.append(os.path.join(root,file))
		img_load_start = "/"+dir_for_img+"/"+files[0]
	return(img_load_start)

def load_in_server(dir_for_img, img_load_start):
	with open(img_load_start, "rb") as file:
		url = "https://api.imgbb.com/1/upload"
		payload = {
			"key": "fcfbae2f7823157500624e0cd3701b13",
			"image": base64.b64encode(file.read()),
		}
		res = requests.post(url, payload)
	return(str(res.text))
	
def ya_img(newload_url):
	ya_url = 'https://yandex.ru/images/search?rpt=imageview&url='+newload_url+'?rr=0&yu=2599695931622150338&uinfo=sw-1920-sh-1080-ww-1920-wh-662-pd-1-wp-16x9_1920x1080&source-serpid=xf9AL61mlT3JfI6IylCRYQ'
	new_res = requests.get(ya_url)
	return(json.dumps(new_res.text))
#================================================================================

#================================================================================
while True:
	try:
		img_check()
		resul_ya = str(ya_img(json.loads(load_in_server(dir_for_img, img_check()))["data"]['url'])).replace(">", ">\n").replace(str('\\"'), '"')
		soup = BeautifulSoup(str(resul_ya), 'html.parser')
		span_s = soup.find_all("div", class_="Tags Tags_type_expandable Tags_view_buttons")[0]
		soup = BeautifulSoup(str(span_s), 'html.parser')
		respes = soup.find_all("span")
		print("<o>------------------------------------<o>")
		for i in range(len(respes)):
			print(respes[i].get_text().replace("\n", "").encode().decode('unicode_escape'))
		os.system("rm -rf /"+dir_for_img+"/*")
	except:
		time.sleep(2)
#================================================================================


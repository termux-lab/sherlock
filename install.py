import os
print("Обновление pip...")
os.system("pip3 install --upgrade pip")
os.system("clear")
print("              [Installer]\n")
mod = ["html2text", "requests", "bs4", "vk_api", "urllib3"]
print("Для работы этой версии шерлока, нужен доступ к хранилищу.")
input("Нажмите Enter, для установки нужных библиотек.")
os.system("termux-setup-storage")
print("Начало установки.")
for i in range(len(mod)):
    print("Установка "+mod[i]+"...")
    os.system("pip3 install "+mod[i])

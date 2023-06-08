import os, stat, os.path
import psutil

program_name = "notepad++.exe"
filename = input("Введите полный путь к файлу: ")

while(not(os.path.exists(filename) and os.path.isfile(filename))):
    filename = input("Введите полный путь к файлу: ")

os.chmod(filename, stat.S_IRUSR)
print("МБО работает...")

while(True):

    process_list = []
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if(process.info['name'] != program_name):
            cmdlin = process.info['cmdline']
            if(cmdlin != None):
                for i in cmdlin:
                    if(i == filename):
                        process_list.append(process.info)
        else:
            print(f"МБО: Доступ {process.name()} разрешён")

    for i in process_list:
        process = psutil.Process(i['pid'])
        print(f"МБО: Доступ {process.name()} запрещён")
        process.kill()


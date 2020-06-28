import shutil
from os import walk
import os
import ctypes
import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime


onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
dateOnly = datetime.utcfromtimestamp(os.path.getctime(onlyfiles[0])).strftime('%Y-%m-%d %H_%M_%S__')

try:
    os.mkdir(f"./{dateOnly}")
except FileExistsError:
    print("directory has also created")



allFiles = listdir()
onlyfolder = list(set(allFiles) - set(onlyfiles))

# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
# os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')

date = datetime.utcfromtimestamp(os.path.getctime(onlyfiles[0])).strftime('%Y-%m-%d %H_%M_%S')

for i in onlyfolder:
    if i != f"./{dateOnly}":
        if i.find("-") == -1:
            shutil.rmtree(i)
            try:
                os.mkdir(f"./{dateOnly}")
            except FileExistsError:
                print("directory has also created")
            
    

for i in onlyfiles:
    try:
        if i.endswith(".mp4"):
            os.rename(fr"./{i}",fr'./{date}.mp4')
            shutil.move(f'./{date}.mp4', f"./{dateOnly}/{i}")
            
        elif i.endswith(".log"):
            os.rename(fr"./{i}",fr'./base_chat.log')
            shutil.move('./base_chat.log', f"./{dateOnly}/base_chat.log")
        
        elif i.endswith(".json"):
            
            if(i.find("comments")):
                os.rename(fr"./{i}",fr'./comments.json')
                shutil.move('./comments.json', f"./{dateOnly}/comments.json")
            
            

            elif(i.find("downloads")):
                os.rename(fr"./{i}",fr'./info.json')
                shutil.move('./info.json', f"./{dateOnly}/info.json")

    except FileExistsError:
        print("This file has already renamed")


# os.system('pause')

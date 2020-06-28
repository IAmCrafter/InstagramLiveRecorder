import json
from datetime import datetime
import os.path
import io
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path.endswith('.json'):


    messageTextFile =  os.path.join(os.getcwd(), "messages.txt") 
    fi1e =  io.open("messages.txt", "w", encoding="utf-8") #os.path.join(os.getcwd(), "messages.txt")

    data = json.load(open(file_path, 'r'))

    try:
        for i in data['comments']:
            tempName = i['user']['username']
            tempMess = i['text']
            tempTime = datetime.utcfromtimestamp(i['created_at']).strftime('%Y-%m-%d %H:%M:%S')

            if(i['user']['is_verified'] == True):
                tempName += " (ᴠᴇʀɪꜰʏ)"

            if(i['user']['is_private'] == True):
                tempName += " (ʟᴏᴄᴋᴇᴅ)"

            tempMessage =f"({tempTime})   " + tempName + " : " + tempMess + '\n\n\n'
            fi1e.write(tempMessage)

        fi1e.close()
    except KeyError:
        print("You have selected a JSON file, but there is no messages of live.")
else:
    print("You Have not selected a JSON file, please try again.")

os.system('pause')

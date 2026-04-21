import sys
import os

try:
    from easier_openai import Assistant
except ImportError:
    print("easier_openai not installed. Quitting")
    sys.exit(1)

asst = Assistant()

if os.curdir != "src":
    os.chdir("src")
with open("../assets/sounds.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        print(i)
        asst.text_to_speech(i.strip(), play=False, response_format="mp3", save_to_file_path=f"../assets/{i.strip()}.mp3")

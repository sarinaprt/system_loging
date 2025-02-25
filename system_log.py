import os
import re

if not os.path.exists("username_file.txt"):
    with open("username_file.txt", "w", encoding="utf-8") as f:
        f.write("")

with open("username_file.txt", "r", encoding="utf-8") as f:
    read_user_file = f.read()

username = input("please enter your user name: ").strip()

name= re.findall(r":'(\w+)'", read_user_file)
if username == name:
    name_exists = True
    print("no finished")

else:
    id_user = read_user_file.count(":") + 1 
    with open("username_file.txt", "a", encoding="utf-8") as f:
        f.write(f" - {id_user}:'{username}'")  


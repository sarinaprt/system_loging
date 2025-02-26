import os
import re
if not os.path.exists("username_file.txt"):
    with open("username_file.txt", "w", encoding="utf-8") as f:
        f.write("")
    print("user folder")
if not os.path.exists("password_file.txt"):
    with open ("password_file.txt","w",encoding="utf-8")as p :
        p.write("")
    print("password folder")
        
with open("username_file.txt", "r", encoding="utf-8") as f:
    read_user_file = f.read()
    print(read_user_file)

username = input("please enter your user name: ").strip()
password=input("please enter your password")
# id_in_user=[]
name= re.findall(r":'(\w+)'", read_user_file)
if username in name:
    id=re.search(rf"-( \d+):'{username}'",read_user_file).group(1)
     
    
    # print(id.group(1))
    # id_in_user.append(id.group(1))
    # print(id_in_user)
    # print(id)

else:
    id_user = read_user_file.count(":") + 1 
    with open("username_file.txt", "a", encoding="utf-8") as f:
        f.write(f" - {id_user}:'{username}'")  
        


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
        

username = input("Please enter your username: ").strip("")
password = input("Please enter your password: ").strip("")

user_id=None
pass_id=None
with open("username_file.txt", "r", encoding="utf-8") as f_user:
    for line in f_user:
        id= re.search(rf"-\s*(\d+):'{username}'", line)
        if id:
            user_id=id.group(1)
            break

if user_id:
    with open("password_file.txt","r",encoding="utf-8")as f:
        lines=f.readlines()

    for line in lines:
        pass_finded_atr=re.search(rf"-\s*{user_id}:\s*'(.+?)'\s*",line)
        if pass_finded_atr:
            pass_finded=pass_finded_atr.group(1).strip()
            break

    if pass_finded == password:
        num = input("If you want to change your password enter 1, if you want to know your ID enter 2: ")

        if num=="1":
            new_pass=input("enter yor new password:\n")
            with open("password_file.txt", "r", encoding="utf-8") as f, open("temp.txt", "w", encoding="utf-8") as temp:
                for line in f:
                    updated_lines = re.sub(rf"-\s*{user_id}:'{pass_finded}'", rf"- {user_id}:'{new_pass}'", line)
                    temp.write(updated_lines)
            os.replace("temp.txt","password_file.txt")
            print("✅ Password updated successfully!")


        elif num == "2":
            print(f"Your ID is: {id}")


    else:
                
        print("❌ Wrong password!")


else:
    with open("username_file.txt", "r", encoding="utf-8") as f_user:
        content = f_user.read()
        new_id = content.count(":") + 1  
        #new_id = sum(1 for _ in open("username_file.txt", encoding="utf-8")) + 1

    with open("username_file.txt", "a", encoding="utf-8") as f_user, \
        open("password_file.txt", "a", encoding="utf-8") as f_pass:
        
        f_user.write(f"- {new_id}:'{username}'\n") 
        f_pass.write(f"- {new_id}:'{password}'\n")

    print("✅ New user registered successfully!")

import os
import re
from pydub import AudioSegment
from pydub.playback import play


sound_so={
    "1":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\۱.wav",
    "2":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\2.wav",
    "3":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\3.wav",
    "4":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\4.wav",
    "5":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\5.wav",
    "6":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\6.wav",
    "7":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\7.wav",
    "8":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\8.wav",
    "9":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\9.wav",
    "10":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\10.wav",
    "11":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\11.wav",
    "12":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\12.wav",
    "13":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\13.wav",
    "14":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\14.wav",
    "15":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\15.wav",
    "16":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\16.wav",
    "17":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\17.wav",
    "18":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\18.wav",
    "19":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\19.wav",
    "20":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\20.wav",
    "30":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\30.wav",
    "40":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\40.wav",
    "50":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\50.wav",
    "60":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\60.wav",
    "70":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\70.wav",
    "80":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\80.wav",
    "90":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\90.wav",
    "100":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\100.wav",
    "و":"C:\\Users\\NoteBook\\Documents\\Cyberlink\\libraryss\\system_log.py\\numbers\\او.wav"
    }
def sound_play(user_id):
    sound_1 = []  # لیست برای ذخیره‌ی فایل‌های صوتی
    
    user_id = str(user_id)  # تبدیل به رشته
    if user_id in sound_so:  
        file_path = sound_so[user_id]
        if os.path.exists(file_path):
            sound = AudioSegment.from_file(file_path)
            play(sound)
            print("🎵 Playing full ID sound")
        else:
            print(f"⚠️ Error: File not found - {file_path}")
    else:
        for num in user_id:
            if num in sound_so:
                file_path = sound_so[num]
                if os.path.exists(file_path):
                    sound_1.append(AudioSegment.from_file(file_path))
                else:
                    print(f"⚠️ File not found: {file_path}")
            else:
                print(f"⚠️ No sound file for number: {num}")

        if sound_1:  
            for sound in sound_1:
                play(sound)
        else:
            print("❌ No matching sound found.")


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
            print(f"Your ID is: {user_id}")
            sound_play(user_id)

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
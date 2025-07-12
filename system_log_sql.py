import os
from pydub import AudioSegment
from pydub.playback import play
import sound_lib
import DDL
import calcu
from calend import app_calender

def sound_play(user_id,speed=2.5):
    sound_list=[]
    if str(user_id) in sound_lib.sound_so:
        file_path=sound_lib.sound_so[str(user_id)]
        if os.path.exists(file_path):
            sound=AudioSegment.from_file(file_path).speedup(playback_speed=speed)+10
            play(sound)
        else:
            print("file path not exists")
    else:
        tens=(int(user_id)//10)*10
        ones=int(user_id)%10
        if int(user_id)>20 and ones!=0:
            if str(tens) in sound_lib.sound_so and str(ones) in sound_lib.sound_so:
                file_path_tens=sound_lib.sound_so[str(tens)]
                file_path_ones=sound_lib.sound_so[str(ones)]
                if os.path.exists(file_path_tens) and os.path.exists(file_path_ones):
                    sound_list.append(AudioSegment.from_file(file_path_tens).speedup(playback_speed=speed)+10)
                    sound_list.append(AudioSegment.from_file(sound_lib.sound_so["v"]).speedup(playback_speed=2.5)+10)
                    sound_list.append(AudioSegment.from_file(file_path_ones).speedup(playback_speed=speed)+10)
                else:
                    print("file path not exists")
            else:
                print(f" No sound file ")
        if sound_list:
            for sound in sound_list:
                play(sound)
        else:
            print("not found")
while True:
    try:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()
        break
    except KeyboardInterrupt as e :
        print("enter your username or password")   
print(f"{username} \n {password}")

user=DDL.user_exist(username)

if user:
    user_id=user[0]
    password_sql=user[1]

    if password_sql == password:
        Access = input("If you want to change your password enter 1, if you want to know your ID enter 2 ,calculater enter 3, daily note number 4: ")

        if Access=="1":
            new_password=input("enter yor new password:\n")
            DDL.update_pass(new_password,user_id)
            print("Your password has been changed")

        elif Access == "2":
            print(f"Your ID is : {user_id}")
            sound_play(user_id)

        elif Access=="3":
            calcu.calculator()
            print("calculator")

        elif Access=="4":
            app_calender(user_id)

    else:
                    
        print("Wrong password!")



else:
    DDL.insert_user(username,password)
    print("New user registered successfully!")

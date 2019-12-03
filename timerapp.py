import time
import datetime 
import colorama
from colorama import Fore, Back, Style
colorama.init()
# from playsound import playsound
import winsound

# number of seconds between time checks, 300 = 5 mins, but 900 print only the 15 mins messages
#  5 minute delay
# t_delay = 300
#  15 minute delay
# t_delay = 300

# audio file cues ////////////////////
# first hour chime
hr1_chime_path = "clock_auds/4weirdNya.wav"
# extra sound after hour chime plays
hr1_bonus_path = "clock_auds/hourlyNya.wav"
# Second + hour chime
hr2_chime_path = "clock_auds/awooShort.wav"
# # first quarter sound
carillion1_path = "clock_auds/1weirdNya.wav"
# # half hour sound
carillion2_path = "clock_auds/2weirdNya.wav"
# # 3/4 hr sound
carillion3_path = "clock_auds/3weirdNya.wav"
# //////////////////////////////////

current_time = datetime.datetime.now()

print("Start " + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
# put in update time adjust below, then for the sleep amount
print("Beginning timer: updates every 5 mins \n ---")

elapsed_min = 0
elapsed_quarters = 0
elapsed_hr = 0
while True:
    time.sleep(300)
    elapsed_min += 5
    # 60 for each hr
    if (elapsed_min % 60) == 0:
        elapsed_quarters -= 3
        elapsed_hr += 1
        # update current time
        current_time = datetime.datetime.now()
        if elapsed_hr == 1:
            # hourly chime
            print(Fore.YELLOW + Back.CYAN + str(elapsed_hr) + Style.RESET_ALL + " hour elapsed " + Back.CYAN + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
            winsound.PlaySound(hr1_chime_path, winsound.SND_FILENAME)
            winsound.PlaySound(hr1_bonus_path, winsound.SND_ASYNC)
        else: 
            print(Fore.RED + Back.WHITE + str(elapsed_hr) + Style.RESET_ALL + " hours have elapsed " + Back.RED + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
            winsound.PlaySound(hr2_chime_path, winsound.SND_ASYNC)
        # play hour marker special aud
    elif elapsed_min != 0 and elapsed_min % 15 == 0:
        elapsed_quarters += 1
        if elapsed_quarters == 1 :
            # play audio for 1st carillion
            winsound.PlaySound(carillion1_path, winsound.SND_ASYNC)
            #  text for 1st is same as 3rd quarter
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        elif elapsed_quarters == 2:
            # half carillion
            winsound.PlaySound(carillion2_path, winsound.SND_ASYNC)
            # update current time for display purposes
            current_time = datetime.datetime.now()
            print(Back.YELLOW + Fore.BLACK + str(elapsed_min) + Style.RESET_ALL + " min elapsed " + Back.YELLOW + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
        elif elapsed_quarters == 3:
            # 3rd quarter carillion
            winsound.PlaySound(carillion3_path, winsound.SND_ASYNC)
            # text for 3rd quarter same as 1st
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        # play nyas based on elapsed time
    else:
        print(str(elapsed_min) + " min...")

# ///////////
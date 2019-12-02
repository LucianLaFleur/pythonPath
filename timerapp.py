import time
import datetime 
import colorama
from colorama import Fore, Back, Style
colorama.init()
# from playsound import playsound
import winsound

# winsound.PlaySound("clock_auds/1weirdNya.wav", winsound.SND_ASYNC)

# c_t = datetime.datetime.now()

# tar_time = c_t.minute + 15

# print(c_t)
# print("curr min ... %s." % c_t.minute)
# print("tar for chime ... %s." % tar_time)

# /////////

# POMIDORO
# Adjust, run a pomidoro timer, 30 min work, 10 break
#  how to open youtube from python? Check udemy classes
# CLOCK TOWER RELATED TO REAL TIME
#  track internal clock , playing nya each time hour?
# check if the time.minute == 14 and time.second == 00
# play chime

# ////////////
# NOTE: CURR GOAL: iterate out sound files to variables


# number of seconds between time checks, 300 = 5 mins, but 900 print only the 15 mins messages
t_delay = 4

# audio file cues
# first hour chime
hr1_chime = winsound.PlaySound("clock_auds/4weirdNya.wav", winsound.SND_FILENAME)
# extra sound after hour chime plays
hr1_bonus = winsound.PlaySound("clock_auds/hourlyNya.wav", winsound.SND_ASYNC)
# first quarter sound
carillion1 = winsound.PlaySound("clock_auds/1weirdNya.wav", winsound.SND_ASYNC)
# half hour sound
carillion2 = winsound.PlaySound("clock_auds/2weirdNya.wav", winsound.SND_ASYNC)
# 3/4 hr sound
carillion3 = winsound.PlaySound("clock_auds/3weirdNya.wav", winsound.SND_ASYNC)

current_time = datetime.datetime.now()

print("Start " + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
# put in update time adjust below, then for the sleep amount
print("Beginning timer: updates every 5 mins \n ---")

elapsed_min = 0
elapsed_quarters = 0
elapsed_hr = 0
while True:
    time.sleep(t_delay)
    elapsed_min += (t_delay/60)
    # 60 for each hr
    if (elapsed_min % 60) == 0:
        elapsed_quarters -= 3
        elapsed_hr += 1
        if elapsed_hr == 1:
            # hourly chime
            print(Fore.YELLOW + Back.CYAN + str(elapsed_hr) + Style.RESET_ALL + " hour elapsed " + Back.CYAN + "--- --- ---" + Style.RESET_ALL)
            hr1_chime
            hr1_bonus
        else: 
            print(Fore.RED + Back.WHITE + str(elapsed_hr) + Style.RESET_ALL + " hours have elapsed " + Back.RED + "--- --- ---" + Style.RESET_ALL)
            winsound.PlaySound("clock_auds/awooShort.wav", winsound.SND_FILENAME)
        # play hour marker special aud
    elif elapsed_min != 0 and elapsed_min % 15 == 0:
        elapsed_quarters += 1
        if elapsed_quarters == 1 :
            # play audio for 1st carillion
            carillion1
            #  text for 1st is same as 3rd quarter
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        elif elapsed_quarters == 2:
            # half carillion
            carillion2
            print(Back.YELLOW + Fore.BLACK + str(elapsed_min) + Style.RESET_ALL + " min elapsed " + Back.YELLOW + "--- --- ---" + Style.RESET_ALL)
        elif elapsed_quarters == 3:
            # 3rd quarter carillion
            carillion3
            # text for 3rd quarter same as 1st
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        # play nyas based on elapsed time
    else:
        print(str(elapsed_min) + " min...")

# ///////////
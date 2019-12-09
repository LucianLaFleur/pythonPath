import time
import datetime 
import colorama
from colorama import Fore, Back, Style
colorama.init()
import winsound


# audio file cues EXAMPLE ONLY ////////////////////
# first hour chime
hr1_chime_path = "clock_auds/4weirdNya.wav"
# //////////////////////////////////

current_time = datetime.datetime.now()

# print("Start " + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
# put in update time adjust below, then for the sleep amount

# //////////take in user input for 
# warning for near break end?
# activte start marker?
# rest start marker?
# Make defaults for pomidoro
# make variant for res-band ac40, rest20, 5round, br-90, vi 3 cycles, (heavy pump workout)

active_t = 10
rest_t = 2
num_rounds = 3
# ...  subtracting ending rest when finished, thus the -1 , e.g. you don't rest before the intermission...
set_t = ((active_t * num_rounds) + (rest_t*(num_rounds-1)))
print("time per set : " + str(set_t))
set_intermission = 1000
num_cycles = 3
# ... a cycle is an activity/rest pattern bookended by a round break
cycle_t = (set_t * num_cycles) + (set_intermission * (num_cycles - 1))
print("Total time : " + str(cycle_t))

# //////////////
# elapsed_min = 0
# elapsed_quarters = 0
# elapsed_hr = 0
# while True:
#     time.sleep(300)
#     elapsed_min += 5
#     # 60 for each hr
#     if (elapsed_min % 60) == 0:
#         elapsed_quarters -= 3
#         elapsed_hr += 1
#         # update current time
#         current_time = datetime.datetime.now()
#         if elapsed_hr == 1:
#             # hourly chime
#             print(Fore.YELLOW + Back.CYAN + str(elapsed_hr) + Style.RESET_ALL + " hour elapsed " + Back.CYAN + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
#             winsound.PlaySound(hr1_chime_path, winsound.SND_FILENAME)
#             winsound.PlaySound(hr1_bonus_path, winsound.SND_ASYNC)
#         else: 
#             print(Fore.RED + Back.WHITE + str(elapsed_hr) + Style.RESET_ALL + " hours have elapsed " + Back.RED + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
#             winsound.PlaySound(hr2_chime_path, winsound.SND_ASYNC)
#         # play hour marker special aud
#     elif elapsed_min != 0 and elapsed_min % 15 == 0:
#         elapsed_quarters += 1
#         if elapsed_quarters == 1 :
#             # play audio for 1st carillion
#             winsound.PlaySound(carillion1_path, winsound.SND_ASYNC)
#             #  text for 1st is same as 3rd quarter
#             print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
#         elif elapsed_quarters == 2:
#             # half carillion
#             winsound.PlaySound(carillion2_path, winsound.SND_ASYNC)
#             # update current time for display purposes
#             current_time = datetime.datetime.now()
#             print(Back.YELLOW + Fore.BLACK + str(elapsed_min) + Style.RESET_ALL + " min elapsed " + Back.YELLOW + "--- --- ---" + Style.RESET_ALL + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
#         elif elapsed_quarters == 3:
#             # 3rd quarter carillion
#             winsound.PlaySound(carillion3_path, winsound.SND_ASYNC)
#             # text for 3rd quarter same as 1st
#             print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
#         # play nyas based on elapsed time
#     else:
#         print(str(elapsed_min) + " min...")

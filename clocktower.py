import time
import datetime 
# import colorama
# from colorama import Fore, Back, Style
# colorama.init()
import winsound

cou1 = 0
c_t = datetime.datetime.now()

print(c_t)
print("---")
print("curr min ... %s." % c_t.minute)

# while cou1 < 5:
#   c_t = datetime.datetime.now()
#   if c_t.second % 5 == 0:
#     print("+1 for divisor of 5 seconds!")
#     print(str(c_t.minute) + " mins at " + str(c_t.second) + " seconds")
#     cou1 += 1
#     time.sleep(3)

while True:
  # constantly scan for the current time
  c_t = datetime.datetime.now()
  # check for what hour it is
  if c_t.minute == 0:
    curr_hr = datetime.datetime.now().hour
    # NOTE: custom chimes for hours can be set in the below conditional
    winsound.PlaySound("clock_auds/westminster_hr.wav", winsound.SND_FILENAME)
    # limit to 12 hours for the chime-bonging
    if curr_hr > 12:
      curr_hr = (curr_hr - 12)
    # make a bong sound for each hour detected
    for bong in range(0, curr_hr):
      winsound.PlaySound("clock_auds/hourlyNya.wav", winsound.SND_FILENAME)
    time.sleep(750)
  elif c_t.minute == 45:
    # Aud plays on the 45 minute mark
    winsound.PlaySound("clock_auds/westminster_45.wav", winsound.SND_ASYNC)
    # sleep almost 15 mins before checking again
    time.sleep(880)
  elif c_t.minute == 30:
    winsound.PlaySound("clock_auds/westminster_30.wav", winsound.SND_ASYNC)
    # sleep almost 15 mins before checking again
    time.sleep(880)
  elif c_t.minute == 15:
    winsound.PlaySound("clock_auds/westminster_15.wav", winsound.SND_ASYNC)
    # sleep almost 15 mins before checking again
    time.sleep(880)


# /////////
# print(datetime.datetime.now().hour)
# winsound.PlaySound("clock_auds/westminster_hr.wav", winsound.SND_FILENAME)

# for bong in range(0, 3):
#       winsound.PlaySound("clock_auds/hourlyNya.wav", winsound.SND_FILENAME)

# time.sleep(10)

# print("test over")

# ///////////

# POMIDORO
# Adjust, run a pomidoro timer, 30 min work, 10 break
#  how to open youtube from python? Check udemy classes
# CLOCK TOWER RELATED TO REAL TIME
#  track internal clock , playing nya each time hour?
# check if the time.minute == 14 and time.second == 00
# play chime

# ///////////
# winsound.PlaySound("clock_auds/1weirdNya.wav", winsound.SND_ASYNC)
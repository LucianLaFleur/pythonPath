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
#  iterate out time buffer to variables
current_time = datetime.datetime.now()

print("Start " + str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second))
# put in update time adjust below, then for the sleep amount
print("Beginning timer: updates every 5 mins \n ---")

elapsed_min = 0
elapsed_quarters = 0
elapsed_hr = 0
while True:
    #  move to 360 to be every 5 mins
    time.sleep(5)
    elapsed_min += 5
    # 60 for each hr
    if (elapsed_min % 60) == 0:
        elapsed_quarters -= 3
        elapsed_hr += 1
        if elapsed_hr == 1:
            # hourly chime
            print(Fore.YELLOW + Back.CYAN + str(elapsed_hr) + Style.RESET_ALL + " hour elapsed " + Back.CYAN + "--- --- ---" + Style.RESET_ALL)
            winsound.PlaySound("clock_auds/4weirdNya.wav", winsound.SND_FILENAME)
            winsound.PlaySound("clock_auds/hourlyNya.wav", winsound.SND_ASYNC)
        else: 
            print(Fore.RED + Back.WHITE + str(elapsed_hr) + Style.RESET_ALL + " hours have elapsed " + Back.RED + "--- --- ---" + Style.RESET_ALL)
            winsound.PlaySound("clock_auds/awooShort.wav", winsound.SND_FILENAME)
        # play hour marker special aud
    elif elapsed_min != 0 and elapsed_min % 15 == 0:
        elapsed_quarters += 1
        if elapsed_quarters == 1 :
            # play audio for 1st carillion
            winsound.PlaySound("clock_auds/1weirdNya.wav", winsound.SND_ASYNC)
            #  text for 1st is same as 3rd quarter
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        elif elapsed_quarters == 2:
            # half carillion
            winsound.PlaySound("clock_auds/2weirdNya.wav", winsound.SND_ASYNC)
            print(Back.YELLOW + Fore.BLACK + str(elapsed_min) + Style.RESET_ALL + " min elapsed " + Back.YELLOW + "--- --- ---" + Style.RESET_ALL)
        elif elapsed_quarters == 3:
            # 3rd quarter carillion
            winsound.PlaySound("clock_auds/3weirdNya.wav", winsound.SND_ASYNC)
            # text for 3rd quarter same as 1st
            print(Back.MAGENTA + str(elapsed_min) + Style.RESET_ALL + " min Completed!")
        # play nyas based on elapsed time
    else:
        print(str(elapsed_min) + " min...")

# ///////////
# Stopwatch from Tkinter /////////////

# from Tkinter import *
# import time

# def Main():
#     global root

#     root = Tk()
#     root.title("Stopwatch")
#     width = 600
#     height = 200
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     x = (screen_width / 2) - (width / 2)
#     y = (screen_height / 2) - (height / 2)
#     root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#     Top = Frame(root, width=600)
#     Top.pack(side=TOP)
#     stopWatch = StopWatch(root)
#     stopWatch.pack(side=TOP)
#     Bottom = Frame(root, width=600)
#     Bottom.pack(side=BOTTOM)
#     Start = Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
#     Start.pack(side=LEFT)
#     Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
#     Stop.pack(side=LEFT)
#     Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
#     Reset.pack(side=LEFT)
#     Exit = Button(Bottom, text='Close', command=stopWatch.Exit, width=10, height=2)
#     Exit.pack(side=LEFT)
#     Title = Label(Top, text="Stopwatch For Beginners", font=("arial", 18), fg="white", bg="black")
#     Title.pack(fill=X)
#     root.config(bg="black")
#     root.mainloop()


# class StopWatch(Frame):

#     def __init__(self, parent=None, **kw):
#         Frame.__init__(self, parent, kw)
#         self.startTime = 0.0
#         self.nextTime = 0.0
#         self.onRunning = 0
#         self.timestr = StringVar()
#         self.MakeWidget()

#     def MakeWidget(self):
#         timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="green", bg="black")
#         self.SetTime(self.nextTime)
#         timeText.pack(fill=X, expand=NO, pady=2, padx=2)

#     def Updater(self):
#         self.nextTime = time.time() - self.startTime
#         self.SetTime(self.nextTime)
#         self.timer = self.after(50, self.Updater)

#     def SetTime(self, nextElap):
#         minutes = int(nextElap / 60)
#         seconds = int(nextElap - minutes * 60.0)
#         miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
#         self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

#     def Start(self):
#         if not self.onRunning:
#             self.startTime = time.time() - self.nextTime
#             self.Updater()
#             self.onRunning = 1

#     def Stop(self):
#         if self.onRunning:
#             self.after_cancel(self.timer)
#             self.nextTime = time.time() - self.startTime
#             self.SetTime(self.nextTime)
#             self.onRunning = 0

#     def Exit(self):
#             root.destroy()
#             exit()

#     def Reset(self):
#         self.startTime = time.time()
#         self.nextTime = 0.0
#         self.SetTime(self.nextTime)

# if __name__ == '__main__':
#     Main()


#  additions to construct Miss-HM's song for hour-counter
#  westminster chimes 4 versions
# For each hour "bong"
#  https://www.youtube.com/watch?v=eEKUdugY6Yo 
# Alt version with the sound of NTW firing?
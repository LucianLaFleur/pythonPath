# import time

# # s, m, hr placeholders
# ts = 55
# tm = 59
# th = 1

# while True:
#     # zfill forces 2 digits to always appear
#     print(str(th).zfill(2)+ ":"+ str(tm).zfill(2)+":"+ str(ts).zfill(2))
#     ts += 1
#     time.sleep(1)
#     if ts == 60:
#         ts = 0
#         tm += 1
#     if tm == 60:
#         tm = 0
#         th += 1

#  additions to construct Miss-HM's song for hour-counter
#  westminster chimes 4 versions
# For each hour "bong"
#  https://www.youtube.com/watch?v=eEKUdugY6Yo 
# Alt version with the sound of NTW firing?

# make presets "t" for 30 mins, "f" for fifteen, "h" for 1 hr
# Adjust, run a pomidoro timer, 30 min work, 10 break

print('Enter countdown seconds: ')
in_num = input()

# loop from ten to zero by a step of -1 each iteration 
def countdown(in_num):
    for i in range(in_num, 0, -1):
        print(i)

# input condiitionals, presets for 30 min or 1hr countdown, or custom input available


# ///////////

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
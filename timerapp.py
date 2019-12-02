import time

# s, m, hr placeholders
ts = 55
tm = 59
th = 1

while True:
    # zfill forces 2 digits to always appear
    print(str(th).zfill(2)+ ":"+ str(tm).zfill(2)+":"+ str(ts).zfill(2))
    ts += 1
    time.sleep(1)
    if ts == 60:
        ts = 0
        tm += 1
    if tm == 60:
        tm = 0
        th += 1

#  additions to construct Miss-HM's song for hour-counter
#  westminster chimes 4 versions
# For each hour "bong"
#  https://www.youtube.com/watch?v=eEKUdugY6Yo 
# Alt version with the sound of NTW firing?
# 
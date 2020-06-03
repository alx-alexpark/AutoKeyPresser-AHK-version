from ahk import AHK
import time

ahk = AHK()


presskey = input("What Key to Spam Press???\n>")
times = float(input("how many times to press?? If infinity type -1\n>"))
delaytime = float(input("What delay Between Pressing Keys?(seconds)\n>"))
input("press enter to continue")


for count in range(3, 0, -1):
    print(count)
    time.sleep(1)


if times == -1:
    while True:
        ahk.key_down(presskey)
        ahk.key_up(presskey)
        #keyboard.send(delaytime)
        time.sleep(delaytime)
elif times >= 0:
    for number in range(times):
        ahk.key_down(presskey)
        ahk.key_up(presskey)
        #keyboard.send(presskey)
        time.sleep(delaytime)
else:
    print("ERROR")

    

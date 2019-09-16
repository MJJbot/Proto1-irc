import subprocess
from threading import Thread, Lock
import time
import irc_bot

def run_pro(channel):
    #proc = subprocess.Popen(['python3', 'irc_bot.py', channel])
    th = Thread(target=irc_bot.main, args=(channel, ))
    th.start()
    #return proc

processes = []
channels = ['handongsuk', 'looksam']

for i in channels:
    print("exec bot to " + i)
    proc = run_pro(i)
    #processes.append(proc)

# for proc in processes:
#     proc.communicate()


import subprocess
import time

def run_pro(channel):
    proc = subprocess.Popen(['python3', 'irc_bot.py', channel])
    return proc

processes = []
channels = ['handongsuk', 'looksam']

for i in channels:
    print("exec bot to " + i)
    proc = run_pro(i)
    processes.append(proc)

for proc in processes:
    proc.communicate()


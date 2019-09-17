from threading import Thread
import time
import irc_bot

bots = []

def run_thread(channel):
    # bot = irc_bot()
    th = Thread(target=irc_bot.main, args=(channel, ))
    th.start()

    return th

# def disconn_bot(channel, thread):
#     thread.

processes = []
channels = ['saddummy', 'lol_crown', 'rhdgurwns']

for i in channels:
    thread = run_thread(i)
    #processes.append(proc)



# for proc in processes:
#     proc.communicate()


'''
ShellOS Build 202106002
Powered by IDLE Studios
'''
import os
import sys
import time

Floder = "/disk/0/"
cmd = ''
cmd_split = []

print('ShellOS Boot Compeleted')
cmd = input(Floder)

while True:
    cmd_split = cmd.split(cmd)

    if cmd_split[0] == "cd":
        if len(cmd_split) == '1':
            print('无效目录，请重试')
            pass
        else:
            Floder = cmd_split[1]
        pass
    elif cmd_split[0] == 'shutdown':
        if len(cmd_split) == '2':
            if cmd_split[1] == "-r":
                print('系统将在60秒后重启')
                time.sleep(50)
                print('系统将在10秒后重启')
                time.sleep(10)
                os.system('start ShellOS_CLauncher.exe')
                sys.exit()
                pass
            pass
        else:
            sys.exit()
        pass
    elif cmd_split[0] == 'cmd':
        os.system("start cmd")
        pass


'''
ShellOS Build 202106003
Powered by IDLE Studios
'''
import os
import sys
import time

Floder = "/disk/0/"
cmd = ''
cmd_split = []
debug = False
cmd = input(Floder)

print('ShellOS Boot Compeleted')

#函数库
def sims(mode):
    if mode == 'linux':
        os.system(r'start \apps\sims\linux.exe')
        pass
    else:
        os.system(r'start \apps\sims\sim.exe')
        pass
    pass





def cmd_filter():
    cmd_split = cmd.split(cmd)
    if debug == True:
        print(cmd_split)

    #选择目录
    if cmd_split[0] == "cd":
        if len(cmd_split) == '1':
            print('无效目录，请重试')
            pass
        else:
            Floder = cmd_split[1]
        pass

    #关闭系统或重启
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
    
    #启动cmd
    elif cmd_split[0] == 'cmd':
        os.system("start cmd")
        pass
    elif cmd_split[0] == 'sims':
        if len(cmd_split) == 2:
            sims(cmd_split[1])
            pass
        pass
    pass

while True:
    cmd_filter()
    pass

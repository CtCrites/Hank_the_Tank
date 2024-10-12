import time as tipy
import random
import os

def rock():
    os.system("echo '             ________                                   ________                '")
    os.system("echo '       _____/  ______}                                 {______  \_____          '")
    os.system("echo '              (______}                                 {______)                 '")
    os.system("echo '             (_______}                                 {_______)                '")
    os.system("echo '       ____    (_____}                                 {_____)    ____          '")
    os.system("echo '           \__(_____}                                   {_____)__/              '")
    os.system("echo '                                                                                '")
    return
    
def paper():
    os.system("echo '                                                                                '")
    os.system("echo '       ______________                                    ______________         '")
    os.system("echo '    __/    ________)__)                                (__(________    \__      '")
    os.system("echo '    __  _{_____}                                              (_____}_  __      '")
    os.system("echo '      ---                                                            ---        '")
    os.system("echo '                                                                                '")
    return
    
def scissors():
    os.system("echo '        __________                                       __________             '")
    os.system("echo '  _____/  ________}                                     (________  \_____       '")
    os.system("echo '      \  \ \_____                                         _____| /  /           '")
    os.system("echo '       \  \ ______}                                     (______ /  /            '")
    os.system("echo '  _____ (v    }                                             {    v) _____       '")
    os.system("echo '       \_(___}                                               {___)_/            '")
    os.system("echo '                                                                                '")
    return
    
def rvp():
    os.system("echo '             ________                                                           '")
    os.system("echo '       _____/  ______}                                   ______________         '")
    os.system("echo '              (______}                                 (__(________    \__      '")
    os.system("echo '             (_______}                                        (_____}_  __      '")
    os.system("echo '       ____    (_____}                                                ---       '")
    os.system("echo '           \__(_____}                                                           '")
    os.system("echo '                                                                                '")
    return
  
def rvs():
    os.system("echo '             ________                                    __________             '")
    os.system("echo '       _____/  ______}                                  (________  \_____       '")
    os.system("echo '              (______}                                    _____| /  /           '")
    os.system("echo '             (_______}                                  (______ /  /            '")
    os.system("echo '       ____    (_____}                                      {    v) _____       '")
    os.system("echo '           \__(_____}                                        {___)_/            '")
    os.system("echo '                                                                                '")
    return
    
def pvr():  
    os.system("echo '                                                        ________                '")
    os.system("echo '       ______________                                  {______  \_____          '")
    os.system("echo '    __/    ________)__)                                {______)                 '")
    os.system("echo '    __  _{_____}                                       {_______)                '")
    os.system("echo '     ---                                               {_____)    ____          '")
    os.system("echo '                                                        {_____)__/              '")
    os.system("echo '                                                                                '")
    return
    
def pvs():
    os.system("echo '                                                         __________             '")
    os.system("echo '       ______________                                   (________  \_____       '")
    os.system("echo '    __/    ________)__)                                   _____| /  /           '")
    os.system("echo '    __  _{_____}                                        (______ /  /            '")
    os.system("echo '      ---                                                   {    v) _____       '")
    os.system("echo '                                                             {___)_/            '")
    os.system("echo '                                                                                '")
    return

def svr():
    os.system("echo '        __________                                      ________                '")
    os.system("echo '  _____/  ________}                                    {______  \_____          '")
    os.system("echo '      \  \ \_____                                      {______)                 '")
    os.system("echo '       \  \ ______}                                    {_______)                '")
    os.system("echo '  _____ (v    }                                        {_____)    ____          '")
    os.system("echo '       \_(___}                                          {_____)__/              '")
    os.system("echo '                                                                                '")
    return

def svp():
    os.system("echo '        __________                                                              '")
    os.system("echo '  _____/  ________}                                      ______________         '")
    os.system("echo '      \  \ \_____                                      (__(________    \__      '")
    os.system("echo '       \  \ ______}                                           (_____}_  __      '")
    os.system("echo '  _____ (v    }                                                      ---        '")
    os.system("echo '       \_(___}                                                                  '")
    os.system("echo '                                                                                '")
    return


    
def rpsanimate():
    os.system("clear")
    rock()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    rock()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    rock()
    os.system("echo '                                   ROCK                                         '")
    tipy.sleep(0.5)
    
    
    os.system("clear")
    paper()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    paper()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    paper()
    os.system("echo '                                  PAPER                                        '")
    tipy.sleep(0.5)
    
    os.system("clear")
    scissors()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    scissors()
    tipy.sleep(0.25)
    os.system("clear")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    os.system("echo ''")
    scissors()  
    os.system("echo '                                 SCISSORS                                       '") 
    tipy.sleep(0.5)
    os.system("echo '                                  SHOOT!                                        '")
    return

def RPSgame():
    #Hank()
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    m = int(input("Make your choice for your move: "))
    hm = random.randint(1,3)
    rpsanimate()
    tipy.sleep(1)
    if m == 1 and hm == 1:
       os.system("clear")
       rock()
       os.system("echo '                                    TIE                                         '")
       input()
    elif m == 1 and hm == 2:
       os.system("clear")
       rvp()
       os.system("echo '                                YOU LOSE!                                        '")
       input()
    elif m == 1 and hm == 3:
       os.system("clear")
       rvs()
       os.system("echo '                                 YOU WIN!                                        '")
       input()
    elif m == 2 and hm == 1:
       os.system("clear")
       pvr()
       os.system("echo '                                 YOU WIN!                                        '")
       input()
    elif m == 2 and hm == 2:
       os.system("clear")
       paper()
       os.system("echo '                                     TIE                                         '")
       input()
    elif m == 2 and hm == 3:
       os.system("clear")
       pvs()
       os.system("echo '                                 YOU LOSE!                                       '")
       input()
    elif m == 3 and hm == 1:
       os.system("clear")
       svr()
       os.system("echo '                                 YOU LOSE!                                       '")
       input()
    elif m == 3 and hm == 2:
       os.system("clear")
       svp()
       os.system("echo '                                 YOU WIN!                                        '")
       input()
    elif m == 3 and hm == 3:
       os.system("clear")
       scissors()
       os.system("echo '                                      TIE                                        '")
       input()
    x = input("Would you like to play again? [y/n]: ")
    if x == 'y' or x == 'Y':
       RPSgame()
    return

import webbrowser

from colorama import init
from colorama import Fore
init()

import time

while True:
    print(print(Fore.LIGHTWHITE_EX),'Kакой предмет тебе нужен ?')
    print(Fore.LIGHTRED_EX,'1 - ВМ лекция','2 - ВМ практика',Fore.LIGHTYELLOW_EX,'3 - Укр.яз лекция', '4 - Укр.яз практика',Fore.LIGHTGREEN_EX,'5 - Физика лекция','6 - Физика практика ',Fore.LIGHTCYAN_EX,'7 - ОАОИ лекция','8 - ОАОИ практика ',Fore.MAGENTA,'100 - Stop', sep='\n')
    subject = int(input('Your number: '))
    if subject == 1:
        print('ВМ лекция, открываю!')
        webbrowser.open_new_tab('https://meet.google.com/nmd-nzjm-dqp?authuser=1&pli=1')
    elif subject == 2:
        print('ВМ прак., открываю!')
        webbrowser.open('https://meet.google.com/nmd-nzjm-dqp?authuser=1&pli=1')
    elif subject == 3:
        print('Укр.яз лекция, открываю!')
        webbrowser.open('https://meet.google.com/vdr-hysi-jvf?authuser=1')
    elif subject == 4:
        print('Укр.яз практика, открываю!')
        webbrowser.open('https://meet.google.com/hgp-jdgt-ycf?authuser=1&hs=179')
    elif subject == 5:
        print('Физика лекция, открываю!')
        webbrowser.open('https://meet.google.com/pym-iprr-yho?authuser=1')
    elif subject == 6:
        print('Физика практика открываю!')
        webbrowser.open('https://meet.google.com/myh-cbau-axt?authuser=1&hs=179')
    elif subject == 7:
        print('ОАОИ лекция, открываю!')
        webbrowser.open_new_tab('https://meet.google.com/uqr-ymaz-dcx?authuser=1')
    elif subject == 8:
        print('ОАОИ практика, открываю!')
        webbrowser.open_new_tab('https://meet.google.com/xeb-czfm-jtr?authuser=1')
    elif subject == int(100):
        print('Закрываюсь!')
        time.sleep(1)
        break
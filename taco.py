from datetime import datetime
from platform import node, system, architecture, uname
from getpass import getuser
from socket import gethostname, gethostbyname
import socket
from os import system

system('clear')

TACOTIME = '5' # weekday of taco day | default is 5 (friday)

def internet():
    try:
        socket.setdefaulttimeout(0.1)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('8.8.8.8', 53))
        return 'Good'
    except socket.error as ex:
        print(ex)
        return 'Bad'

def colored(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

now = datetime.now()

month = str(now.now().month)
day = str(now.now().day)
hour = str(now.now().hour)
minute = str(now.now().minute)
second = str(now.now().second)

if str(datetime.today().weekday()) == TACOTIME:
    node = 'TACO-TIME!'
else:
    node = node()

release = uname().release.split('.')

if len(hour) == 1: hour += "0"
if len(minute) == 1: minute += "0"
if len(second) == 1: second += "0"

print(f'''
  {colored(128,128,128)}  ╭╯╭╯╭╯     {colored(255,255,255)}│ {getuser()}{colored(241, 195, 68)}@{colored(255,255,255)}{node}
  {colored(241, 195, 68)} ╱▔▔▔▔▔╲▔╲   {colored(255,255,255)}├───────────────────
  {colored(241, 195, 68)}╱┈╭╮┈╭╮┈╲{colored(181, 201, 54)}╮{colored(241, 195, 68)}╲  {colored(255,255,255)}│ Arch{colored(241, 195, 68)}: {colored(255,255,255)}{architecture()[0]}
  {colored(241, 195, 68)}▏┈▂▂▂▂▂┈▕{colored(181, 201, 54)}╮{colored(241, 195, 68)}▕  {colored(255,255,255)}│ Release{colored(241, 195, 68)}: {colored(255,255,255)}{release[0]}.{release[1]}
  {colored(241, 195, 68)}▏┈╲▂▂▂╱┈▕{colored(181, 201, 54)}╮{colored(241, 195, 68)}▕  {colored(255,255,255)}│ Connection{colored(241, 195, 68)}: {colored(255,255,255)}{internet()}
  {colored(241, 195, 68)}╲▂▂▂▂▂▂▂▂╲╱  {colored(255,255,255)}│ Time{colored(241, 195, 68)}: {colored(255,255,255)}{hour}:{minute}:{second}
''')

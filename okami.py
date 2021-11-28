import os
from colorama import Fore, Back
import datetime
import platform
import getpass
import random

def get_datetime():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    if len(hour) == 1: hour += "0"
    if len(minute) == 1: minute += "0"
    if len(second) == 1: second += "0"

    if len(month) == 1: month += "0"
    if len(day) == 1: day += "0"

    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
    }

def get_computer():
    user = getpass.getuser()
    
    system = platform.system()
    while len(system) == 12 == False: system = str(system) + ' '

    architecture = platform.architecture()
    while len(architecture) == 12 == False: architecture = str(architecture) + ' '

    node = platform.node()
    while len(node) == 12 == False: node = str(node) + ' '

    return {
        "type": system,
        "architecture": architecture[0],
        "user": user,
        "system": node,
    }


symbols1 = 'ぁ あ ぃ い ぅ う ぇ え ぉ お か が き ぎ く ぐ け げ こ ご さ ざ し じ す ず せ ぜ そ ぞ た だ ち ぢ っ つ づ て で と ど な に ぬ ね の は ば ぱ ひ び ぴ ふ ぶ ぷ へ べ ぺ ほ ぼ ぽ ま み'.split()
symbols2 = 'ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄸ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅃ ㅄ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅥ ㅦ ㅧ ㅨ ㅩ ㅪ ㅫ ㅬ ㅭ ㅮ ㅯ ㅰ ㅱ ㅲ ㅳ ㅴ ㅵ ㅶ ㅷ ㅸ ㅹ ㅺ ㅻ ㅼ ㅽ ㅾ ㅿ ㆀ ㆁ ㆂ ㆃ ㆄ ㆅ ㆆ ㆇ ㆈ ㆉ ㆊ'.split()

def ranchars(type):
    craft = ''
    for __ in range(7):    craft += random.choice(type)
    return craft

def ranchars2(type, amount):
    craft = ''
    for __ in range(amount):    craft += random.choice(type)
    return craft

os.system('clear')

print(f"""{Fore.LIGHTCYAN_EX}
          ╭────────────────╮ {Fore.LIGHTCYAN_EX}╭───────────────────────────╮ ╭────────────────╮
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}Type{Fore.LIGHTCYAN_EX}:          {Fore.LIGHTWHITE_EX}{get_computer()["type"]}  {Fore.LIGHTCYAN_EX}    │ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}Architecture{Fore.LIGHTCYAN_EX}:  {Fore.LIGHTWHITE_EX}{get_computer()["architecture"]}  {Fore.LIGHTCYAN_EX}    │ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}User{Fore.LIGHTCYAN_EX}:          {Fore.LIGHTWHITE_EX}{get_computer()["user"]}     {Fore.LIGHTCYAN_EX} │ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}System{Fore.LIGHTCYAN_EX}:        {Fore.LIGHTWHITE_EX}{get_computer()["system"]} {Fore.LIGHTCYAN_EX}    │ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}╰───────────────────────────╯ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}╭───────────────────────────╮ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}Date{Fore.LIGHTCYAN_EX}:   {Fore.LIGHTWHITE_EX}{get_datetime()["year"]}{Fore.LIGHTCYAN_EX}:{Fore.LIGHTWHITE_EX}{get_datetime()["month"]}{Fore.LIGHTCYAN_EX}:{Fore.LIGHTWHITE_EX}{get_datetime()["day"]}{Fore.LIGHTCYAN_EX}        │ │ {ranchars(symbols2)} │
          │ {ranchars(symbols1)} │ {Fore.LIGHTCYAN_EX}│ {Fore.LIGHTWHITE_EX}Time{Fore.LIGHTCYAN_EX}:   {Fore.LIGHTWHITE_EX}{get_datetime()["hour"]}{Fore.LIGHTCYAN_EX}:{Fore.LIGHTWHITE_EX}{get_datetime()["minute"]}{Fore.LIGHTCYAN_EX}:{Fore.LIGHTWHITE_EX}{get_datetime()["second"]}{Fore.LIGHTCYAN_EX}          │ │ {ranchars(symbols2)} │
          ╰────────────────╯ {Fore.LIGHTCYAN_EX}╰───────────────────────────╯ ╰────────────────╯
          ╭─────────────────────────────────────────────────────────────────╮
          │ {ranchars2('▁▂▃▄▅▆▇', 63)} │
          ╰─────────────────────────────────────────────────────────────────╯
""")

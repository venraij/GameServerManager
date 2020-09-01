import os
from checkSteamCmd import setup_steam_cmd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def setup_tool():
    try:
        os.system("python -m pip install wget winshell Dispatch pywin32")
        os.system("pip install py-steamcmd-wrapper")
        os.system("pywin32-228.win32-py3.8.exe")
        os.system("pywin32-228.win-amd64-py3.8.exe")
    except OSError as e:
        print('Failed installation of dependencies.')
        print(e)

    try:
        os.makedirs(os.path.join(os.getcwd(), "steamcmd"))
    except OSError as e:
        print("SteamCMD folder already exists.")
        print(e)

    setup_steam_cmd()

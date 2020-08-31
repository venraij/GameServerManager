import os
from pysteamcmdwrapper import SteamCMD

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setupSteamCmd():
    s = SteamCMD(os.path.join(os.getcwd(),"steamcmd"))
    try:
        s.install()
    except:
        print("SteamCMD already installed.")


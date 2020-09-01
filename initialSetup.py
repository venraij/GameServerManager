import os, sys
from checkSteamCmd import setupSteamCmd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setupTool():
    try:
        os.system("python pip install wget zipfile os shutil sys time winshell Dispatch UPnPy socket py-steamcmd-wrapper pywin32 pypiwin32")
        os.system("python pywin32_postinstall.py -install")
    except:
        print('Failed installation of dependencies.')

    try:
        os.makedirs(os.path.join(os.getcwd(),"steamcmd"))
    except:
        print("SteamCMD folder already exists.")
        
    setupSteamCmd();

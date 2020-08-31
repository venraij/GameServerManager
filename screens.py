from arma3 import arma3MainMenu

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mainMenu ():
    print("\n")
    print('###############################')
    print("# /// More Servers Coming /// #")
    print("# 1) Life is Feudal: Your Own #")
    print("# 2) Rust                     #")
    print("# 3) Arma 3                   #")
    print("# 4) Exit                     #")
    print('###############################')
    num = input(" Select menu option: ")

    if num == "1":
        lif()

    elif num == '2':
        rust()

    elif num == '3':
        arma3MainMenu()

def rust():
    print("\n")
    print('####################################')
    print("# 1) Install Rust Server           #")
    print("# 2) Delete Rust Server            #")
    print("# 3) Update Rust Server            #")
    print("# 4) Start server                  #")
    print("# 5) Main Menu                     #")
    print('####################################')
    num = input(" Select a menu option: ")

    if num == '1':
        rustinstall()

    elif num == '2':
        rustdelete()

    elif num == '3':
        rustupdate()

    elif num == '4':
        startrust()

    elif num == '5':
        mainmenu()

def lif ():
    print("\n")
    print('####################################')
    print("# 1) Install Life is Feudal Server #")
    print("# 2) Delete Life is Feudal Server  #")
    print("# 3) Update Life is Feudal Server  #")
    print("# 4) Start Life is Feudal Server   #")
    print("# 5) Main Menu                     #")
    print('####################################')
    num = input(" Select a menu option: ")

    if num == "1":
        g = 'Lif'
        lifinstall()

    elif num == "2":
        removeserverlif()

    elif num == '3':
        lifupdate()

    elif num == '4':
        lifrun()

    elif num == '5':
        mainmenu()

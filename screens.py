from arma3 import arma3_main_menu

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main_menu():
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
        arma3_main_menu()


def rust():
     print("\n")
#     print('####################################')
#     print("# 1) Install Rust Server           #")
#     print("# 2) Delete Rust Server            #")
#     print("# 3) Update Rust Server            #")
#     print("# 4) Start server                  #")
#     print("# 5) Main Menu                     #")
#     print('####################################')
#     num = input(" Select a menu option: ")
#
#     if num == '1':
#         rust_install()
#
#     elif num == '2':
#         rust_delete()
#
#     elif num == '3':
#         rust_update()
#
#     elif num == '4':
#         rust_start()
#
#     elif num == '5':
#         main_menu()
#
#
def lif():
     print("\n")
#     print('####################################')
#     print("# 1) Install Life is Feudal Server #")
#     print("# 2) Delete Life is Feudal Server  #")
#     print("# 3) Update Life is Feudal Server  #")
#     print("# 4) Start Life is Feudal Server   #")
#     print("# 5) Main Menu                     #")
#     print('####################################')
#     num = input(" Select a menu option: ")
#
#     if num == "1":
#         g = 'Lif'
#         lif_install()
#
#     elif num == "2":
#         lif_remove()
#
#     elif num == '3':
#         lif_update()
#
#     elif num == '4':
#         lif_run()
#
#     elif num == '5':
#         main_menu()

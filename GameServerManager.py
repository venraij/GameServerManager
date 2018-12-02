import wget
import zipfile
import os
import shutil
import sys
import time

user = os.getlogin()
directory1 = "C:/Users/" + user + "/Desktop/GameServerManager/Servers/Lif/SteamCMD"
directory2 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/docs'
directory3 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif'

def mainmenu ():
    print('###############################')
    print("# /// More Servers Coming /// #")
    print("# 1) Life is Feudal: Your Own #")
    print("# 2) Exit                     #")
    print('###############################')
    num = input(" Select menu option: ")

    if num == "1":
        lif()
    else:
        quit()

def lif ():
    print('####################################')
    print("# 1) Install Life is Feudal Server #")
    print("# 2) Delete Life is Feudal Server  #")
    print("# 3) Update Life is Feudal Server  #")
    print("# 4) Main Menu                     #")
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
        mainmenu()

def lifupdate ():
    print("Updating Server...")
    with open(os.path.join(directory1, 'ServerUpdate.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/steamcmd.exe +login anonymous +force_install_dir C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif +app_update 320850 validate +quit'])
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/ServerUpdate.bat')

def lifinstall ():
    print('Creating folders...')
    os.makedirs('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD')

    print("Downloading SteamCMD...")
    wget.download('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip', 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD')

    print('Extracting SteamCMD...')
    with zipfile.ZipFile('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/steamcmd.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD')

    print("Installing SteamCMD...")
    with open(os.path.join(directory1, 'ServerInstall.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/steamcmd.exe +login anonymous +force_install_dir C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif +app_update 320850 +quit'])

    print('Downloading server files...')
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/ServerInstall.bat')

    print('Downloading MariaDB...')
    wget.download('http://mirror.i3d.net/pub/mariadb//mariadb-5.5.62/winx64-packages/mariadb-5.5.62-winx64.msi', 'C:/Users/' + user + '/Downloads')

    print('Installing MariaDB...')
    print('Follow the installation instructions')
    print('SET FORMAT TO UTF-8')
    print('CHECK ACCES ROOT REMOTELY')
    os.system('C:/Users/' + user + '/Downloads/mariadb-5.5.62-winx64.msi')
    passw = input('Enter MariaDB root password:')

    print('Setting up MariaDB...')
    with open(os.path.join(directory2, 'config_local.cs'), 'w') as OPATH:
        OPATH.writelines(['$cm_config::DB::Connect::server =   "127.0.0.1:3306"; // server IP or domain name. Can enter port if it is not default\n'
                          '$cm_config::DB::Connect::user =     "root"; // MUST be a user with ROOT privileges in order to create new DBs\n'
                          '$cm_config::DB::Connect::password =  "' + passw + '"; // password for that user'])

    with open(os.path.join(directory3, 'config_local.cs'), 'w') as OPATH:
        OPATH.writelines(['$cm_config::DB::Connect::server =   "127.0.0.1:3306"; // server IP or domain name. Can enter port if it is not default\n'
                          '$cm_config::DB::Connect::user =     "root"; // MUST be a user with ROOT privileges in order to create new DBs\n'
                          '$cm_config::DB::Connect::password =  "' + passw + '"; // password for that user'])

    print('1)Search for HeidiSQL in the start menu and open it.\n'
          '2)Create a new session called LIF.\n'
          '3)Click the "Open" button.\n'
          '4)Click "Login"')
    input('Enter "Y" to continue')

    print('1)In the white space area, Right Click > Create New > Database\n'
          '2)Name Database: lif_1\n'
          '3)Collation: utf8_general_ci\n'
          '4)Right Click (in the white space again) > Refresh')
    input('Enter "Y" to continue')

    print('Updating my.ini file...')
    with open(os.path.join('C:/Program Files/MariaDB 5.5/data', 'my.ini'), 'w') as OPATH:
        OPATH.writelines([
                             '[mysqld]\n'
                             'datadir=C:/Program Files/MariaDB 5.5/data\n'
                             'port=3306\n'
                             'sql_mode="STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"\n'
                             'default_storage_engine=innodb\n'
                             'innodb_buffer_pool_size=2039M\n'
                             'innodb_log_file_size=50M\n'
                             'character-set-server=utf8\n'
                             'innodb_file_per_table=ON\n'
                             'innodb_file_format=Barracuda\n'
                             'innodb_flush_log_at_trx_commit=1\n'
                             'max_sp_recursion_depth=255\n'
                             'max_allowed_packet=10M\n'
                             '\n'
                             'query_cache_size=0\n'
                             'query_cache_type=OFF\n'
                             '\n'
                             '[client]\n'
                             'port=3306'])

    print('Port forward the following ports in your router:\n'
          '28000-28003 UDP and TCP')
    input('Enter "Y" to continue')


    print('Installation Finished: You can acces the server files via your desktop.')
    print('Right click on the server exe and make a shortcut.\n'
          'Then right click on the shortcut and click properties.\n'
          'Put "-world 1" in target after the path.\n'
          'You can edit settings in config/world_1.xml')
    input('Enter "Y" to go back to the menu:')

    lif()

def removeserverlif ():
    print("Removing server files...")
    shutil.rmtree('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif')
    lif()

mainmenu()
import wget
import zipfile
import os
import shutil
import sys
import time

user = os.getlogin()
directory2 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/docs'
directory3 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif'

def mainmenu ():
    print('###############################')
    print("# /// More Servers Coming /// #")
    print("# 1) Life is Feudal: Your Own #")
    print("# 2) Rust                     #")
    print("# 3) Exit                     #")
    print('###############################')
    num = input(" Select menu option: ")

    if num == "1":
        lif()

    elif num == '2':
        rust()

def rust():
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

def lifupdate ():
    print("Updating Server...")
    with open(os.path.join(directory1, 'ServerUpdate.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/steamcmd.exe +login anonymous +force_install_dir C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif +app_update 320850 validate +quit'])
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/SteamCMD/ServerUpdate.bat')
    lif()

def lifinstall ():
    game = 'Lif'
    saveloc = "C:/Users/" + user + "/Desktop"
    permfiles = "/GameServerManager/Servers/" + game
    fullsave = saveloc + permfiles

    print('Creating folders...')
    os.makedirs(fullsave+'/SteamCMD')

    print("Downloading SteamCMD...")
    wget.download('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip', fullsave+'/SteamCMD')

    print('Extracting SteamCMD...')
    with zipfile.ZipFile(fullsave+'/SteamCMD' + '/steamcmd.zip', 'r') as zip_ref:
        zip_ref.extractall(fullsave+'/SteamCMD')

    print("Installing SteamCMD...")
    with open(os.path.join(fullsave + '/SteamCMD', 'ServerInstall.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off \n'
                          + fullsave + '/SteamCMD' + '/steamcmd.exe +login anonymous +force_install_dir '+fullsave+' +app_update 320850 validate +quit'])

    print('Downloading server files...')
    os.system(fullsave+'/SteamCMD/ServerInstall.bat')

    print('Downloading MariaDB...')
    wget.download('http://mirror.i3d.net/pub/mariadb//mariadb-5.5.62/winx64-packages/mariadb-5.5.62-winx64.msi', 'C:/Users/' + user + '/Downloads')

    print('Installing MariaDB...')
    print('Follow the installation instructions')
    print('SET FORMAT TO UTF-8')
    print('CHECK ACCES ROOT REMOTELY')
    os.system('C:/Users/' + user + '/Downloads/mariadb-5.5.62-winx64.msi')
    passw = input('Enter MariaDB root password:')

    ip = input('Enter computer IP:')

    print('Setting up MariaDB...')
    with open(os.path.join(directory2, 'config_local.cs'), 'w') as OPATH:
        OPATH.writelines(['$cm_config::DB::Connect::server =   "'+ip+'"; // server IP or domain name. Can enter port if it is not default\n'
                          '$cm_config::DB::Connect::user =     "root"; // MUST be a user with ROOT privileges in order to create new DBs\n'
                          '$cm_config::DB::Connect::password =  "' + passw + '"; // password for that user'])

    with open(os.path.join(directory3, 'config_local.cs'), 'w') as OPATH:
        OPATH.writelines(['$cm_config::DB::Connect::server =   "'+ip+'"; // server IP or domain name. Can enter port if it is not default\n'
                          '$cm_config::DB::Connect::user =     "root"; // MUST be a user with ROOT privileges in order to create new DBs\n'
                          '$cm_config::DB::Connect::password =  "' + passw + '"; // password for that user'])

    print('1)Search for HeidiSQL in the start menu and open it.\n'
          '2)Create a new session called LIF.\n'
          '3)Change ip to ' + ip + '\n'
          '4)Enter your created password.\n'
          '5)Click the "Open" button.')

    input('Enter "Y" to continue')

    print('1)In the white space area, Right Click > Create New > Database\n'
          '2)Name Database: lif_1\n'
          '3)Collation: utf8_general_ci\n'
          '4)Right Click (in the white space again) > Refresh\n'
          '5)')
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

    with open(os.path.join(directory3, 'StartServer.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off '+ "\n"
            +fullsave +"/ddctd_cm_yo_server.exe"+" -world 1"])

    print('Installation Finished: You can acces the server files via your desktop.')
    print('You can edit settings in config/world_1.xml')
    input('Enter "Y" to go back to the menu:')

    lif()

def lifrun ():
    game = 'Lif'
    saveloc = "C:/Users/" + user + "/Desktop"
    permfiles = "/GameServerManager/Servers/" + game
    fullsave = saveloc + permfiles

    print('Starting Server...')
    os.system(fullsave +'/StartServer.bat')
    lif()

def removeserverlif ():
    print("Removing server files...")
    shutil.rmtree('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif')
    lif()

def rustinstall():
    print('Creating folders...')
    os.makedirs('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD')

    print("Downloading SteamCMD...")
    wget.download('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip', 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD')

    print('Extracting SteamCMD...')
    with zipfile.ZipFile('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/steamcmd.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD')

    print('Removing old files...')
    os.remove('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/steamcmd.zip')

    with open(os.path.join('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD', 'ServerInstall.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/steamcmd.exe +login anonymous +force_install_dir C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust +app_update 258550 validate +quit'])

    print('Downloading server files...')
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/ServerInstall.bat')

    print('Creating command line parameter start file...')
    with open(os.path.join('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust', 'ServerRun.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/RustDedicated.exe -batchmode +server.ip 0.0.0.0 +server.port 28015 +rcon.ip 0.0.0.0 +rcon.web 0 +server.tickrate 10 +server.hostname "GameServerManager" +server.maxplayers 50 +server.worldsize 3000 +server.seed 50000 +server.saveinterval 600 +rcon.password "rconpassword" -logfile gamelog.txt -silent-crashes -'])

    input('You can change the file called "ServerInstall.bat" for server settings. Input "Y" to go back to main menu:')
    rust()

def rustdelete():
    print("Removing server files...")
    shutil.rmtree('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust')
    rust()

def rustupdate ():
    print("Updating Server...")
    with open(os.path.join(directory1, 'ServerUpdate.bat'), 'w') as OPATH:
        OPATH.writelines(['@echo off\n'
                          'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/steamcmd.exe +login anonymous +force_install_dir C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust +app_update 258550 validate +quit'])
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/SteamCMD/ServerUpdate.bat')
    rust()

def startrust():
    os.system('C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust/ServerRun.bat')
    rust()

game = ""
saveloc = "C:/Users/" + user + "/Desktop"
permfiles = "/GameServerManager/Servers/"+game
fullsave = saveloc + permfiles

mainmenu()
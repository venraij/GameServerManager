import subprocess
import sys

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wget", "zipfile", "os", "shutil", "sys" , "time", "winshell", "Dispatch", "upnpy", "pywin32"])
except:
    print()
    
import wget
import zipfile
import os
import shutil
import sys
import time
import winshell
from win32com.client import Dispatch
import upnpy

user = os.getlogin()
directory2 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif/docs'
directory3 = 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Lif'

try:
    os.system("python pywin32_postinstall.py -install")
    
except:
    print()

def mainmenu ():
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
        arma3()


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

def arma3():
    print("\n")
    print('####################################')
    print("# 1) Install Arma 3 Server         #")
    print("# 2) Delete Arma 3 Server          #")
    print("# 3) Update Arma 3 Server          #")
    print("# 4) Start Arma 3 Server           #")
    print("# 5) Main Menu                     #")
    print('####################################')
    num = input(" Select a menu option: ")

    if num == "1":
        arma3Install()

    elif num == "2":
        removeArma3()

    elif num == '3':
        arma3Update()

    elif num == '4':
        arma3Run()

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


def arma3Install():
    game = 'Arma3'
    driveLetter = input('Enter the drive letter to install too: ')
    
    saveloc = driveLetter + ":/Users/" + user + "/Desktop"
    permfiles = "/GameServerManager/Servers/" + game
    fullsave = saveloc + permfiles

    try:
        print('Creating folders...')
        os.makedirs(driveLetter + ":/Apps/Steam")
        os.makedirs(driveLetter + ":/Games/ArmA3/A3Master")
        os.makedirs(driveLetter + ":/Games/ArmA3/A3Files")

        print("Downloading SteamCMD...")
        wget.download('https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip', driveLetter + ':/Apps/Steam')

        print('Extracting SteamCMD...')
        with zipfile.ZipFile(driveLetter + ':/Apps/Steam' + '/steamcmd.zip', 'r') as zip_ref:
            zip_ref.extractall(driveLetter + ':/Apps/Steam')

        print("Installing SteamCMD...")
        with open(os.path.join(driveLetter + ':/Apps/Steam', 'ServerInstall.bat'), 'w') as OPATH:
            OPATH.writelines(['@echo off \n'
                          + driveLetter + ':/Apps/Steam' + '/steamcmd.exe +quit'])

        print("Creating Arma3server_steamcmd.cmd...")
        with open(os.path.join(driveLetter + ':/Games/ArmA3/A3Files', 'Arma3server_steamcmd.cmd'), 'w') as OPATH:
            OPATH.writelines(['@echo off \n' +
                              '@rem http://media.steampowered.com/installer/steamcmd.zip \n' +
                              'SETLOCAL ENABLEDELAYEDEXPANSION \n' +
                              'SET A3serverBRANCH=233780 -beta \n' +
                              'SET A3serverPath=D:\Games\ArmA3\A3Master \n' +
                              'echo. \n' +
                              'echo     You are about to update Arma 3 server \n' +
                              'echo        Dir: %A3serverPath% \n' +
                              'echo        Branch: %A3serverBRANCH% \n' +
                              'echo. \n' +
                              'echo     Key "ENTER" to proceed \n' +
                              'pause \n' +
                               driveLetter + ':\Apps\Steam\steamcmd.exe +login mrnicknick1234 bd16101999WW21945 +force_install_dir ' + driveLetter + ':\Games\ArmA3\A3Master +"app_update 233780" validate +quit \n' +
                              'echo . \n' +
                              'echo     Your Arma 3 server is now up to date \n' +
                              'echo     key "ENTER" to exit \n' +
                              'pause \n'
                              ])

        print("Installing ArmA3 Server...")
        os.system(driveLetter + ':/Games/ArmA3/A3Files/Arma3server_steamcmd.cmd')

    except:
        print("The folders " + driveLetter + ":/Apps/Steam, " + driveLetter + ":/Games/ArmA3/A3Master and " + driveLetter + ":/Games/ArmA3/A3Files already exist.")

    try:
        print("Creating default config file...")
        with open(os.path.join(driveLetter + ':/Games/ArmA3/A3Master', 'CONFIG_server.cfg'), 'w') as OPATH:
            OPATH.writelines([
                                  '// \n'
                                + '// server.cfg \n'
                                + '// \n'
                                + '// comments are written with "//" in front of them. \n'
                                + '\n'
                                + '// NOTE: More parameters and details are available at http://community.bistudio.com/wiki/server.cfg \n'
                                + '\n'
                                + '// STEAM PORTS (not needed anymore, it\'s +1 +2 to gameport) \n'
                                + '// steamPort		= 8766;		// default  8766, needs to be unique if multiple servers are on the same box \n'
                                + '// steamQueryPort	= 27016;	// default 27016, needs to be unique if multiple servers are on the same box \n'
                                + '\n'
                                + '// GENERAL SETTINGS \n'
                                + 'hostname = "Created with GameServerManager";	// Name of the server displayed in the public server list \n'
                                + '//password		= "password";		// Password required to join the server (remove // at start of line to enable) \n'
                                + 'passwordAdmin	= "AdminPassword";		// Password to login as admin. Open the chat and type: #login password \n'
                                + 'maxPlayers		= 20;	// Maximum amount of players, including headless clients. Anybody who joins the server is considered a player, regardless of their role or team. \n'
                                + 'persistent		= 1;	// If set to 1, missions will continue to run after all players have disconnected; required if you want to use the -autoInit startup parameter \n'
                                + '\n'
                                + '// VOICE CHAT \n'
                                + 'disableVoN		= 0;	// If set to 1, voice chat will be disabled \n'
                                + 'vonCodecQuality	= 10;	// Supports range 1-30, the higher the better sound quality, the more bandwidth consumption: \n'
                                + '\n'
                                + '// VOTING \n'
                                + 'voteMissionPlayers	= 1;		// Minimum number of players required before displaying the mission selection screen, if you have not already selected a mission in this config \n'
                                + 'voteThreshold		= 0.33;		// Percentage (0.00 to 1.00) of players needed to vote something into effect, for example an admin or a new mission. Set to 9999 to disable voting. \n'
                                + 'allowedVoteCmds[] =				// Voting commands allowed to players \n'
                                + '{ \n'
                                + '	// {command, preinit, postinit, threshold} - specifying a threshold value will override "voteThreshold" for that command \n'
                                + '	{"admin", false, false},		// vote admin \n'
                                + '	{"kick", false, true, 0.51},	// vote kick \n'
                                + '	{"missions", false, false},		// mission change \n'
                                + '	{"mission", false, false},		// mission selection \n'
                                + '	{"restart", false, false},		// mission restart \n'
                                + '	{"reassign", false, false}		// mission restart with roles unassigned \n'
                                + '}; \n'
                                + '\n'
                                + '// WELCOME MESSAGE ("message of the day") \n'
                                + '// It can be several lines, separated by comma \n'
                                + '// Empty messages "" will not be displayed, but can be used to increase the delay before other messages \n'
                                + 'motd[] = \n'
                                + '{ \n'
                                + '	"Server created with GameServerManager", \n'
                                + '	"Website: https://github.com/venraij/GameServerManager" \n'
                                + '}; \n'
                                + 'motdInterval = 5;	// Number of seconds between each message \n'
                                + '\n'
                                + '// MISSIONS CYCLE \n'
                                + 'class Missions \n'
                                + '{ \n'
                                + '	class Mission1 \n'
                                + '	{ \n'
                                + '		template	= "MyMission.Altis";	// Filename of pbo in MPMissions folder \n'
                                + '		difficulty	= "Regular";			// "Recruit", "Regular", "Veteran", "Custom" \n'
                                + '	}; \n'
                                + '}; \n'
                                + '\n'
                                + '// LOGGING \n'
                                + 'timeStampFormat	= "short";				// Timestamp format used in the server RPT logs. Possible values are "none" (default), "short", "full" \n'
                                + 'logFile			= "server_console.log";	// Server console output filename \n'
                                + '\n'
                                + '// SECURITY \n'
                                + 'BattlEye				= 1;	// If set to 1, BattlEye Anti-Cheat will be enabled on the server (default: 1, recommended: 1) \n'
                                + 'verifySignatures		= 2;	// If set to 2, players with unknown or unsigned mods won\'t be allowed join (default: 0, recommended: 2) \n'
                                + 'kickDuplicate			= 1;	// If set to 1, players with an ID that is identical to another player will be kicked (recommended: 1) \n'
                                + 'allowedFilePatching		= 1;	// Prevents clients with filePatching enabled from joining the server \n'
                                + '								// (0 = block filePatching, 1 = allow headless clients, 2 = allow all) (default: 0, recommended: 1) \n'
                                + '\n'
                                + '// FILE EXTENSIONS \n'
                                + '\n'
                                + '// only allow files with those extensions to be loaded via loadFile command (since Arma 3 v1.19.124216) \n'
                                + 'allowedLoadFileExtensions[] =		{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml","inc","ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n'
                                + '\n'
                                + '// only allow files with those extensions to be loaded via preprocessFile / preprocessFileLineNumbers commands (since Arma 3 v1.19.124323) \n'
                                + 'allowedPreprocessFileExtensions[] =	{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml","inc","ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n'
                                + '\n'
                                + '// only allow files and URLs with those extensions to be loaded via htmlLoad command (since Arma 3 v1.27.126715) \n'
                                + 'allowedHTMLLoadExtensions[] =		{"htm","html","php","xml","txt"}; \n'
                                + '\n'
                                + '// EVENT SCRIPTS - see http://community.bistudio.com/wiki/ArmA:_Server_Side_Scripting \n'
                                + 'onUserConnected		= "";	// command to run when a player connects \n'
                                + 'onUserDisconnected	= "";	// command to run when a player disconnects \n'
                                + 'doubleIdDetected	= "";	// command to run if a player has the same ID as another player in the server \n'
                                + 'onUnsignedData		= "kick (_this select 0)";	// command to run if a player has unsigned files \n'
                                + 'onHackedData		= "kick (_this select 0)";	// command to run if a player has tampered files \n'
                                + '\n'
                                + '// HEADLESS CLIENT \n'
                                + 'headlessClients[]	= {"127.0.0.1"};	// list of IP addresses allowed to connect using headless clients; example: {"127.0.0.1", "192.168.1.100"}; \n'
                                + 'localClient[]		= {"127.0.0.1"};	// list of IP addresses to which are granted unlimited bandwidth;  example: {"127.0.0.1", "192.168.1.100"};'])
            
    except:
        print("Error")

    try:
        print("Creating desktop shortcut")
        desktop = winshell.desktop()
        path = os.path.join(desktop, "ArmA3Server.lnk")
        target = r"" + driveLetter + ":\Games\Arma3\A3Master\arma3server.exe"
        wDir = r"" + driveLetter + ":\Games\Arma3\A3Master"
        icon = r"" + driveLetter + ":\Games\Arma3\A3Master\arma3server.exe"
        args = ["-profiles=" + driveLetter + ":\Games\Arma3\A3Master","-port=2302","-config=CONFIG_server.cfg","-world=empty"]

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.Arguments = " ".join(args)
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()

    except:
        print("Error")

    ip = input('Enter computer IP (Not the public ip!): ')

    print("Opening up the ports via UPnP...")
    upnp = upnpy.UPnP()
    devices = upnp.discover()
    device = upnp.get_igd()
    device.get_services()
    service = device['WANIPConn1']
    service.get_actions()
    service.AddPortMapping.get_input_arguments()
    service.AddPortMapping(
        NewRemoteHost='',
        NewExternalPort=2302,
        NewProtocol='UDP',
        NewInternalPort=2302,
        NewInternalClient=ip,
        NewEnabled=1,
        NewPortMappingDescription='ArmA3 Server Port 1',
        NewLeaseDuration=0
    )
    service.AddPortMapping(
        NewRemoteHost='',
        NewExternalPort=2303,
        NewProtocol='UDP',
        NewInternalPort=2303,
        NewInternalClient=ip,
        NewEnabled=1,
        NewPortMappingDescription='ArmA3 Server Port 2',
        NewLeaseDuration=0
    )
    arma3()

def arma3Update ():
    driveLetter = input('Enter the drive letter where the server is installed: ')
    print("Updating ArmA3 Server...")
    os.system(driveLetter + ':/Games/ArmA3/A3Files/Arma3server_steamcmd.cmd')
    arma3()

def removeArma3 ():
    driveLetter = input('Enter the drive letter where the server is installed: ')
    print("Removing gameserver files...")
    shutil.rmtree(driveLetter + ':/Games/ArmA3')
    arma3()

def arma3Run ():
    print("Starting ArmA3 server...")
    os.system(driveLetter + ':/Games/Arma3/A3Master/arma3server.exe -profiles=' + driveLetter + ':/Games/Arma3/A3Master -port=2302 -config=CONFIG_server.cfg -world=empty')
    arma3()

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

    print('Installing to ' + fullsave);

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
    wget.download('http://ftp.hosteurope.de/mirror/archive.mariadb.org/mariadb-5.5.62/winx64-packages/mariadb-5.5.62-winx64.msi', 'C:/Users/' + user + '/Downloads')

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
    print('Installing to ' + 'C:/Users/' + user + '/Desktop/GameServerManager/Servers/Rust)')
    
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

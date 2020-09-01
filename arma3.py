import os
import shutil
import winshell

from pysteamcmdwrapper import SteamCMD, SteamCMDException
from win32com.client import Dispatch


# from screens import main_menu


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def arma3_main_menu():
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
        arma3_install()

    elif num == "2":
        arma3_remove()

    elif num == '3':
        arma3_update()

    elif num == '4':
        arma3_run()

    elif num == '5':
        main_menu()


def arma3_update():
    try:
        server_dir = "servers/armaserver"

        print("Checking SteamCMD install...")
        s = SteamCMD("steamcmd")
        try:
            s.install()
        except SteamCMDException as e:
            print(bcolors.OKGREEN + "SteamCMD is up-to-date." + bcolors.ENDC)
            print(e)

        print("Updating ArmA3 Server...")
        s.login()
        s.app_update(233780, os.path.join(os.getcwd(), server_dir), validate=True)

    except SteamCMDException as e:
        print(bcolors.FAIL + "Arma 3 server update failed." + bcolors.ENDC)
        print(e)

    arma3_main_menu()


def arma3_remove():
    server_dir = "servers/armaserver"
    print("Removing gameserver files...")
    print(os.path.join(os.getcwd(), server_dir))
    try:
        shutil.rmtree(os.path.join(os.getcwd(), server_dir))
    except OSError as e:
        print(bcolors.FAIL + "Failed to remove the Arma 3 server." + bcolors.ENDC)
        print(e)

    arma3_main_menu()


def arma3_run():
    server_dir = "servers/armaserver"
    print("Starting ArmA3 server...")
    try:
        os.system(os.path.join(os.getcwd(), server_dir) + "/arma3server.exe" + " -profiles=" + (
            os.path.join(os.getcwd(), server_dir)) + " -port=2302 -config=CONFIG_server.cfg -world=empty")
    except OSError as e:
        print(bcolors.FAIL + "There was an error while starting the Arma 3 server." + bcolors.ENDC)
        print(e)

    arma3_main_menu()


def arma3_install():
    port_arma = 2302
    port_query = 2303
    port_steam = 2304

    server_dir = "servers/armaserver"

    port_arma_input = input("To which port do you want players to connect? (DEFAULT: 2302): ")
    port_query_input = input("The port used by Steam query (DEFAULT: 2303):")
    port_steam_input = input("Regular steam port (DEFAULT: 2304) ")

    if port_arma_input:
        port_arma = port_arma_input

    if port_query_input:
        port_query = port_query_input

    if port_steam_input:
        port_steam = port_steam_input

    s = SteamCMD("steamcmd")
    try:
        s.install()
    except SteamCMDException as e:
        print(bcolors.OKGREEN + "SteamCMD is up-to-date." + bcolors.ENDC)
        print(e)

    s.login()
    s.app_update(233780, os.path.join(os.getcwd(), server_dir), validate=True)

    try:
        if not os.path.exists(os.path.join(os.getcwd(), server_dir) + '/CONFIG_server.cfg'):
            print("Creating default config file...")
            with open(os.path.exists(os.path.join(os.getcwd(), server_dir)), 'CONFIG_server.cfg', 'w') as OPATH:
                OPATH.writelines([
                    '// \n'
                    + '// server.cfg \n'
                    + '// \n'
                    + '// comments are written with "//" in front of them. \n'
                    + '\n'
                    + '// NOTE: More parameters and details are available at '
                      'http://community.bistudio.com/wiki/server.cfg \n '
                    + '\n'
                    + '// STEAM PORTS (not needed anymore, it\'s +1 +2 to gameport) \n'
                    + 'steamPort		= ' + str(
                        port_steam) + ';		// default  8766, needs to be unique if multiple servers are on the '
                                      'same box \n '
                    + 'steamQueryPort	= ' + str(
                        port_query) + ';	// default 27016, needs to be unique if multiple servers are on the same '
                                      'box \n '
                    + '\n'
                    + '// GENERAL SETTINGS \n'
                    + 'hostname = "Created with GameServerManager";	// Name of the server displayed in the public '
                      'server list \n '
                    + '//password		= "password";		// Password required to join the server (remove // at '
                      'start of line to enable) \n '
                    + 'passwordAdmin	= "AdminPassword";		// Password to login as admin. Open the chat and type: '
                      '#login password \n '
                    + 'maxPlayers		= 20;	// Maximum amount of players, including headless clients. Anybody who '
                      'joins the server is considered a player, regardless of their role or team. \n '
                    + 'persistent		= 1;	// If set to 1, missions will continue to run after all players have '
                      'disconnected; required if you want to use the -autoInit startup parameter \n '
                    + '\n'
                    + '// VOICE CHAT \n'
                    + 'disableVoN		= 0;	// If set to 1, voice chat will be disabled \n'
                    + 'vonCodecQuality	= 10;	// Supports range 1-30, the higher the better sound quality, the more '
                      'bandwidth consumption: \n '
                    + '\n'
                    + '// VOTING \n'
                    + 'voteMissionPlayers	= 1;		// Minimum number of players required before displaying the '
                      'mission selection screen, if you have not already selected a mission in this config \n '
                    + 'voteThreshold		= 0.33;		// Percentage (0.00 to 1.00) of players needed to vote '
                      'something into effect, for example an admin or a new mission. Set to 9999 to disable voting. \n '
                    + 'allowedVoteCmds[] =				// Voting commands allowed to players \n'
                    + '{ \n'
                    + '// {command, preinit, postinit, threshold} - specifying a threshold value will override '
                      '"voteThreshold" for that command \n '
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
                    + '// Empty messages "" will not be displayed, but can be used to increase the delay before other '
                      'messages \n '
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
                    + 'timeStampFormat	= "short";				// Timestamp format used in the server RPT logs. '
                      'Possible values are "none" (default), "short", "full" \n '
                    + 'logFile			= "server_console.log";	// Server console output filename \n'
                    + '\n'
                    + '// SECURITY \n'
                    + 'BattlEye				= 1;	// If set to 1, BattlEye Anti-Cheat will be enabled on the server '
                      '(default: 1, recommended: 1) \n '
                    + 'verifySignatures		= 2;	// If set to 2, players with unknown or unsigned mods won\'t be '
                      'allowed join (default: 0, recommended: 2) \n '
                    + 'kickDuplicate			= 1;	// If set to 1, players with an ID that is identical to '
                      'another player will be kicked (recommended: 1) \n '
                    + 'allowedFilePatching		= 1;	// Prevents clients with filePatching enabled from joining the '
                      'server \n '
                    + '// (0 = block filePatching, 1 = allow headless clients, 2 = allow all) (default: 0, '
                      'recommended: 1) \n '
                    + '\n'
                    + '// FILE EXTENSIONS \n'
                    + '\n'
                    + '// only allow files with those extensions to be loaded via loadFile command (since Arma 3 '
                      'v1.19.124216) \n '
                    + 'allowedLoadFileExtensions[] =		{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml","inc",'
                      '"ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n '
                    + '\n'
                    + '// only allow files with those extensions to be loaded via preprocessFile / '
                      'preprocessFileLineNumbers commands (since Arma 3 v1.19.124323) \n '
                    + 'allowedPreprocessFileExtensions[] =	{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml","inc",'
                      '"ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n '
                    + '\n'
                    + '// only allow files and URLs with those extensions to be loaded via htmlLoad command (since '
                      'Arma 3 v1.27.126715) \n '
                    + 'allowedHTMLLoadExtensions[] =		{"htm","html","php","xml","txt"}; \n'
                    + '\n'
                    + '// EVENT SCRIPTS - see http://community.bistudio.com/wiki/ArmA:_Server_Side_Scripting \n'
                    + 'onUserConnected		= "";	// command to run when a player connects \n'
                    + 'onUserDisconnected	= "";	// command to run when a player disconnects \n'
                    + 'doubleIdDetected	= "";	// command to run if a player has the same ID as another player in the '
                      'server \n '
                    + 'onUnsignedData		= "kick (_this select 0)";	// command to run if a player has unsigned files \n'
                    + 'onHackedData		= "kick (_this select 0)";	// command to run if a player has tampered files \n'
                    + '\n'
                    + '// HEADLESS CLIENT \n'
                    + 'headlessClients[]	= {"127.0.0.1"};	// list of IP addresses allowed to connect using '
                      'headless clients; example: {"127.0.0.1", "192.168.1.100"}; \n '
                    + 'localClient[]		= {"127.0.0.1"};	// list of IP addresses to which are granted unlimited '
                      'bandwidth;  example: {"127.0.0.1", "192.168.1.100"};'])

        elif os.path.exists(os.path.join(os.getcwd(), server_dir) + '/CONFIG_server.cfg'):
            if (input(bcolors.FAIL + 'The file ' + os.path.join(os.getcwd(),
                                                                server_dir) + '/CONFIG_server.cfg already exists. '
                                                                              'Would you like to override it? (y/n): '
                                                                              '' + bcolors.ENDC).lower()) == 'y':
                print("Creating new default config file...")
                with open(os.path.exists(os.path.join(os.getcwd(), server_dir)), 'CONFIG_server.cfg', 'w') as OPATH:
                    OPATH.writelines([
                        '// \n'
                        + '// server.cfg \n'
                        + '// \n'
                        + '// comments are written with "//" in front of them. \n'
                        + '\n'
                        + '// NOTE: More parameters and details are available at '
                          'http://community.bistudio.com/wiki/server.cfg \n '
                        + '\n'
                        + '// STEAM PORTS (not needed anymore, it\'s +1 +2 to gameport) \n'
                        + 'steamPort		= ' + str(
                            port_steam) + ';	// default  8766, needs to be unique if multiple servers are on the '
                                          'same box \n '
                        + 'steamQueryPort	= ' + str(
                            port_query) + ';	// default 27016, needs to be unique if multiple servers are on the '
                                          'same box \n '
                        + '\n'
                        + '// GENERAL SETTINGS \n'
                        + 'hostname = "Created with GameServerManager";	// Name of the server displayed in the public '
                          'server list \n '
                        + '//password		= "password";		// Password required to join the server (remove // at '
                          'start of line to enable) \n '
                        + 'passwordAdmin	= "AdminPassword";		// Password to login as admin. Open the chat and '
                          'type: #login password \n '
                        + 'maxPlayers		= 20;	// Maximum amount of players, including headless clients. Anybody '
                          'who joins the server is considered a player, regardless of their role or team. \n '
                        + 'persistent		= 1;	// If set to 1, missions will continue to run after all players '
                          'have disconnected; required if you want to use the -autoInit startup parameter \n '
                        + '\n'
                        + '// VOICE CHAT \n'
                        + 'disableVoN		= 0;	// If set to 1, voice chat will be disabled \n'
                        + 'vonCodecQuality	= 10;	// Supports range 1-30, the higher the better sound quality, '
                          'the more bandwidth consumption: \n '
                        + '\n'
                        + '// VOTING \n'
                        + 'voteMissionPlayers	= 1;		// Minimum number of players required before displaying '
                          'the mission selection screen, if you have not already selected a mission in this config \n '
                        + 'voteThreshold		= 0.33;		// Percentage (0.00 to 1.00) of players needed to vote '
                          'something into effect, for example an admin or a new mission. Set to 9999 to disable '
                          'voting. \n '
                        + 'allowedVoteCmds[] =				// Voting commands allowed to players \n'
                        + '{ \n'
                        + '// {command, preinit, postinit, threshold} - specifying a threshold value will override '
                          '"voteThreshold" for that command \n '
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
                        + '// Empty messages "" will not be displayed, but can be used to increase the delay before '
                          'other messages \n '
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
                        + 'timeStampFormat	= "short";				// Timestamp format used in the server RPT logs. '
                          'Possible values are "none" (default), "short", "full" \n '
                        + 'logFile			= "server_console.log";	// Server console output filename \n'
                        + '\n'
                        + '// SECURITY \n'
                        + 'BattlEye				= 1;	// If set to 1, BattlEye Anti-Cheat will be enabled on the '
                          'server (default: 1, recommended: 1) \n '
                        + 'verifySignatures		= 2;	// If set to 2, players with unknown or unsigned mods won\'t '
                          'be allowed join (default: 0, recommended: 2) \n '
                        + 'kickDuplicate			= 1;	// If set to 1, players with an ID that is identical to '
                          'another player will be kicked (recommended: 1) \n '
                        + 'allowedFilePatching		= 1;	// Prevents clients with filePatching enabled from joining '
                          'the server \n '
                        + '// (0 = block filePatching, 1 = allow headless clients, 2 = allow all) (default: 0, '
                          'recommended: 1) \n '
                        + '\n'
                        + '// FILE EXTENSIONS \n'
                        + '\n'
                        + '// only allow files with those extensions to be loaded via loadFile command (since Arma 3 '
                          'v1.19.124216) \n '
                        + 'allowedLoadFileExtensions[] =		{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml",'
                          '"inc","ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n '
                        + '\n'
                        + '// only allow files with those extensions to be loaded via preprocessFile / '
                          'preprocessFileLineNumbers commands (since Arma 3 v1.19.124323) \n '
                        + 'allowedPreprocessFileExtensions[] =	{"hpp","sqs","sqf","fsm","cpp","paa","txt","xml",'
                          '"inc","ext","sqm","ods","fxy","lip","csv","kb","bik","bikb","html","htm","biedi"}; \n '
                        + '\n'
                        + '// only allow files and URLs with those extensions to be loaded via htmlLoad command ('
                          'since Arma 3 v1.27.126715) \n '
                        + 'allowedHTMLLoadExtensions[] =		{"htm","html","php","xml","txt"}; \n'
                        + '\n'
                        + '// EVENT SCRIPTS - see http://community.bistudio.com/wiki/ArmA:_Server_Side_Scripting \n'
                        + 'onUserConnected		= "";	// command to run when a player connects \n'
                        + 'onUserDisconnected	= "";	// command to run when a player disconnects \n'
                        + 'doubleIdDetected	= "";	// command to run if a player has the same ID as another player in '
                          'the server \n '
                        + 'onUnsignedData		= "kick (_this select 0)";	// command to run if a player has unsigned '
                          'files \n '
                        + 'onHackedData		= "kick (_this select 0)";	// command to run if a player has tampered files \n'
                        + '\n'
                        + '// HEADLESS CLIENT \n'
                        + 'headlessClients[]	= {"127.0.0.1"};	// list of IP addresses allowed to connect using '
                          'headless clients; example: {"127.0.0.1", "192.168.1.100"}; \n '
                        + 'localClient[]		= {"127.0.0.1"};	// list of IP addresses to which are granted '
                          'unlimited bandwidth;  example: {"127.0.0.1", "192.168.1.100"};'])

    except OSError as e:
        print(bcolors.FAIL + "Error while creating config file." + bcolors.ENDC)
        print(e)

    try:
        print("Creating desktop shortcut...")
        desktop = winshell.desktop()
        path = os.path.join(desktop, "ArmA3Server.lnk")
        target = r"" + os.path.join(os.getcwd(), server_dir) + "/arma3server.exe"
        w_dir = r"" + os.path.join(os.getcwd(), server_dir)
        icon = r"" + os.path.join(os.getcwd(), server_dir) + "/arma3server.exe"
        args = ["-profiles=" + os.path.join(os.getcwd(), server_dir), "-port=" + port_arma + "",
                "-config=CONFIG_server.cfg", "-world=empty"]

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.Arguments = " ".join(args)
        shortcut.WorkingDirectory = w_dir
        shortcut.IconLocation = icon
        shortcut.save()

    except Exception as e:
        print(e)

    arma3_main_menu()

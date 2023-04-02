package windows

import chocolatey "github.com/venraij/SteamCMDWrapper/pkg/Chocolatey"

func Install() {
	chocolatey.Install()
	chocolatey.InstallPackage("SteamCMD", "-y")
}

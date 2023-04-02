package chocolatey

import (
	"log"
	"os"
	"os/exec"
)

func Install() {
	cmd := exec.Command("powershell", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func InstallPackage(packageName string, args string) {
	cmd := exec.Command("choco", "install", packageName, args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func UninstallPackage(packageName string, args string) {
	cmd := exec.Command("choco", "uninstall", packageName, args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func UpdatePackage(packageName string, args string) {
	cmd := exec.Command("choco", "upgrade", packageName, args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func UpdateAllPackages(args string) {
	cmd := exec.Command("choco", "upgrade", "all", args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func ListPackages(args string) {
	cmd := exec.Command("choco", "list", args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func ListInstalledPackages(args string) {
	cmd := exec.Command("choco", "list", "--localonly", args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

func ListOutdatedPackages(args string) {
	cmd := exec.Command("choco", "list", "--outdated", args)
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
		return
	}
}

package SteamCMD

import (
	"log"
	"os"
)

func Install() {
	//Create a folder/directory at a full qualified path'
	dirname, err := os.UserHomeDir()
	if err != nil {
		log.Fatal(err)
		err = nil
	}

	path := dirname + "/Go-SteamCMD"
	err = os.Mkdir(path, 0755)

	if err != nil {
		log.Fatal(err)
	} else {
		log.Println("Directory created successfully at: " + path)
	}
}

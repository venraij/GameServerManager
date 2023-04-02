package SteamCMD

import (
	"log"
	"os"
)

func install() {
	//Create a folder/directory at a full qualified path'
	dirname, err := os.UserHomeDir()
	if err != nil {
		log.Fatal(err)
		err = nil
	}

	path := dirname + "/GameServerManager"
	err = os.Mkdir(path, 0755)

	if err != nil {
		log.Fatal(err)
	}
}

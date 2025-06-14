# file Obsidian su Github

come inserire su Github una cartella creata con Obsidian

## su Github

1. creo un repo su Github
2. assegno un token al repository

## su Obsidian

1. uso il plugin Git di Obsidian
2. lancio "clone"
3. indico il nome del repo con questa sequenta:   https://token@github.com/paolovolterra/NomeRepo.git
4. creo in Obsidian la cartella dedicata al repo 
5. da bash autorizzo la cartella  con 
	```
	git config --global --add safe.directory D:/PKM/Github
	```
6. scrivo o inserisco file e cartelle nella cartella
7. lancio Git:commit-and-sync

# file Obsidian su Github

_come inserire su Github una cartella creata con Obsidian_

Normalmente utilizzo Obsidian per prendere appunti

E se questi appunti li trasformassi in pagine sul [mio Github](https://github.com/paolovolterra)?


## su Github

1. creo un repo su [Github](https://github.com/)
2. [assegno un token](https://github.com/settings/tokens) al repository


## su Obsidian

1. uso il [plugin Git](https://github.com/Vinzent03/obsidian-git) di Obsidian
2. lancio "clone"
3. indico il nome del repo con questa sequenta:   https://token@github.com/paolovolterra/NomeRepo.git
4. creo in Obsidian la cartella dedicata al repo 
5. da bash autorizzo la cartella  con 
	```
	git config --global --add safe.directory D:/PKM/Github
	```
6. scrivo o inserisco file e cartelle nella cartella
7. lancio Git:commit-and-sync


## note

- il token non cambia se il repo passa da privato a pubblico o viceversa
- i link delle immagini devono avere formato standard markdown
```
[immagine](media/nomemmagine.png)
```
- posso avere più cartelle dedicate singolarmente a repo Github
- Github non interpreta le sezioni YAML
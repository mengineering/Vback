#!/bin/sh

#Autore: Andrea Mengozzi
#Data primo rilascio: 25/12/2023
#rev00

#Scopo
#Questo script esegue la copia di specifiche cartelle presenti sul mac (o su icloud) il cui nome è contenuto nel file xxxx nel percorso di destinazione
#percorso di origine e destinazione

#initial working directory
INIT_WRK_DIRECTORY=$(pwd)

#input file percorsi cartelle sottoposte a backup

read -r destination<./destinations.txt

elenco=$INIT_WRK_DIRECTORY/source_folders.txt

#NOTE: nel file source_folders lasciare una riga vuota alla fine nella versione macos, altrimenti non copia tutte le cartelle

#creo il log file
cd $destination
#output di tutte le operazioni eseguite
touch log.txt
#output degli errori
touch Errors_log.txt

while read -r line
	do
	fld_one=$line
	#copia della cartella - UBUNTU
	#cp -r -u -v $fld_one $destination 2>> Errors_log.txt >> log.txt
    
    #copia della cartella - MacOS
    cp -r -v $fld_one $destination 2>> Errors_log.txt >> log.txt
    
	#note 2>> indica append dello stderr > invece reindirizza stdout sovrascrivendo il file log

done <"$elenco"

#solo Ubuntus
#notify-send "Copia eseguita, ricordati di consultare il file degli errori"


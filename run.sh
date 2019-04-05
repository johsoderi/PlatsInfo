#!/bin/bash

clear
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo Skapar virtuell miljö...
python3 -m venv $SCRIPTPATH/tmp/VirtEnv
echo Klart.
echo Aktiverar den virtuella miljön...
source $SCRIPTPATH/tmp/VirtEnv/bin/activate
echo Klart.
echo Kör Python-script...
python3 $SCRIPTPATH/project.py
echo Raderar tillfälliga filer...
rm -R $SCRIPTPATH/tmp
echo Klart.

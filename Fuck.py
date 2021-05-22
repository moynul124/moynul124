#!/data/data/com.termux/files/usr/bin/bash

## Author : Asif Javed

## Email  : lovehacker966@gmail.com

## Github : @lovehackerAsif

## Reddit : lovehacker

 

#colors

R='\033[1;31m'

B='\033[1;34m'

C='\033[0;36m'

G='\033[1;32m'

W='\033[1;37m'

Y='\033[1;33m'

 

DIR="$(pwd)"

 

echo

echo -e $R"   ###########┈┈┈┈╱▔▔▔▔╲┈┈┈┈########### "

echo -e $R"   ###########┈┈┈▕▕╲┊┊╱▏▏┈┈┈########### "

echo -e $R"   ###########┈┈┈▕▕▂╱╲▂▏▏┈┈┈########### "

echo -e $R"   ###########┈┈┈┈╲┊┊┊┊╱┈┈┈┈########### "

echo -e $R"   ###########┈┈┈┈▕╲▂▂╱▏┈┈┈┈########### "

echo -e $R"   ###########╱▔▔▔▔┊┊┊┊▔▔▔▔╲########### "

echo

 

echo -e $G"   [*] Installing termux-style..."

echo

echo -e $Y"   [*] Setting Up The Program..."

echo

 

if [ ! -d $HOME/.termux ]; then

mkdir $HOME/.termux

fi

 

mv $DIR/data.tar.gz $PREFIX/share

cd $PREFIX/share

echo -e $Y"   [*] Extracting Files..."$C

echo

tar -xhf data.tar.gz

chmod +x termux-style/theme

ln -s $PREFIX/share/termux-style/theme $PREFIX/bin/termux-style

rm $PREFIX/share/data.tar.gz

termux-reload-settings

echo -e $G"   [*] Setup Completed."

echo

echo -e $Y"   [*] Now You Can Run This Program By Just typing 'termux-style'."

echo -e $Y"   [*] Developer lovehacker."

echo

echo -e $G"   [*] Developed By$R lovehacker."

echo

 


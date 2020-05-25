#!/bin/bash

echo "0%"
cd ~/
echo "25%"
wget https://raw.githubusercontent.com/PTEC-Repository/Main-repo/master/ptecSystem.zip
echo "33.3%"
export PATH='$HOME/PTEC/base/bin/:$PATH'
echo "50%"
rm ./PTEC/ -r
echo "75%"
unzip ptecSystem.zip
echo "87.5%"
echo "export $PATH='$HOME/PTEC/base/bin/:$PATH'" >> ~/bash.bashrc
echo "export $PATH='$HOME/PTEC/base/bin/:$PATH'" >> ~/profile
echo "100%"

echo "PTPKG SYSTEM INSTALLATION  COMPLETE!"
echo "Type: 'ptpkg help' For An Introduction To PTPKG!"

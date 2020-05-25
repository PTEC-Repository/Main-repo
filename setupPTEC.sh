#!/bin/bash

cd ~/

rm ./ptecSystem*

rm ./PTEC -r

wget https://raw.githubusercontent.com/PTEC-Repository/Main-repo/master/ptecSystem.zip

unzip ptecSystem.zip

export PATH='$HOME/PTEC/base/bin/:$PATH'

echo "export $PATH='$HOME/PTEC/base/bin/:$PATH'" >> ~/bash.bashrc

echo "export $PATH='$HOME/PTEC/base/bin/:$PATH'" >> ~/profile

echo "PTPKG Installed, the command ptpkg will now work on any terminal opened from now."

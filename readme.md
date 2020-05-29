### PTEC Main Repository&nbsp;
PTEC OFFICIAL MAIN repository, official creation date: 5/21/20
---
PTRepocode: PTOFFICIAL-MAIN-5/21/20


To install (Copy the lot and paste it in to a terminal):

cd ~/ ; rm ./setupPTEC.sh ; wget https://raw.githubusercontent.com/PTEC-Repository/Main-repo/master/setupPTEC.sh ; chmod 777 ./setupPTEC.sh ; ./setupPTEC.sh ; export PATH="$HOME/PTEC/base/bin:$PATH"

To update insaller script, re-run the above. This is reccomended if expiriencing issues, ond also once a month.


!Warning!
Updating currently causes all installed packages, and assets to be removed.

To update:
~/setupPTEC.sh

Ubuntu users:
You may experience import errors with distutuls, this should fix that:
sudo apt install python3-distutils

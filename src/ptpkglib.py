ver = 'DEVELOPMENT'

import ptlib
import os
import sys

home = os.environ['HOME']
mainRepo = 'https://raw.githubusercontent.com/PTEC-Repository/Main-repo/master/'
repoPath = home + '/PTEC/base/config/repolist'

def checkInstall():
    if os.path.exists(home + '/PTEC/base/'):
        return True
    else:
        return False

if checkInstall():
    ...
else:
    print('Ptpkglib here, PTEC Base is most likley not installed, this will cause SERIOUS complications. Continuing')

def checkRepolist():
    if len(ptlib.catFile(repoPath).splitlines()) < 1:
        ptlib.log('Mirror List Is Empty, You Could Run \'ptpkg repolist-gen\'')

def getRepos():
    try:
        repos = ptlib.catFile(repoPath).splitlines()
        return repos
    except FileNotFoundError:
        ptlib.log('Repository list not existent, this is most likley due to it not being generated. You could generate it using ptpkg. type \'ptpkg help\' for info on generating the repository list Exiting')
        exit()

def clearRepo():
    ptlib.overwriteFile(repoPath, '')

def addRepo(repo):
    ptlib.echoToFile(repoPath, repo + '\n')

def Install(pkg):

    os.system('rm ~/PTEC/base/tmp/* -r')
    print('PTEC Tmp Directory Cleared')
    repos = getRepos()

def Remove(pkg):
    print('ptpkglib Remove Function Not Implimented (Yet)')

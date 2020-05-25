ver = '1.0'

import ptlib
import os
import sys

home = os.environ['HOME']
mainRepo = 'https://raw.githubusercontent.com/PTEC-Repository/Main-repo/master/'
repoPath = home + '/PTEC/base/config/repolist'
ptecPath = home + '/PTEC/'

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

def clearTmp():
    ptlib.command('rm ' + ptecPath + 'base/tmp/* -r')

def clearCache():
    ptlib.command('rm ' + ptecPath + 'base/pkg/* -r')
    print('^ Don\'t Worry About Previous Errors! (If there were any!)\n')

def Download(URL, name):
    ptlib.wget(URL, ptecPath + '/base/pkg/' + name)

def LInstall(pkg):
    if ptlib.exists(pkg):
        clearTmp()
        ptlib.unZip(pkg, ptecPath + 'base/tmp/')
        tmp = ptecPath + 'base/tmp/'
        ver = ptlib.catFile(tmp + 'data/ver')
        desc = ptlib.catFile(tmp + 'data/desc')
        name = ptlib.catFile(tmp + 'data/name')
        category = ptlib.catFile(tmp + 'data/category')
        ptlib.log('Installing: ' + name + '\n    > Version: ' + ver + '\n    > Description: ' + desc + '\n    > Category: ' + category)
        name = name.rstrip()
        print('0% (Copying Assets)')
        ptlib.command('cp \'' + tmp + name + '\' -r \'' + ptecPath + '\'')
        print('50% (Copying Binaries)')
        ptlib.command('cp \'' + tmp + 'exec/' + name +'\' ' + ptecPath + 'base/bin/')
        print('100% (Done)')
        ptlib.log('Package: ' + name + ' Installed!')
        exit()
    else:
        ptlib.log('ERROR: Package: \'' + pkg + '\' Not Found!')
def Install(pkg):
    pkglist = str()
    verlist = str()
    namelist = str()
    skip = False
    
    clearTmp()
    
    repos = getRepos()

    for repo in repos:
        pkglist = str()
        verlist = str()
        namelist = str()
        clearTmp()
        if not skip:
            ptlib.log('checking repo: ' + repo + 'for package: ' + pkg)
            ptlib.wget(repo + 'PKGList', ptecPath + 'base/tmp/PKGList')
            PKGList = ptlib.catFile(ptecPath + 'base/tmp/PKGList')
            PKGList = PKGList.splitlines()
            for line in PKGList:
                pkglist += line.split(' ')[0] + ' '
                verlist += line.split(' ')[1] + ' '
                namelist += line.split(' ')[2] + ' '
            pkglist = pkglist.rstrip().split(' ')
            verlist = verlist.rstrip().split(' ')
            namelist = namelist.rstrip().split(' ')
            if not skip:
                if pkg in pkglist:
                    if not skip:
                        index = pkglist.index(pkg)
                        ptlib.log('Found: ' + pkg + ' Version: ' + verlist[index] + ' In Repository: ' + repo)
                        name = namelist[index]
                        ptlib.log('Downloading: ' + name)
                        Download(repo + name, name)
                        ptlib.log('Installing: ' + pkg + '... (' + ptecPath + 'base/pkg' + name + ')')
                        LInstall(ptecPath + 'base/pkg/' + name)
                        skip = True
                        ptlib.log('Skipping All Other Searches...')
                else:
                    ptlib.log('Cant Find: ' + pkg + ' In Repository: ' + repo)

def listAll():
    repos = getRepos()
    clearTmp()
    out = str()
    for repo in repos:
        clearTmp()
        ptlib.wget(repo + 'PKGList', ptecPath + 'base/tmp/pkglist')
        pkglist = ptlib.catFile(ptecPath + 'base/tmp/pkglist').splitlines()
        out += 'Repo: ' + repo + '\n'
        for pkg in pkglist:
            out += '    ' + pkg + '\n'
    return out

def lCache():
    out = ptlib.shell('ls ' + ptecPath + 'base/pkg/')
    ptlib.log('Package Listing Of PTEC Package Cache:\n' + out)

def Remove(pkg):
    print('ptpkglib Remove Function Not Implimented (Yet)')

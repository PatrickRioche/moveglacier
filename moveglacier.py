# Auteur : Rioche Patrick   le 29/08/2020
#
# Mode d'emploi :
#
#   moveglacier.py chemin +options >trace.log
#
#   Ce programme met en forme une structure de fichier pour stocker dans 
#   Glacier amazon S3
#
#   Entree :
#       chemin
#       options     liste des options
#
#   Sortie :
#       NA
#
#   Version :
#       V1.0    29/08/2020
#
__version__ = 'V1.0'
DEBUG = 1

import os, sys

if len(sys.argv) == 0:
    print ( "Mode de d'emploi : " + __version__ )
    print ( "                                 " )
    print ( "    moveglacier.py chemin" )
    sys.exit(1)

#
#   Recuperation des arguments de la ligne de commande
#
#sChe = sys.argv[1]
#sChe = '/Users/patrickrioche/Desktop/Aarchiver'
sChe = 'C:/Users/Rioche-P/OneDrive - Harmonie Mutuelle/Bureau/Aarchiver'
#sTable = sFic.split("/")[-1].split(".")[0]

#
#   Initialisation global
#
import shutil, os
from datetime import datetime

dGlacier = {}

#
#   Definition des fonctions
#

#
#   Definition des fonctions Exemples
#
def get_creation_date(file):
    stat = os.stat(file)
    try:
        return stat.st_birthtime
    except AttributeError:
        # Nous sommes probablement sous Linux. Pas de moyen pour obtenir la date de création, que la dernière date de modification.
        return stat.st_mtime

#
#   Definition de mes fonctions
#
def ReplaceCS( sTheString ):
    sS1 = sTheString.lstrip().rstrip()
    sS2 = sS1.replace('\\','/')
    return( sS2 )

def GetAAAA( sTheCreatDateFile ):
    sS1 = sTheCreatDateFile.split("-"[0])
    return sS1[0]

def GetMM( sTheCreatDateFile ):
    sS1 = sTheCreatDateFile.split("-"[0])
    return sS1[1]

def GetDD( sTheCreatDateFile ):
    sS1 = sTheCreatDateFile.split("-"[0])
    sS2 = sS1[2].split(" "[0])
    return sS2[0]

def GetCreatDateFile(sFile):
    sCreatDateFile = datetime.fromtimestamp(get_creation_date(sFile) )
    return str(sCreatDateFile)

def GetExtendFile( sFile ):
    sS1 = sFile.split("."[0])
    return sS1[1]

def MakS3Dir( sTheDirSrc, sTheDirDst ):
    sSupDir = sTheDirDst.replace( sTheDirSrc, "")
    if (DEBUG) : print( "sSupDir=>" + sSupDir + "<=" )    
    sDirs = sSupDir.split("/"[0])
    sS1 = sDirs[1:]
    sMakDir = sS1[:-1]
    sTheRootDir = sTheDirSrc
    for sItemDir in sMakDir:
        sTheRootDir = sTheRootDir + "/" + sItemDir
        print( "creer=>" + sTheRootDir + "<" )
        if not os.path.exists(sTheRootDir):
            os.makedirs(sTheRootDir)
    return

def MoveGlacier( s3Root, s3File ):
    if s3File[0] == ".": return
    if (DEBUG) : print( s3File )
    sCreatDateFile = GetCreatDateFile(s3Root + "/" + s3File)
    sDirSrc = ReplaceCS(s3Root) + "/" 
    sDirDst = ReplaceCS(sChe) + "/s3g/" + GetExtendFile(s3File) + "/" + GetAAAA(sCreatDateFile) + "/" + GetMM(sCreatDateFile) + "/" + GetDD(sCreatDateFile) + "/" 
    if (DEBUG) : print( "MOVE " + sDirSrc + s3File + "->" + sDirDst + s3File )
    MakS3Dir( sChe, sDirDst )
    shutil.move( sDirSrc + s3File, sDirDst + s3File )
 
#   Programme Principal
#
sChe = ReplaceCS( sChe )

if (DEBUG): print ( "sChe=>" + sChe + "<=" )
print ( "==> " + sChe )

for sRoot, sDir, sFiles in os.walk(sChe):
    if (DEBUG) : print ( "sRoot=>" + sRoot + "<=")
    for sFile in sFiles:
        MoveGlacier( sRoot, sFile )


print ( "<== " + sChe )
#   
#   Fin de programme
#

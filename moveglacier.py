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
import os
from datetime import datetime

dGlacier = {}

#
#   Definition des fonctions
#
def get_creation_date(file):
    stat = os.stat(file)
    try:
        return stat.st_birthtime
    except AttributeError:
        # Nous sommes probablement sous Linux. Pas de moyen pour obtenir la date de création, que la dernière date de modification.
        return stat.st_mtime

def aff_creation_date(file):
    creation_date = datetime.fromtimestamp(get_creation_date(file))
    print("Date de création: %s" % creation_date)

def aff_rep_s3(file):
    sDateCreat = datetime.fromtimestamp(get_creation_date(file))
    print( sDateCreat )

def moveglacier( s3Root, s3File ):
    if s3File[0] == ".": return
    print( s3File )
    aff_rep_s3( s3Root + "/" + s3File)

#
#   Programme Principal
#
if (DEBUG): print ( "sChe=>" + sChe + "<=" )
print ( "==> " + sChe )

for sRoot, sDir, sFiles in os.walk(sChe):
    if (DEBUG) : print ( "sRoot=>" + sRoot + "<=")
    for sFile in sFiles:
        moveglacier( sRoot, sFile )


print ( "<== " + sChe )
#   
#   Fin de programme
#

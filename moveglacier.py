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

if len(sys.argv) == 1:
    print ( "Mode de d'emploi : " + __version__ )
    print ( "                                 " )
    print ( "    moveglacier.py chemin" )
    sys.exit(1)

#
#   Recuperation des arguments de la ligne de commande
#
sChe = sys.argv[1]
sChe = '/Users/patrickrioche/Desktop/Aarchiver'
#sTable = sFic.split("/")[-1].split(".")[0]

#
#   Initialisation global
#
dGlacier = {}

#
#   Definition des fonctions
#

if (DEBUG): print ( "sChe = " + sChe )

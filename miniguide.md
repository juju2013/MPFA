# Mini Guide

## Installation

Pour un Ubuntu 18.04 de base :

    sudo apt update
    sudo apt install wget unzip python3-pip zbar-tools
    pip3 install pillow pyzbar qrcode
    wget https://github.com/juju2013/MPFA/archive/refs/heads/master.zip
    unzip master.zip
    cd MPFA-master/
  
## Générer votre cochon

 *  Scanner votre attestation de vaccination et découper votre certificat Covid (le premier Qrcode du haut dans l'exemple ci-dessous), 
 nommer le `monpass.png` et déposer le dans MPFA-master.
 
 <img src="https://www.ameli.fr/sites/default/files/thumbnails/image/attestation-vaccination-format-europeen-exemple.jpg" height=600 />

Lancer simplement 

    ./passfun.py monpass.png cochon.jpg funpass.png --pos 50 --trans 80 --scale 90

Et voilà !!

 <img src="funpass.png" height=400 />

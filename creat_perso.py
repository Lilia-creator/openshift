
def create_perso(Pseudo="",PV="",Force="",Armure=""):
    Pseudo = input('Veuillez taper votre pseudo : ').strip()
    PV  = int(input('Veuillez taper votre PV : '))
    Force  = int(input('Veuillez taper Votre force : '))
    Armure  = int(input('Veuillez taper votre Armure : '))
    return [Pseudo,PV,Force,Armure]


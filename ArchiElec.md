# MIoT-Project

MPPT : Conversionn de tension, pour charger la batterie, il faut adapter le courant et la
tension nécessaire pour charger la batterie la plus rapidement sans l'abimé

BMS : estimer l'état de charge SOC
arrêter charge si batt pleine


Regarder sur KiKad, mais en gros pour le MPPT :
Le signal va du panel au sensor et la batterie va au sensor.
Puis les informations et le courant passe dans le micro processor.
Le microprocessor envoie les infos au StepDown qui redirige le courant à la batterie
Le Stepdown reçois le courant du panneau solaire et l'envoie à la batterie
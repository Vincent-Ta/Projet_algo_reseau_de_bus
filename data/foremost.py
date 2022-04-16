from horaires import *
import operator
from math import inf


def foremost(dep, dest, heure_de_depart):
    """Cette fois ci on veut le chemin le plus court en partant à une certaine heure"""
    noeud_courant=dep
    heure_actuelle=changer_string_en_min(heure_de_depart)
    liste_tot=dep.liste_arrets([])
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom], ["aucune ligne"]]}
    arrets_inconnus={k.nom:[inf,'',"aucune ligne"] for k in liste_tot if k!=noeud_courant}

    for id_voisin in range(len(dep.arrets_voisins)):
        if dep.arrets_voisins[id_voisin].nom != "terminus":
            #La distance entre de point de départ et ses voisins est égale à la distance en min entre les deux + le temps d'attente du bus
            arrets_inconnus[dep.arrets_voisins[id_voisin].nom]=[distance_en_min_entre_deux_arrets(dep, dep.arrets_voisins[id_voisin])+temps_d_attente(heure_actuelle, dep,dep.arrets_voisins[id_voisin]), dep.nom, dep.ligne[id_voisin]]

    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_foremost(arrets_inconnus, liste_tot)
        mise_a_jour_foremost(noeud_courant, arrets_connus, arrets_inconnus, liste_tot, heure_actuelle)
        #l'heure actuelle est l'heure de départ + le temps d'arriver à l'arret suivant avec le temps d'attente
        heure_actuelle=heure_actuelle+arrets_connus[noeud_courant.nom][0]

    return arrets_connus[dest.nom]


def mise_a_jour_foremost(arret, arrets_connus, arrets_inconnus, liste_tot, heure_actuelle):

        for v in arret.arrets_voisins:
            if v.nom in arrets_inconnus :
                #Ici aussi, on prend en compte le temps d'attente + la distance entre deux arrets 
                d= arrets_inconnus[arret.nom][0] +  distance_en_min_entre_deux_arrets(arret, v) + temps_d_attente(heure_actuelle, arret, v)
                
                if d<arrets_inconnus[v.nom][0] :
                    indice_arret_v=arret.arrets_voisins.index(v)
                    arrets_inconnus[v.nom]=[d,arret.nom, arret.ligne[indice_arret_v]]

        old_arret_nom=arrets_inconnus[arret.nom][1]

        for i in liste_tot :
            if old_arret_nom==i.nom :
                old_arret=i

        indice_arret_v=old_arret.arrets_voisins.index(arret)
        arrets_connus[arret.nom]=[arrets_inconnus[arret.nom][0], arrets_connus[arrets_inconnus[arret.nom][1]][1] + [arret.nom], arrets_connus[arrets_inconnus[arret.nom][1]][2] + [old_arret.ligne[indice_arret_v]]]
        del arrets_inconnus[arret.nom]


def affichage_foremost(chemin):
    for i in range(1, len(chemin[1])):
        print("aller à", chemin[1][i], "avec la", chemin[2][i])

def get_new_arret_foremost(arrets_inconnus, liste_tot):
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0]


        for i in liste_tot:
            if i.nom==nom_arret:
                return i  
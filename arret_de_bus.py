from operator import contains
from horaires import *
from math import inf
import operator

class Arret_de_bus:
    '''
    Arrets voisin = [[ligne, arret_suivant, arret_precedent], [ligne, arret_suivant, arret_precedent]]
    Horaires=[[ligne, horaire_suivant, horaire_precedent], [ligne,horaire_suivant, horaire_precedent]]
    Horairesjf=[[ligne, horairejf_suivant, horairejf_pecedent], [ligne, horairejf_suivant, horairejf_precedent]]
    '''

    def __init__(self, nom):
        self.nom = nom
        self.arrets_voisins=[]
        self.horaires=[]
        self.horaires_jf=[]

    def __str__(self):
        return  "arret : " + self.nom
   
    def add_arret(self, new_arret):
        if new_arret not in self.arrets_voisins:
            self.arrets_voisins.append(new_arret)
            new_arret.arrets_voisins.append(self)

    def liste_arrets(self, liste=[]):
        if self not in liste:
            liste.append(self)
        for i in self.arrets_voisins:
            if i not in liste:
                i.liste_arrets(liste)
        return liste    

    def add_horaire(self, horaire):
        self.horaires.append(horaire)    

    def add_horaire_jf(self, horaire_jf):
        self.horaires_jf.append(horaire_jf) 

    def djikstra(self, dep, dest) :
        noeud_courant=dep
        a_visiter=self.liste_arrets([])
        liste_tot=self.liste_arrets([])
        liste_dist=init_liste_distances(self ,liste_tot)
        liste_chemin=init_chemin(dep, liste_tot)
        arrets_connus={noeud_courant:[0,[noeud_courant]]}
        print(liste_chemin)

        while a_visiter != [] or noeud_courant != dest:
            maj_a_visiter(noeud_courant, a_visiter)
            print("noeud courant : ", noeud_courant.nom)
            mise_a_jour(noeud_courant, liste_dist, liste_tot, liste_chemin, a_visiter)
            noeud_courant=get_new_noeud_courant(noeud_courant, a_visiter, liste_dist, liste_tot)


            print(liste_chemin)
            print(liste_dist)

        return liste_dist





'''
    def distance_entre_deux_arrets_adjacents_minutes(self, dep,  dest):
            dep=changer_string_en_heure(self.horaires[self.arrets_voisins.index(dest)][0])
            dest=changer_string_en_heure(dest.horaires[dest.arrets_voisins.index(self)][0])
'''

def init_dico_listes_distances(dep):
    dict={}

    for i in dep.liste_arrets():
        i=0
    pass






def get_new_noeud_courant(noeud_courant, liste_arrets_a_visiter, liste_distances, liste_tot):
    distance_min=inf
    indice_min=-1
    indice=-1
    for n in noeud_courant.arrets_voisins:
        if n in liste_arrets_a_visiter :
            indice=liste_tot.index(n)
            if distance_min>=liste_distances[indice]:
                indice_min=indice
    return liste_tot[indice_min]


def init_liste_distances(self, liste_tot):
    liste_dist=[inf]*len(liste_tot)
    for i in range (len(liste_tot)):
        if liste_tot[i]==self:
            liste_dist[i]=0
    return liste_dist

def init_chemin(arret, liste_tot):
    l=[]
    for i in range(len(liste_tot)) :
        l.append([])
    print(len(l))
    #for j in range(len(liste_tot)):
     #   l[i][0]=arret
    return l


def maj_a_visiter(a, liste):
    liste.remove(a)
      
def mise_a_jour(arret, liste_dist, liste_tot, liste_chemin, a_visiter):
    n=0
    indice1=liste_tot.index(arret)
    liste_chemin[indice1].append(arret.nom)

    for i in range(len(arret.arrets_voisins)):
        if liste_tot[i]==arret:
            n=i

        for j in range(len(liste_tot)):
            if  arret.arrets_voisins[i]==liste_tot[j]:
                if liste_dist[n]+1<liste_dist[j]:
                    liste_dist[j]=liste_dist[n]+1
                    for i in range(len(arret.arrets_voisins)) :
                        if arret.arrets_voisins[i] in a_visiter:
                            indice2=liste_tot.index(arret.arrets_voisins[i])
                            liste_chemin[indice2] = liste_chemin[indice1] + liste_chemin[indice2]


#arrets inconnus avec la longueur et l arret precedent
#arret est inconnu
def mise_a_jour_2(arret, arrets_connus, arrets_inconnus, liste_tot):
        #arret est le noeud courant dans la liste des arrets inconnus

        for v in arret.arrets_voisins:
            if v.nom in arrets_inconnus :
               d= arrets_inconnus[arret.nom][0] + 1
               if d<arrets_inconnus[v.nom][0] :
                   arrets_inconnus[v.nom]=[d,arret.nom]
        print(arrets_inconnus)
        print(arrets_inconnus[arret.nom])
        arrets_connus[arret.nom]=[arrets_inconnus[arret.nom][0], arrets_connus[arrets_inconnus[arret.nom][1]][1] + [arret.nom]]
        del arrets_inconnus[arret.nom]


def dij_dico(dep, dest):
    noeud_courant=dep
    liste_tot=dep.liste_arrets([])
    arrets_connus={noeud_courant.nom:[0,[noeud_courant.nom]]}
    arrets_inconnus={k.nom:[inf,''] for k in liste_tot if k!=noeud_courant}


    for voisin in dep.arrets_voisins:
        arrets_inconnus[voisin.nom]=[1, dep.nom]
    while arrets_inconnus !=[] and any(arrets_inconnus[k][0]<inf for k in arrets_inconnus):
        noeud_courant=get_new_arret_2(arrets_inconnus, liste_tot)

        mise_a_jour_2(noeud_courant, arrets_connus, arrets_inconnus, liste_tot)

    return arrets_connus[dest.nom]


def get_new_arret_2(arrets_inconnus, liste_tot):
    if arrets_inconnus != []:
        nom_arret=min(arrets_inconnus.items(), key=operator.itemgetter(1))[0]
        print(arrets_inconnus.items())
        for i in liste_tot:
            if i .nom==nom_arret:
                return i        

    
    
    

if __name__=="__main__":
    #test avec 3 arrets        a1 -> a5 -> a2 -> a3 -> a4 -> a1
    a1=Arret_de_bus("soleil levant")
    a2=Arret_de_bus("cimetiere")
    a3=Arret_de_bus("plessis piquet")
    a4=Arret_de_bus("marche")
    a5=Arret_de_bus("theatre")

    h_sc=["10:10", "11:11"]
    h_cp=["10:13", "11:14"]
    h_pm=["10:16", "11:17"]
    h_ms=["10:19", "11:20"]

    h_pc=["7:16", "13:17"]
    h_cs=["7:19", "13:20"]
    h_sm=["7:22", "13:23"]
    h_mp=["7:25", "13:26"]



    a1.add_arret(a5)
    a5.add_arret(a2)
    a2.add_arret(a3)
    a3.add_arret(a4)
    a1.add_arret(a4)

    a1.add_horaire(h_sc)
    a1.add_horaire(h_sm)

    a2.add_horaire(h_cs)
    a2.add_horaire(h_cp)

    a3.add_horaire(h_pc)
    a3.add_horaire(h_pm)

    a4.add_horaire(h_ms)
    a4.add_horaire(h_mp)

    a5.add_horaire(h_ms)
    a5.add_horaire(h_mp)


    print(dij_dico(a1, a3))

    
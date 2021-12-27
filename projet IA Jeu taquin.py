import time 

#Definir l'etat initial du taquin
def etat_initial():
    return [[3, 2, 7], [8, 6, 0], [1, 5, 4]]

#Verifie si l'etat courant est l'etat final
def est_etat_final(t):
    return t==[[1, 2, 3], [8, 0, 4], [7, 6, 5]]

#Retourne la posiotion de la case vide 
def position_case_vide(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if(t[i][j] == 0):
                return(i,j)

#Retourne la valeur de la case de coordonnées x,y
def numero(t,x,y):
    return t[x][y]

#Permet de permuter les plaquettes situées dans les cases de coordonnées x,y
def permutation(t,c1,c2):
    from copy import deepcopy 
    t2 = deepcopy(t) 
    #deepcopy permet de copier t dans une autre variable pour garder l'etat avant la permutation 
    aux = t2[c1[0]][c1[1]]
    t2[c1[0]][c1[1]] = t2[c2[0]][c2[1]]
    t2[c2[0]][c2[1]] = aux 
    return t2

#Pour afficher le taquin 

def affichage(t):
    print("\t\t\t\t\t+---+---+---+")
    print("\t\t\t\t\t| %i | %i | %i |" % (t[0][0], t[0][1], t[0][2]))
    print("\t\t\t\t\t+---+---+---+")
    print("\t\t\t\t\t| %i | %i | %i |" % (t[1][0], t[1][1], t[1][2]))
    print("\t\t\t\t\t+---+---+---+")
    print("\t\t\t\t\t| %i | %i | %i |" % (t[2][0], t[2][1], t[2][2]))
    print("\t\t\t\t\t+---+---+---+")

#Retourne la liste des noeuds generes d'un etat donnée
def transitions(t):
    #Permet de donnée la liste des coordonnées des cases voisins de la case de coordonnées(x,y)=p  
    def possible_transition(t,p):
        poses = []
        if (p[0]>0) :
            poses.append((p[0]-1,p[1]))
        if p[1]>0:
            poses.append((p[0],p[1]-1))
        if (p[0] < len(t)-1):
            poses.append((p[0]+1,p[1]))
        if (p[1] < len(t)-1):
            poses.append((p[0],p[1]+1))
        return poses

    p = position_case_vide(t)
    poses = possible_transition(t,p)#liste poses contient les coordonnées des voisins de la case vide
    trans = []
    # Permet de permuter la case vide avec les elements de la liste poses
    for pos in poses :
        trans.append(permutation(t,p,pos))
    return trans


# Recherche en largeur => parcourir l'arbre niveau par niveau 
def recherche_en_largeur(t,ef):
    start=time.time()
    #On a cree la listeopenqui contient les noeuds a examiner , la liste niveau pour sauvgarder 
    # le niveau de chaque  noeud 
    #et la liste closed qui contient les noeuds deja examinées
    Open = [t] 
    closed =[]
    niveau = [0] 
    #n1 et n sont utiliser pour l'affichage de niveau 
    n1 = 0
    n = 0
    #affichage de l'etat initail
    print('\t\t        __________________ niveau',n,'__________________ ')
    affichage(t)
    while(Open != []):
       #Retirer la premiere noeud de la liste open et le rajouter dans la liste closed 
       noeud = Open.pop(0)
       closed.append(noeud)
       n1 = n # n1 contient le niveau du dernier noeud examiné
       #Retirer son niveau de la liste niveau
       n = niveau.pop(0)#n contient le niveau du  noeud a examiner
       if((n!= n1)and(n!=0)):#si n <> n1 on affiche le niveau de noeud donc on a passé au niveau suivant
            print('\t\t        __________________ niveau',n,'__________________ ')
       if(n!=0):
         affichage(noeud)  
         print('\t\t\t\t    ______________________  \n')
       #Verifier si le noeud est l'état final 
       # si c'est le cas la racherche est terminer et on le retourne
       if (noeud == ef):
           print("Etat final")
           print("liste open ",len(Open))
           print("liste closed",len(closed))
           return noeud
       #Sinon on va determiner les etats generes du noeud et les ajouter a la fin de la liste open 
       #et on ajoute leur niveau dans la liste niveau 
       childs = transitions(noeud)  
       for child in childs:
           if (child not in closed) and (child not in Open):
                Open.append(child)
                niveau.append(n+1)
       print('Time spent:%0.2fs'%(time.time()-start))
    

    




def recherche_en_profondeurlimite(t,ef,l):
    start=time.time()
    #On a cree la liste Open qui contient les noeuds a examiner 
    # ainsi que la liste niveau pour sauvgarder le niveau de chaque  noeud 
    #et la liste closed qui contient les noeuds deja examinées
    Open= [t]
    closed=[]
    niveau = [0]
    while(Open != []):
        #tant que la valeur du 1er element de liste niveau est > a la limite donnée on le supprime 
        # et la noeud correspondant dans la liste Open
        while (niveau[0]>l): 
            Open.pop(0)
            niveau.pop(0)
            if niveau == []:
                break;
            
        if(Open == []):
           print("pas de solution")  
        
        else : 
            #Retirer la premiere noeud de la liste Open et le rajouter dans la liste closed  
            noeud = Open.pop(0)
            closed.append(noeud)
            #n contient le niveau du  noeud a examiner
            n = niveau.pop(0)
            print('\t\t        __________________ niveau',n,'__________________ ')
            affichage(noeud)
            #Verifier si le noeud est l'état final 
            #si c'est le cas la racherche est terminer et on le retourne
            if (noeud == ef):
                 print("Etat final")
                 print("liste open ",len(Open))
                 print("liste closed",len(closed))
                 return noeud  
            #Sinon on va determiner les etats generes du noeud et les ajouter au debut  de la liste Open 
            # et on ajoute leur niveau dans la liste niveau 
            childs = transitions(noeud)  
            for child in childs :
                if (child not in closed) and (child not in Open) :
                    if(n<l):
                     Open.insert(0,child)
                     niveau.insert(0,n+1)
        print('Time spent:%0.2fs'%(time.time()-start))

#Fonction h retourne le nombre de cases differents du t par rapport aux cases de l'état final
def h(t,ef):
    i = 0
    for j in range(len(t)):
        for k in range(len(t[j])):
            if(t[j][k] != ef[j][k]):
             i += 1
    return i



def recherche(t,ef):
    start=time.time()
    #On a cree la liste Open qui contient les noeuds a examiner
    # et la liste closed qui contient les noeuds deja examinées
    Open= []
    closed = []
    niveau = 0 
    success = False
    Open.append(t)  
    while(Open != [] and not success):
        #Retirer la premiere noeud de la liste open et le rajouter dans la liste closed 
        noeud = Open[0]
        print('\t\t        __________________ niveau',niveau,'__________________ ')
        affichage(noeud)
        niveau += 1 
        Open.remove(noeud)
        closed.append(noeud)
        #Verifier si le noeud est l'état final 
        # si c'est le cas la racherche est terminer et on le retourne avec son niveau
        if(noeud == ef):
            success = True
            print("liste open ",len(Open))
            print("liste closed",len(closed))
            affichage(noeud)
        #Sinon on va determiner les etats generes du noeud 
        # et les ajouter a la fin de la liste open et on ajoute leur niveau dans la liste niveau 
        else:
            childs = transitions(noeud)  
            for child in childs:
                if (child in Open) or (child in closed):
                    childs.remove(child)
            Open=Open+ childs
            #on va trié les noeuds de la liste Open selon leur fonction d'évalution
            Open.sort(key = lambda e:( niveau+h(e,ef) ))
        print('Time spent:%0.2fs'%(time.time()-start))



t = [[1,2,3],[8,6,0],[7,5,4]]
ef = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print("\n\t-----------Recherche en profondeur limité-----------\t\n")
p = recherche_en_profondeurlimite(t,ef,3)
print("\n\t-----------Recherche en largeur-----------\t\n")
l = recherche_en_largeur(t,ef)
print("\n\t-----------Recherche A*-----------\t\n")
a= recherche(t,ef)

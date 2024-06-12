print("Hello World !!!!")
print("C'est la tache 4")
print("Aminata est notre SCRUM")

                                        ### Liste
# Cr�er une liste avec les noms de quatres animaux
animaux = [" lion", "girafe", "chat", "souris", "chien", "chameau"]
# Afficher le premier �l�ment de animaux
print(animaux[0])
# Afficher le dernier �l�ment de animaux
print(animaux[-1])
# Afficher le quatrieme �l�ment de animaux
print(animaux[3])

                                        #### Op�ration sur les listes
animaux1 = ['cerf', 'leopard', 'mouton']

# Concat�ner deux listes 
conc_ani = animaux + animaux1
print(conc_ani)
# R�p�ter une liste 
rep_ani1 = animaux1 * 3
print(rep_ani1)
#Comme pour les strings, ce sont les deux seuls operations possibles les listes
                                    #### Remplacer un element d'une liste
#Remplacer le premier element de la liste animaux1 par 'taureau'
animaux1[0] = 'taureau'
print(animaux1)
#Remplacer le dernier element de la liste animaux1 par 'chevre'
animaux1[-1] = "chevre"
print(animaux1)

                                    #### Rajouter un �l�ment dans une liste
# Avec la concatenation                                     
animaux1 = animaux1 + ["scorpion"]
print(animaux1)

# Fonction append()
animaux1.append('cafard')
print(animaux1)

# Rajouter une liste dans une liste
animaux1.append(["singe", "chat", "souris"]) 
print(animaux1)
a = ["singe", "chat", "souris"]

print(animaux1)
# Afficher le dernier element du dernier element avec indexation negative
print(animaux1[-1][-1])

# Afficher le dernier element du dernier element avec indexation positive
print(animaux1[len(animaux)-1][len(animaux1[len(animaux1)-1])-1])


# Afficher les �l�ments rajout�s en utilisant les index -1 et -2

animaux1 = ['taureau', 'leopard', 'chevre', 'scorpion', 'cafard', ['singe', 'chat', 'souris']]



                                        #### Tranches
# Afficher les deux premiers �l�ments de la liste
print(animaux1[:2]) #Indexation positive
print(animaux1[: -len(animaux)+1]) #Indexation negative

# Afficher les deux derniers �l�ments de la liste
print(animaux1[len(animaux1)-2:]) #Indexation positive
print(animaux1[-2:]) #Indexation negative

# Afficher les �l�ments avec un pas de 2 
print(animaux1[:len(animaux1):2]) #Indexation positive
print(animaux1[::2]) #Indexation positive
print(animaux1[-len(animaux1): : 2]) #Indexation negative

#Afficher les element de l'index 3 jusqu'au dernier avec un pas de 2
print(animaux1[3: :2]) #Indexation positive
print(animaux1[-len(animaux1) +3 : :2]) #Indexation negative

                                        ### Fonction len()
len(animaux1)

                                        ### Les fonctions range() et list()
# Generer des valeurs entieres de 0 a 10
print(range(0,11))
print(list(range(0,11))) #Pour afficher les elements il faut coupler avec list() 
# Generer des valeurs entieres de 0 a 20
print(list(range(0,21)))                
# Generer des valeurs entieres de 0 a 20 avec un pas de 3                       
print(list(range(0,21,3)))
# Generer des valeurs entieres de 0 a 100 
print(list(range(0,101)))
# Generer des valeurs entieres de 0 a 100 avec un pas de 10
print(list(range(0,101,10)))


                                    #### Listes de listes
animaux3 = [["chat", "chameau", "chamelle"], ["chien", "leopard", "tigre"], ["grenouille", "dragon"]]
# Afficher Chamelle
print(animaux3[0][2]) #Indexation positive
print(animaux3[0][-len(animaux3)+2]) #Indexation negative

#Afficher Chien
print(animaux3[1][0]) #Indexation positive
print(animaux3[-len(animaux3)+1][-len(animaux3[1])]) #Indexation negative

                                    ### Minimum, maximum et somme d'�une liste
val = list(range(0,11))
print(val)
# Afficher le minimum
min(val)
# Afficher le maximum
max(val)
# Sommer les valeurs de val
sum(val)

# Impossible de chercher le maximum dans une liste ou il y a des str
# val_ani = ["girafe", "lion", 1, 2, 3, 6.6]
# max(val_ani)

# S'il n'y a que des str il fait le classement par ordre alphabetique
val_ani1 = [ "girafe", "lion", "anophele", "chat", "mouton", "zebre"]
max(val_ani1)
min(val_ani1)


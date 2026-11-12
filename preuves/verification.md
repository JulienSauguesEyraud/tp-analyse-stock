# Verification du projet

Pour chaque cas, coller la commande, sa sortie, et votre explication.

1. Jeu initial de quatre articles.
- commande : docker run --rm -v "${PWD}/entrees:/entrees" -v "resultats:/resultats" analyse-stock:v1
- sortie : 
    References : 4
    Unites : 16
    Valeur totale : 670.00 EUR
    References en stock faible : 3
    References en rupture : 1
- explication : 

2. CSV modifie sans reconstruction.
- commande : docker run --rm -v "${PWD}/entrees:/entrees" -v "resultats:/resultats" analyse-stock:v1
- sortie : 
    References : 4
    Unites : 36
    Valeur totale : 830.00 EUR
    References en stock faible : 2
    References en rupture : 0
- explication : en rajoutant 20 cables les valeurs se mettent à jour sans avoir besoin de rebuild car on donne le chemin dans la commande elle n'est pas copiée dans l'image comme le stock.py

3. Tentative d'ecriture dans entrees en lecture seule.
- commande : docker run --rm -v "${PWD}/entrees:/entrees:ro" -v "resultats:/resultats" analyse-stock:v1
- sortie : 
    References : 4
    Unites : 36
    Valeur totale : 830.00 EUR
    References en stock faible : 2
    References en rupture : 0
- explication : ça ne change rien car entrées n'est pas écrit juste lu

4. Rapport relu depuis un autre conteneur avec le meme volume nomme.
- commande : docker run --rm -v "resultats:/resultats" ubuntu:24.04 cat /resultats/bilan-stock.txt
- sortie : 
    References : 4
    Unites : 36
    Valeur totale : 830.00 EUR
    References en stock faible : 2
    References en rupture : 0
- explication : Même si le conteneur est supprimer après chaque execution, le fichier bilan-stock est enregistré dans le volume résultats donc on peut juste lire ce fichier

5. Entree absente, vide ou invalide.
- commande : docker run --rm -v "${PWD}/entrees:/entrees" -v "resultats:/resultats" analyse-stock:v1
- sortie : 
    Erreur : [Errno 2] No such file or directory: '/entrees/stock.csv'

    What's next:
        Debug this container error with Gordon → docker ai "help me fix this container error"
- explication : En supprimant le dossier entrees on reçoit une erreur car le script python en a besoin
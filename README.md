# Analyse de stock avec Docker

## Auteurs
Julien Saugues--Eyraud et Mathis Gilgenkrantz

## Construction
Indiquer votre commande et expliquer votre Dockerfile.

commande : docker build -t analyse-stock:v1 .

explications : 
- FROM ubuntu:24.04 pour avoir une base ubuntu 24.04
- RUN apt-get update \
    && apt-get install -y  --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/* pour installer python3
- WORKDIR /app pour choisir app comme dossier de travail
- COPY stock.py . pour copier stock.py
- CMD ["python3", "stock.py"] pour exécuter ce programme par défaut

## Execution avec montages
Donner les commandes pour votre terminal et expliquer les chemins.
commandes : docker run --rm -v "${PWD}/entrees:/entrees" -v "resultats:/resultats" analyse-stock:v1

## Tests et resultats
Renvoyer vers preuves/verification.md et decrire le resultat attendu.

## Reproduction apres git clone
Donner les etapes exactes, notamment la creation de resultats.

1. Se placer dans le dossier du projet.
2. Vérifier que le dossier `entrees` contient le fichier `stock.csv`.
3. Créer le volume Docker nommé `resultats` avec la commande :
docker volume create resultats

4. Construire l'image Docker :
docker build -t analyse-stock:v1 .

5. Exécuter le conteneur :
docker run --rm -v "${PWD}/entrees:/entrees:ro" -v "resultats:/resultats" analyse-stock:v1

6. Consulter le rapport généré :
docker run --rm -v "resultats:/resultats" ubuntu:24.04 cat /resultats/bilan-stock.txt

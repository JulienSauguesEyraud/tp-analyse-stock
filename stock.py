import argparse
import csv
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


def calculer_statistiques(articles):
    dictionnaire = {"references" : 0, "unites" : 0, "valeur" : 0, "faibles" : 0, "ruptures" : 0}

    references = len(articles)
    unites = 0
    valeur = 0
    faibles = 0
    ruptures = 0
    for i in range(references):
        unites = unites + articles[i][1]
        valeur = valeur + (articles[i][1] * articles[i][2])
        if articles[i][1] < 5 :
            faibles = faibles + 1
            if articles[i][1] <= 0:
                ruptures = ruptures + 1
    dictionnaire["references"] = references
    dictionnaire["unites"] = unites
    dictionnaire["valeur"] = valeur
    dictionnaire["faibles"] = faibles
    dictionnaire["ruptures"] = ruptures
    return dictionnaire


def lire_articles(source):
    with source.open(encoding="utf-8-sig", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        if lecteur.fieldnames != ["article", "quantite", "prix_unitaire"]:
            raise ValueError("Colonnes : article,quantite,prix_unitaire")
        articles = []
        for ligne in lecteur:
            nom = ligne["article"]
            quantite = int(ligne["quantite"])
            prix = Decimal(ligne["prix_unitaire"])
            if not nom or quantite < 0 or not prix.is_finite() or prix < 0:
                raise ValueError("Nom requis, quantite et prix non negatifs.")
            articles.append((nom, quantite, prix))
    if not articles:
        raise ValueError("Le fichier ne contient aucun article.")
    return articles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--entree", default="/entrees/stock.csv")
    parser.add_argument("--sortie", default="/resultats/bilan-stock.txt")
    args = parser.parse_args()
    try:
        stats = calculer_statistiques(lire_articles(Path(args.entree)))
        rapport = "\n".join([
            f"References : {stats['references']}",
            f"Unites : {stats['unites']}",
            f"Valeur totale : {stats['valeur']:.2f} EUR",
            f"References en stock faible : {stats['faibles']}",
            f"References en rupture : {stats['ruptures']}",
        ]) + "\n"
        sortie = Path(args.sortie)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(rapport, encoding="utf-8")
    except (OSError, ValueError, InvalidOperation, TypeError, NotImplementedError) as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 2
    print(rapport, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

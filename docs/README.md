# INSAnonym-utils

## Qu'est-ce que insanonym-utils?

Insanonym-utils est une librarie python créée pour faciliter l'anonymisation de tables. 
Ce projet utilise la librarie pandas pour créer des dataframes et ainsi gagner en rapidité.

## Pourquoi ?

De nombreuses implémentations peuvent exister pour anonymiser un algorithme, mais par expérience, elles ne sont pas toutes optimales.

Certaines implémentations effectuent le processus d'anonymisation ligne par ligne.

D'autres utilisent des Dataframes, mais n'utilisent pas les méthodes qui permettent d'effectuer des opérations rapidement ([comparatif](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)).

### A noter

Attention toutefois: cette librairie ne dispose que de quelques algorithmes simples, et peu efficaces. Le but de la librarie est seulement de faciliter l'écriture, et le traitement des algorithmes sur un dataframe.

## Documentation

### Premiers pas

- Pour comprendre le fonctionnement de la librairie, veuillez vous référer aux [premiers pas](https://github.com/danymat/INSAnonym-utils/blob/main/docs/premiers-pas.md).
- Pour connaitre les algorithmes fournis par la librairie, consulter la section [Algorithmes](https://github.com/danymat/INSAnonym-utils/blob/main/docs/algorithmes.md).
- Pour apprendre à créer ses propres algorithmes, consulter la section [Création d'Algorithmes](https://github.com/danymat/INSAnonym-utils/blob/main/docs/creation-algorithmes.md).




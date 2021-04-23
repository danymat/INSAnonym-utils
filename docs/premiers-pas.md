# Premiers pas

Pour utiliser le script il vous faudra un fichier de configuration, intitulé `parser.cfg`.

Voici un exemple de fichier de configuration:

```json
{
    "name": "dataset1.csv",
    "path": ".",
    "columns": [
        {"name": "id", "column_type":"int" },
        {"name": "date", "column_type":"int" },
        {"name": "latitude", "column_type":"int" },
        {"name": "longitude", "column_type":"int" }
    ],
    "algorithms": [
        { "name": "delete", "options": { "columns": [1,2] } }
    ],
    "file_type": "csv",
    "export": "False",
    "export_rules": {
        "output_name": "output_df",
        "output_format": "csv"
    }
}
```

Ce fichier va lire la table `dataset1.csv` dans le répertoire courant, contenant 4 colonnes, et va appliquer l'algorithme de pseudo-anonymisation sur les colonnes 1 et 2, soit sur `date` et `latitude` respectivement.

- `"name"` - le nom de la table à anonymiser
- `"path"` - le répertoire de la table à anonymiser
- `"columns"`- un ensemble de colonne, où chaque colonne doit avoir les champs:
    - `"name"` - le nom de la colonne
    - `"column_type"` - le type de la colonne 
- `"algorithms"` - un ensemble d'algorithmes (aller à la section Algorithmes pour plus de détails)
- `"file_type"` - le type de fichier de la table à anonymiser (`csv`,`json`)
- `"export"` - (Optionnel, défaut: True) exporte la table résultante (`False`, `True`)
- `"export_rules"` - réglages d'exportation de la table:
    - `"output_name"` - le nom de sortie de la table exportée
    - `"output_format"` - le format d'exportation de la table (`csv`,`json`)

*Note: toutes les commandes suivantes seront effectuées dans l'interpreteur python:*

1. Créer un fichier de configuration simple, intitulé `parser.cfg`.

Vous pouvez utiliser la commande `sample()` pour générer un fichier basique:

```python
from insanonym_utils import utils
utils.sample()
```

Le fichier sera généré dans votre répertoire courant et intitulé `parser.cfg`. 

Vous pouvez ensuite le modifier pour refléter votre table.

2. Nous allons ensuite lire le fichier de configuration

```python
from insanonym_utils import models
model = models.FileConfigModel.parse_file('parser.cfg') 
# Vous pouvez aussi spécifier un chemin absolu pour votre fichier de configuration: 
# e.g models.FileConfigModel.parse_file('path/to/file/parser.cfg')
```

3. Nous allons ensuite utiliser ce fichier de configuration pour charger la table en mémoire:

```python
from insanonym_utils import runner
r = runner.Runner(model)
```

La base de données est maintenant chargée en mémoire. vous pouvez la visualiser en effectuant la commande:

```python
print(r.dataframe)
```

4. La Dataframe ayant fini de charger, nous pouvons executer les algorithmes spécifiés dans le fichier de configuration:

```python
r.execute()
```

La dataframe résultant sera accessible par:
```python
print(r.dataframe)
```

Par défaut, `r.execute()` enregistre la table résultante avec le nom spécifié dans le fichier de configuration.
Passer `"export": "False"` dans le fichier de configuration va prévenir la sauvegarde automatique.

Si toutefois vous voulez enregistrer la table résultante, vous pouvez le faire grâce au runner:

```python
r.save()
```

## Multiples runners

Si vous avez besoin de faire tourner plusieurs algorithmes indépendamment les uns des autres, vous pouvez le faire.
Il vous suffit alors de créer un autre modèle prenant un autre fichier de configuration, tel que:

```python
model2 = models.FileConfigModel.parse_file('new_config_file.cfg') 
```

Et ainsi créer un deuxieme runner:

```python
r2 = runner.Runner(model2)
```

A noter toutefois qu'une deuxième Dataframe sera créée, donc cela peut s'avérer lourd si votre machine ne le supporte pas.

## Considérations

Nous vous proposons d'effectuer des tests sur des versions tronquées de votre table initiale, si sa taille originale est grande.

Pour information, voici le temps de calcul de chaque étape du cycle sur un fichier de `1.7Go` (plus de `34 millions` de lignes):

- Creation du runner (ouverture de la table en dataframe): `42.08s`.
- Execution de l'algorithme `delete` sur une colonne: `1.83s`(Voir la section [algorithmes](algorithmes.md#delete) pour plus de détails).
- Enregistrement de la table résultante: `1m.47s` (Format de sortie: csv)

Pour pouvoir executer les opérations aussi rapidement, pandas a du mettre en RAM toute la table. 

Assurez vous d'avoir une bonne configuration (au moins 8Go de RAM).

(Les tests ont été effectués sur une machine personnelle, donc les specs sont ci-dessous)

```
OS: macOS 11.3 20E5217a x86_64
CPU: Intel i5-7360U (4) @ 2.30GHz
GPU: Intel Iris Plus Graphics 640
Memory: 8192MiB
```


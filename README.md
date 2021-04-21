# INSAnonym-utils

INS'Anonym-utils dispose d'une librarie capable d'effectuer des opérations sur une table, dans le but de l'anonymiser.

Pour l'instant, elle est capable de:

- Créer un dataframe à partir de la table.
- Effectuer l'algorithme de pseudo-anonymisation sur un ensemble de colonnes.
- Exporter la dataframe au format choisi.

## Installation

Prérequis:

- [Poetry](https://python-poetry.org/docs/#installation)

```
git clone https://github.com/danymat/INSAnonym-utils.git
cd INSAnonym-utils
poetry install 
```

## Usage

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

Ce fichier va lire la table `dataset1.csv` dans le répertoire courant, contenant 4 colonnes, et va appliquer l'algorithme de pseudo-anonymisation sur les colonnes 1 et 2, soit `date` et `latitude` respectivement.

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

1. Créer un fichier de configuration selon vos paramètres, au répertoire racine du projet

2. Executer la commande:
```
poetry run anon
```

## Testing

Run the tests:
```bash
cd tests
poetry run pytest
```

## Roadmap

- Créer la section algorithmes dans les docs
- Ajouter plus d'algorithmes
- Donner la possibilité d'ajouter des algorithmes 
- Ajouter un docker d'installation

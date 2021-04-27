# Algorithmes

## Liste des algorithmes fournis

- [Delete](#delete)
- [Delete IDs](#delete_ids)
- [Disturb](#disturb)
- [Pseudo](#pseudo)

Note: la documentation de l'implémentation des algorithmes se trouve [ici](https://danymat.github.io/INSAnonym-utils/algorithms.html).

## Schema

Tous les algorithmes doivent être sous la forme:

```json
...
"algorithms": [
    { 
        "name": "", 
        "options": {}  
    }
]
...
```

Avec: 
- `name` le nom de l'algorithme
- `options` un object d'options

*Note: les algorithmes s'exécutent suivant leur ordre dans le fichier de configuration*

## Delete

### Résumé

Delete remplace toutes les valeurs des colonnes spécifiées par un texte de remplacement.

### Fichier de configuration

```json
...
"algorithms": [
    { 
        "name": "delete", 
        "options": { 
            "columns": ["id"], 
            "alias": "*"
        } 
    }
]
...
```

- `"delete"` le nom de l'algorithme
- `"columns"` une liste de noms de colonnes à supprimer
- `"alias"` (Optionnel, defaut: `Nan`) le texte de remplacement

## Delete_Ids

### Résumé

Remplace tous les ID spécifiés par un alias

### Fichier de configuration

```json
...
"algorithms": [
    { 
        "name": "delete_ids", 
        "options": { 
            "column": "id", 
            "ids": [512, 12],
            "alias": "*"
        } 
    }
]
...
```

- `"delete_ids"` le nom de l'algorithme
- `"column"` le nom de la colonne des identifiants
- `"ids"` une liste d'identifiants à supprimer
- `"alias"` (Optionnel, defaut: `"DEL"`) le texte de remplacement

## Disturb

### Résumé

Ajoute une perturbation [-parameter,+parameter] sur une colonne de la table.
Cet algorithme utilise la loi uniforme pour effectuer la perturbation.

### Fichier de configuration

```json
...
"algorithms": [
    { 
        "name": "disturb", 
        "options": { 
            "column": "id", 
            "parameter": 0.6
        } 
    }
]
...
```

- `"disturb"` le nom de l'algorithme
- `"column"` le nom de la colonne à perturber
- `"parameter"` le paramètre de perturbation (loi uniforme)

## Pseudo

### Résumé

Effectue une pseudo-anonymisation sur les valeurs d'une colonne.

### Fichier de configuration

```json
...
"algorithms": [
    { 
        "name": "pseudo", 
        "options": { 
            "column": "id"
        } 
    }
]
...
```

- `"disturb"` le nom de l'algorithme
- `"column"` le nom de la colonne à perturber
